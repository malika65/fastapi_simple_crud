from . import models, schemas
from sqlalchemy.orm import Session
from . import schemas

def get_catalog(db: Session, catalog_id: int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_catalog = db.query(models.Catalog).filter(models.Catalog.id==catalog_id).first()
    return db_catalog


def get_all_catalogs(db: Session, skip: int = 0, limit: int = 100):
    """
    Return a list of all existing Catalog records
    """
    return db.query(models.Catalog).offset(skip).limit(limit).all()


def add_catalog(db: Session, catalog: schemas.CatalogCreate):
    """
    Create a Catalog object
    """
    db_catalog = models.Catalog(**catalog.dict())
    db.add(db_catalog)
    db.commit()
    db.refresh(db_catalog)
    return db_catalog
    

def update_catalog(db: Session, catalog: schemas.CatalogUpdate, catalog_id: int):
    """
    Update a Catalog object's attribute
    """
    db_catalog = get_catalog(db, catalog_id=catalog_id)
    db_catalog.name = catalog.name
    
    db.commit()
    db.refresh(db_catalog)#refresh the attribute of the given instance
    return db_catalog

def delete_catalog(db: Session, catalog_id: int):
    """
    Delete a Catalog object
    """
    db_catalog = get_catalog(db=db, catalog_id=catalog_id)
    db.delete(db_catalog)
    db.commit() #save changes to db
    
def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    """
    Return a list of all existing Friend records
    """
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    return db_product

def add_product(db: Session, product: schemas.ProductCreate):
    """
    Create a Product object
    """
    db_product= models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product: schemas.ProductUpdate, product_id: int):
    """
    Update a Product object's attributes
    """
    db_product = get_product(db=db, product_id=product_id)
    db_product.name = product.name
    db_product.description = product.description

    db.commit()
    db.refresh(db_product) #refresh the attribute of the given instance
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Delete a Product object
    """
    db_product = get_product(db=db, product_id=product_id)
    db.delete(db_product)
    db.commit() #save changes to db