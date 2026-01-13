import uuid
from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class TenantCreate(BaseModel):
    tenant_name: str
    tenant_code: str
    status: str = "ACTIVE"

class TenantRead(TenantCreate):
    tenant_id: uuid.UUID
    class Config:
        orm_mode = True

class ApplicationCreate(BaseModel):
    tenant_id: uuid.UUID
    appln_name: str
    appln_desc: str | None = None
    appln_owner: str | None = None
    status: str = "ACTIVE"

class ApplicationRead(ApplicationCreate):
    appln_id: uuid.UUID
    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    appln_id: uuid.UUID
    prod_name: str
    prod_desc: str | None = None
    prod_type: str | None = None
    onboarding_type: str | None = None
    expected_completion_days: int | None = None
    allow_concurrent: bool = False
    status: str = "ACTIVE"

class ProductRead(ProductCreate):
    prod_id: uuid.UUID
    class Config:
        orm_mode = True

class ConsentBase(BaseModel):
    appln_id: UUID
    consent_name: str
    consent_type: Optional[str] = None
    status: Optional[str] = "ACTIVE"

class ConsentCreate(ConsentBase):
    pass

class ConsentRead(BaseModel):
    consent_id: UUID
    appln_id: UUID
    consent_name: str
    consent_type: Optional[str]
    status: Optional[str]

    class Config:
        from_attributes = True

class CdCreate(BaseModel):
    appln_id: uuid.UUID
    field_code: str
    field_name: str
    field_type: str | None = None
    is_mandatory: bool = False
    status: str = "ACTIVE"

class CdRead(CdCreate):
    cd_id: uuid.UUID
    class Config:
        orm_mode = True

class TemplateCreate(BaseModel):
    appln_id: uuid.UUID
    template_name: str
    template_type: str | None = None
    status: str = "ACTIVE"

class TemplateRead(TemplateCreate):
    template_id: uuid.UUID
    class Config:
        orm_mode = True
