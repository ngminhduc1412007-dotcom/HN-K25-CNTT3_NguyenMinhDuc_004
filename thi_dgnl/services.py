from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Dishes, Dish_Categories
from schemas import DishCreate, DishResponse

def get_dishes_services(db: Session):
    get_dish = db.query(Dishes).all()
    return get_dish

def create_dish_services(dish: DishCreate, db: Session):
    dishes = dish.model_dump()
    new_dish = Dishes(**dishes)
    try:
        db.add(new_dish)
        db.commit()
        db.refresh(new_dish)
    except:
        db.rollback()
        return
    
def delete_dish_categories_services(id: int, db: Session):
    find_id = db.query(Dish_Categories).filter(Dish_Categories.id == id).first()
    if find_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Khong tim thay"
        )
    
    db.delete(find_id)