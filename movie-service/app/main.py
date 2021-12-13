from fastapi import FastAPI, HTTPException, Depends
from api import models, schemas
from api.db  import SessionLocal, engine
from api import crud
from sqlalchemy.orm import Session
from typing import List
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/all_catalogs/', response_model=List[schemas.CatalogOut])
def list_catalogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    catalogs = crud.get_all_catalogs(db, skip=skip, limit=limit)
    return catalogs

@app.get('/catalog/{catalog_id}', response_model=schemas.CatalogOut)
def get_catalog(catalog_id: int, db: Session = Depends(get_db)):
    db_catalog = crud.get_catalog(db, catalog_id = catalog_id)
    if db_catalog is None:
        raise HTTPException(status_code=404, detail='Catalog not found')
    return db_catalog

@app.post('/create_catalog/', response_model=schemas.CatalogOut, status_code=201)
def create_catalog(catalod: schemas.CatalogCreate, db: Session = Depends(get_db)):
    db_catalog = crud.add_catalog(db=db, catalog=catalod)
    return db_catalog

@app.put('/update_catalog/{catalog_id}/', response_model=schemas.CatalogOut)
def update_catalog(catalog_id: int, catalog: schemas.CatalogUpdate, db: Session = Depends(get_db)):
    #get catalog object from database
    db_catalog = crud.get_catalog(db, catalog_id=catalog_id)
    #check if catalog object exist
    if db_catalog:
        update_catalog = crud.update_catalog(db, catalog=catalog, catalog_id=catalog_id)
        return update_catalog
    else:
        return {'error': f'Catalog with id {catalog_id} does not exist'}

@app.delete('/delete_catalog/{catalog_id}/')
def delete_catalog(catalog_id: int, db: Session = Depends(get_db)):
    #get catalog object from db
    db_catalog = crud.get_catalog(db=db, catalog_id=catalog_id)
    #check if catalog object is exist
    if db_catalog:
        db_catalog = crud.delete_catalog(db=db, catalog_id=catalog_id)
        return db_catalog
    else: 
        return {'error': 'Catalog with id {catalog_id} does not exist'}
    

@app.get('/all_products/', response_model=List[schemas.ProductOut])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_all_products(db, skip=skip, limit=limit)
    return products

@app.get('/product/{product_id}/', response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return db_product

@app.post('/create_product/', response_model=schemas.ProductOut, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product=crud.add_product(db, product)
    return db_product    
    
@app.put('/update_product/{product_id}', response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    #get product object from database
    db_product = crud.get_product(db=db, product_id=product_id)
    #check if product object exists
    if db_product:
        updated_product = crud.update_product(db, product=product, product_id=product_id)
        return updated_product
    else:
        return {"error": f"Product with id {product_id} does not exist"}


@app.delete('/delete_product/{product_id}')
def delete_product(product_id: int, db: Session = Depends(get_db)):
    #get product object from database
    db_product = crud.get_product(db=db, product_id=product_id)
    #check if product object exists
    if db_product:
        return crud.delete_product(db=db, product_id=product_id)
    else:
        return {"error": f"Product with id {id} does not exist"}

