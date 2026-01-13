
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from db import Base
from sqlalchemy import Boolean
from sqlalchemy import DateTime
status = Column(String, nullable=False, default="ACTIVE")


maker_dt = Column(DateTime(timezone=True), server_default=func.now())



class TenantMaster(Base):
    __tablename__ = "tenant_master"
    tenant_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_name = Column(String(255), nullable=False, unique=True)
    tenant_code = Column(String(50), nullable=False, unique=True)
    status = Column(String(20), default="ACTIVE")

class ApplicationMaster(Base):
    __tablename__ = "application_master"

    appln_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant_master.tenant_id"), nullable=False)

    appln_name = Column(String(255), nullable=False, unique=True)
    appln_desc = Column(String)
    appln_owner = Column(String)

    status = Column(String(20), default="ACTIVE")

    maker_id = Column(UUID(as_uuid=True), nullable=False)
    maker_dt = Column(DateTime(timezone=True), default=datetime.utcnow)

class ProductMaster(Base):
    __tablename__ = "product_master"
    prod_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    appln_id = Column(UUID(as_uuid=True), ForeignKey("application_master.appln_id"), nullable=False)
    prod_name = Column(String(255), nullable=False)
    prod_desc = Column(String(500))
    prod_type = Column(String(50))
    onboarding_type = Column(String(50))
    expected_completion_days = Column(Integer)
    allow_concurrent = Column(Boolean, default=False)
    status = Column(String(20), default="ACTIVE")

class ConsentMaster(Base):
    __tablename__ = "consent_master"

    consent_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    appln_id = Column(
        UUID(as_uuid=True),
        ForeignKey("application_master.appln_id"),
        nullable=False
    )

    consent_code = Column(String(100), nullable=False)
    consent_name = Column(String(255), nullable=False)
    consent_type = Column(String(100))
    status = Column(String(20), default="ACTIVE")

    created_dt = Column(DateTime(timezone=True), server_default=func.now())



class CdMaster(Base):
    __tablename__ = "cd_master"
    cd_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    appln_id = Column(UUID(as_uuid=True), ForeignKey("application_master.appln_id"), nullable=False)
    field_code = Column(String(50), nullable=False)
    field_name = Column(String(255), nullable=False)
    field_type = Column(String(50))
    is_mandatory = Column(Boolean, default=False)
    status = Column(String(20), default="ACTIVE")

class TemplateMaster(Base):
    __tablename__ = "template_master"
    template_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    appln_id = Column(UUID(as_uuid=True), ForeignKey("application_master.appln_id"), nullable=False)
    template_name = Column(String(255), nullable=False)
    template_type = Column(String(50))
    status = Column(String(20), default="ACTIVE")
