from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from schemas import DishCreate, DishResponse
from services import get_dishes_services, create_dish_services, delete_dish_categories_services

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/dishes")
def get_dishes(db: Session = Depends(get_db)):
    dishes = get_dishes_services(db)
    return {
        "message": "Thanh cong!",
        "data": dishes
    }
    
@app.post("/dishes")
def create_dish(dish: DishCreate, db: Session = Depends(get_db)):
    new_dish = create_dish_services(dish, db)
    return {
        "message": "Thanh cong!",
        "data": new_dish
    }
    
@app.delete("/dish-categories/{id}")
def delete_dish_category(id: int, db: Session = Depends(get_db)):
    delete_dish = delete_dish_categories_services(id, db)
    raise HTTPException(
        status_code=status.HTTP_200_OK,
        detail="Xoa thanh cong!"
    )