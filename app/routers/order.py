from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from typing import List 
from app.database import get_db
from app.schemas.order import OrderCreate 
from app.models.order_item import OrderItem
from app.models.product import Product  
from app.models.order import Order 
from app.auth.dependencies import get_current_user
from app.schemas.user import UserLogin
router = APIRouter()

@router.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # 1. Crear el pedido
    nuevo_pedido = Order(
        user_id=current_user.id,
        status="pending",
        total_price=0
    )
    db.add(nuevo_pedido)
    db.flush()  # Para obtener el id sin hacer commit
    
    # 2. Crear cada item
    total = 0
    for item in order.items:
        producto = db.query(Product).filter(Product.id == item.product_id).first()
        if not producto:
            raise HTTPException(404, f"Producto {item.product_id} no encontrado")
        nuevo_item = OrderItem(
            order_id=nuevo_pedido.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=producto.price
        )
        total += producto.price * item.quantity
        db.add(nuevo_item)
    
    nuevo_pedido.total_price = total
    db.commit()
    db.refresh(nuevo_pedido)
    return {"order_id": nuevo_pedido.id, "total": total, "status": "pending"}

#obtener pedidos 
@router.post("/orders", response_model= OrderCreate)
def get_orders(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
 pedidos = db.query(Order).filter(Order.user_id == current_user.id).all()
 return pedidos

git add .
git commit -m "Add GET orders endpoint"
git push