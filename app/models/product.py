from sqlalchemy import Column, Integer, String, Float, Numeric
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key= True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float, index=True)
    stock = Column(Integer)
    category = Column(String, index=True)
    
    