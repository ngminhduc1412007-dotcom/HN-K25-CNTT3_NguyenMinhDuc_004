from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Dish_Categories(Base):
    __tablename__ = "dish_categories"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    dish = relationship("dish_category", back_populates="dish")
    
class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    dish_code = Column(String(10), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    dish_category_id = Column(Integer, ForeignKey("dish_categories.id"))
    dish_category = relationship("dishes", back_populates="dish_category")