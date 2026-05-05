from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List 
from app.database import get_db
from app.schemas.product import ProductCreate
from app.models.product import Product 
from app.auth.dependencies import get_current_user
router = APIRouter()

#crear producto 
@router.post("/products", response_model = ProductCreate)
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    nuevo_producto = Product(
    name=product.name,
    price=product.price,
    stock=product.stock
)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    
    return nuevo_producto

#recibir todos los productos 
@router.get("/products", response_model = List[ProductCreate])
def get_products(db: Session = Depends(get_db)):
    productos = db.query(Product).all()
    return productos 

#editar producto 
@router.put("/products/{product_id}", response_model = ProductCreate)
def update_product(product_id:int ,product: ProductCreate, db: Session = Depends(get_db)):
    producto = db.query(Product).filter(Product.id == product_id).first()
    if not producto:
        raise HTTPException(status_code= 404, detail="Producto no encontrado")
    producto.name = product.name
    producto.price = product.price
    producto.stock = product.stock 
    db.commit()
    db.refresh(producto)
    return producto 

#eliminar producto 
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    producto = db.query(Product).filter(Product.id == product_id).first()
    if not producto:
        raise HTTPException(status_code= 404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"message":"producto eliminado correctamente"}


