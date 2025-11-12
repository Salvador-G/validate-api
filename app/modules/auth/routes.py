from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from app.system.db import get_db
from app.modules.auth import services
from app.modules.auth.schemas import UserCreate, LoginSchema, AuditLogCreate, TokenResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


# Registro de usuario
@router.post("/signup")
def signup(request: Request,user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(services.User).filter(services.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya está registrado.")

    new_user = services.create_user(db, user)
    services.create_audit_log(
        db,
        AuditLogCreate(
            user_id=new_user.id,
            action="signup",
            extra_data=f"Usuario {new_user.email} registrado exitosamente."
        ),
        request
    )
    return {"message": "Usuario registrado correctamente", "user": new_user.email}


# Login de usuario
@router.post("/signin")
def signin(request: Request, login_data: LoginSchema, db: Session = Depends(get_db)):
    auth_result = services.authenticate_user(db, login_data)
    if not auth_result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")

    user = auth_result["user"]
    token = auth_result["token"]

    services.create_audit_log(
        db,
        AuditLogCreate(
            user_id=user.id,
            action="login",
            metadata=f"Usuario {user.email} inició sesión."
        ),
        request
    )

    return TokenResponse(access_token=auth_result["token"])


# Verificar token
@router.get("/verify-token")
def verify_token(token: str, db: Session = Depends(get_db)):
    payload = services.verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado.")
    return {"status": "valid", "data": payload}
