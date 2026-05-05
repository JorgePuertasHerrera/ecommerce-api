from fastapi import FastAPI
from app.database import engine, Base 
from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem
from app.routers.product import router as product_router
from app.routers.user import router as user_router
app = FastAPI()
app.include_router(product_router)
app.include_router(user_router)
#importar modelos 
Base.metadata.create_all(bind=engine)
