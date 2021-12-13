
from typing import List
from pydantic import BaseModel
   
    
class ProductBase(BaseModel):
    name: str
    description: str


class ProductOut(ProductBase):
    id: int
    
    class Config:
        orm_mode = True
    

class ProductCreate(ProductBase):
    pass
  
class ProductUpdate(ProductBase):
    pass



class CatalogBase(BaseModel):
    name: str


class CatalogOut(CatalogBase):
    id: int

    class Config:
        orm_mode = True
     

class CatalogCreate(CatalogBase):
    pass

class CatalogUpdate(CatalogBase):
    pass