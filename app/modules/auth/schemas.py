from datetime import datetime
from typing import Optional, Any
from uuid import UUID
from pydantic import BaseModel, EmailStr


# ============================================================
#  USER SCHEMAS
# ============================================================

class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = "client"
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = False


class UserCreate(UserBase):
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None


class UserRead(UserBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # equivalente moderno a orm_mode=True


# ============================================================
#  SESSION SCHEMAS
# ============================================================

class SessionBase(BaseModel):
    token: str
    refresh_token: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    expires_at: Optional[datetime] = None
    revoked: Optional[bool] = False


class SessionCreate(SessionBase):
    user_id: str


class SessionRead(SessionBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================
#  PASSWORD RESET SCHEMAS
# ============================================================

class PasswordResetBase(BaseModel):
    token: str
    expires_at: datetime
    used: Optional[bool] = False


class PasswordResetCreate(PasswordResetBase):
    user_id: str


class PasswordResetRead(PasswordResetBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================
#  TWO-FACTOR AUTH SCHEMAS
# ============================================================

class TwoFactorAuthBase(BaseModel):
    secret_key: Optional[str] = None
    is_enabled: Optional[bool] = False


class TwoFactorAuthCreate(TwoFactorAuthBase):
    user_id: str


class TwoFactorAuthRead(TwoFactorAuthBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================
#  AUDIT LOGS SCHEMAS
# ============================================================

class AuditLogBase(BaseModel):
    action: str
    ip_address: Optional[str] = None
    extra_data: Optional[Any] = None


class AuditLogCreate(AuditLogBase):
    user_id: Optional[UUID] = None


class AuditLogRead(AuditLogBase):
    id: str
    user_id: Optional[UUID] = None
    timestamp: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"