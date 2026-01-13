from fastapi import APIRouter, HTTPException
from typing import List
from fastapi import FastAPI, Depends
from psycopg import IntegrityError
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import Base, engine, get_db
from backend.models import ApplicationMaster, ConsentMaster,TemplateMaster, TenantMaster
from backend.models import TenantMaster
import backend.schemas as schemas
from backend.models import ProductMaster
from backend.models import CdMaster
from fastapi.middleware.cors import CORSMiddleware   


# ---------------------------
# FastAPI setup
# ---------------------------
app = FastAPI(title="Master APIs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "UP", "message": "Service is healthy"}




# ---------------------------
# Tenant APIs
# ---------------------------
@app.post("/tenants", response_model=schemas.TenantRead)
def create_tenant(data: schemas.TenantCreate, db: Session = Depends(get_db)):
    tenant = TenantMaster(**data.dict())
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant

@app.get("/tenants", response_model=List[schemas.TenantRead])
def get_all_tenants(db: Session = Depends(get_db)):
    return db.query(TenantMaster).all()

@app.get("/tenants/{tenant_id}", response_model=schemas.TenantRead)
def get_tenant(tenant_id: str, db: Session = Depends(get_db)):
    tenant = db.query(TenantMaster).filter(TenantMaster.tenant_id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@app.put("/tenants/{tenant_id}", response_model=schemas.TenantRead)
def update_tenant(tenant_id: str, data: schemas.TenantCreate, db: Session = Depends(get_db)):
    tenant = db.query(TenantMaster).filter(TenantMaster.tenant_id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(tenant, key, value)
    db.commit()
    db.refresh(tenant)
    return tenant

@app.delete("/tenants/{tenant_id}")
def delete_tenant(tenant_id: str, db: Session = Depends(get_db)):
    tenant = db.query(TenantMaster).filter(TenantMaster.tenant_id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    db.delete(tenant)
    db.commit()
    return {"detail": "Tenant deleted"}

# ---------------------------
# Application APIs
# ---------------------------
@app.post("/applications", response_model=schemas.ApplicationRead)
def create_application(data: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    application = ApplicationMaster(**data.dict())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

@app.get("/applications", response_model=List[schemas.ApplicationRead])
def get_all_applications(db: Session = Depends(get_db)):
    return db.query(ApplicationMaster).all()

@app.get("/applications/{appln_id}", response_model=schemas.ApplicationRead)
def get_application(appln_id: str, db: Session = Depends(get_db)):
    application = db.query(ApplicationMaster).filter(ApplicationMaster.appln_id == appln_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@app.put("/applications/{appln_id}", response_model=schemas.ApplicationRead)
def update_application(appln_id: str, data: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    application = db.query(ApplicationMaster).filter(ApplicationMaster.appln_id == appln_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(application, key, value)
    db.commit()
    db.refresh(application)
    return application

@app.delete("/applications/{appln_id}")
def delete_application(appln_id: str, db: Session = Depends(get_db)):
    application = db.query(ApplicationMaster).filter(ApplicationMaster.appln_id == appln_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"detail": "Application deleted"}

# ---------------------------
# Product APIs
# ---------------------------
@app.post("/products", response_model=schemas.ProductRead)
def create_product(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = ProductMaster(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.get("/products", response_model=List[schemas.ProductRead])
def get_all_products(db: Session = Depends(get_db)):
    return db.query(ProductMaster).all()

@app.get("/products/{prod_id}", response_model=schemas.ProductRead)
def get_product(prod_id: str, db: Session = Depends(get_db)):
    product = db.query(ProductMaster).filter(ProductMaster.prod_id == prod_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{prod_id}", response_model=schemas.ProductRead)
def update_product(prod_id: str, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(ProductMaster).filter(ProductMaster.prod_id == prod_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{prod_id}")
def delete_product(prod_id: str, db: Session = Depends(get_db)):
    product = db.query(ProductMaster).filter(ProductMaster.prod_id == prod_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}

# ---------------------------
# Consent APIs
# ---------------------------
@app.post("/consents", response_model=schemas.ConsentRead)
def create_consent(data: schemas.ConsentCreate, db: Session = Depends(get_db)):
    consent = ConsentMaster(**data.dict())
    db.add(consent)
    db.commit()
    db.refresh(consent)
    return consent

@app.get("/consents", response_model=List[schemas.ConsentRead])
def get_all_consents(db: Session = Depends(get_db)):
    return db.query(ConsentMaster).all()

@app.get("/consents/{consent_id}", response_model=schemas.ConsentRead)
def get_consent(consent_id: str, db: Session = Depends(get_db)):
    consent = db.query(ConsentMaster).filter(ConsentMaster.consent_id == consent_id).first()
    if not consent:
        raise HTTPException(status_code=404, detail="Consent not found")
    return consent

@app.put("/consents/{consent_id}", response_model=schemas.ConsentRead)
def update_consent(consent_id: str, data: schemas.ConsentCreate, db: Session = Depends(get_db)):
    consent = db.query(ConsentMaster).filter(ConsentMaster.consent_id == consent_id).first()
    if not consent:
        raise HTTPException(status_code=404, detail="Consent not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(consent, key, value)
    db.commit()
    db.refresh(consent)
    return consent

@app.delete("/consents/{consent_id}")
def delete_consent(consent_id: str, db: Session = Depends(get_db)):
    consent = db.query(ConsentMaster).filter(ConsentMaster.consent_id == consent_id).first()
    if not consent:
        raise HTTPException(status_code=404, detail="Consent not found")
    db.delete(consent)
    db.commit()
    return {"detail": "Consent deleted"}

# ---------------------------
# CD APIs
# ---------------------------
@app.post("/cd", response_model=schemas.CdRead)
def create_cd(data: schemas.CdCreate, db: Session = Depends(get_db)):
    cd = CdMaster(**data.dict())
    db.add(cd)
    db.commit()
    db.refresh(cd)
    return cd

@app.get("/cd", response_model=List[schemas.CdRead])
def get_all_cd(db: Session = Depends(get_db)):
    return db.query(CdMaster).all()

@app.get("/cd/{cd_id}", response_model=schemas.CdRead)
def get_cd(cd_id: str, db: Session = Depends(get_db)):
    cd = db.query(CdMaster).filter(CdMaster.cd_id == cd_id).first()
    if not cd:
        raise HTTPException(status_code=404, detail="CD not found")
    return cd

@app.put("/cd/{cd_id}", response_model=schemas.CdRead)
def update_cd(cd_id: str, data: schemas.CdCreate, db: Session = Depends(get_db)):
    cd = db.query(CdMaster).filter(CdMaster.cd_id == cd_id).first()
    if not cd:
        raise HTTPException(status_code=404, detail="CD not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(cd, key, value)
    db.commit()
    db.refresh(cd)
    return cd

@app.delete("/cd/{cd_id}")
def delete_cd(cd_id: str, db: Session = Depends(get_db)):
    cd = db.query(CdMaster).filter(CdMaster.cd_id == cd_id).first()
    if not cd:
        raise HTTPException(status_code=404, detail="CD not found")
    db.delete(cd)
    db.commit()
    return {"detail": "CD deleted"}

# ---------------------------
# Template APIs
# ---------------------------
@app.post("/templates", response_model=schemas.TemplateRead)
def create_template(data: schemas.TemplateCreate, db: Session = Depends(get_db)):
    template = TemplateMaster(**data.dict())
    db.add(template)
    db.commit()
    db.refresh(template)
    return template

@app.get("/templates", response_model=List[schemas.TemplateRead])
def get_all_templates(db: Session = Depends(get_db)):
    return db.query(TemplateMaster).all()

@app.get("/templates/{template_id}", response_model=schemas.TemplateRead)
def get_template(template_id: str, db: Session = Depends(get_db)):
    template = db.query(TemplateMaster).filter(TemplateMaster.template_id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

@app.put("/templates/{template_id}", response_model=schemas.TemplateRead)
def update_template(template_id: str, data: schemas.TemplateCreate, db: Session = Depends(get_db)):
    template = db.query(TemplateMaster).filter(TemplateMaster.template_id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(template, key, value)
    db.commit()
    db.refresh(template)
    return template

@app.delete("/templates/{template_id}")
def delete_template(template_id: str, db: Session = Depends(get_db)):
    template = db.query(TemplateMaster).filter(TemplateMaster.template_id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    db.delete(template)
    db.commit()
    return {"detail": "Template deleted"}
from fastapi.responses import JSONResponse
import traceback

@app.exception_handler(Exception)
async def global_exception_handler(request, exc: Exception):
    print("🔥 INTERNAL SERVER ERROR 🔥")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )
