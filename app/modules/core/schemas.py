from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel


# ============================================================
#  SETTINGS SCHEMAS
# ============================================================

class SettingBase(BaseModel):
    key: str
    value: Optional[str] = None
    description: Optional[str] = None


class SettingCreate(SettingBase):
    pass


class SettingUpdate(BaseModel):
    value: Optional[str] = None
    description: Optional[str] = None


class SettingRead(SettingBase):
    id: str
    updated_at: datetime

    class Config:
        from_attributes = True


# ============================================================
#  API KEYS SCHEMAS
# ============================================================

class ApiKeyBase(BaseModel):
    name: str
    key: str
    permissions: Optional[str] = None
    is_active: Optional[bool] = True
    expires_at: Optional[datetime] = None


class ApiKeyCreate(ApiKeyBase):
    pass


class ApiKeyUpdate(BaseModel):
    name: Optional[str] = None
    permissions: Optional[str] = None
    is_active: Optional[bool] = None
    expires_at: Optional[datetime] = None


class ApiKeyRead(ApiKeyBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================
#  SYSTEM LOGS SCHEMAS
# ============================================================

class SystemLogBase(BaseModel):
    level: str  # info, warning, error
    message: str
    context: Optional[Any] = None


class SystemLogCreate(SystemLogBase):
    pass


class SystemLogRead(SystemLogBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================
#  MODULE STATUS SCHEMAS
# ============================================================

class ModuleStatusBase(BaseModel):
    module_name: str
    is_active: Optional[bool] = True
    error_message: Optional[str] = None


class ModuleStatusCreate(ModuleStatusBase):
    pass


class ModuleStatusUpdate(BaseModel):
    is_active: Optional[bool] = None
    error_message: Optional[str] = None


class ModuleStatusRead(ModuleStatusBase):
    id: str
    last_check: datetime

    class Config:
        from_attributes = True
