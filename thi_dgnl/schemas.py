from pydantic import BaseModel, Field
from typing import Optional

class DishCategotyCreate(BaseModel):
    id: int
    name: str
    
class DishCreate(BaseModel):
    id: int
    dish_code: str
    price: float
    dish_category_id: int
    
class DishResponse(BaseModel):
    statusCode: int
    error: str
    message: str
    data: str
    