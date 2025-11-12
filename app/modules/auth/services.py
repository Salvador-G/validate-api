from datetime import datetime, timedelta
from fastapi import HTTPException, status, Request
from typing import Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError
import os

from app.modules.auth.models import User, Session as UserSession, PasswordReset, AuditLog
from app.modules.auth.schemas import UserCreate, LoginSchema, AuditLogCreate

# Configuración de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Clave secreta y algoritmo para el JWT
SECRET_KEY = os.getenv("SECRET_KEY", "secret_key_default")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
MAX_PASSWORD_LENGTH = 72

# Función para crear el hash de una contraseña
def get_password_hash(password: str) -> str:
    if len(password.encode("utf-8")) > MAX_PASSWORD_LENGTH:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La contraseña no puede exceder los {MAX_PASSWORD_LENGTH} caracteres."
        )
    return pwd_context.hash(password)


# Verificar la contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # También validamos en login
    if len(plain_password.encode("utf-8")) > MAX_PASSWORD_LENGTH:
        return False
    return pwd_context.verify(plain_password, hashed_password)


# Crear token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Registrar nuevo usuario
def create_user(db: Session, user: UserCreate):
    # Generar username concatenando first_name y last_name
    if user.first_name and user.last_name:
        username = f"{user.first_name.lower()}_{user.last_name.lower()}"
    elif user.first_name:
        username = user.first_name.lower()
    else:
        username = user.email.split("@")[0]  # fallback si no hay nombres
        
    db_user = User(
        username=username,
        email=user.email,
        password_hash=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Autenticar usuario y crear sesión
def authenticate_user(db: Session, login_data: LoginSchema):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.password_hash):
        return None

    access_token = create_access_token(data={"sub": str(user.id)})

    db_session = UserSession(
        user_id=user.id,
        token=access_token,
        expires_at=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    return {"user": user, "token": access_token}


# Registrar evento en bitácora (audit log)
def create_audit_log(db: Session, log_data: AuditLogCreate, request: Request):
    log_entry = AuditLog(
        user_id=log_data.user_id,
        action=log_data.action,
        ip_address=request.client.host,
        extra_data=log_data.extra_data,
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry


# Verificar validez del token JWT
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
