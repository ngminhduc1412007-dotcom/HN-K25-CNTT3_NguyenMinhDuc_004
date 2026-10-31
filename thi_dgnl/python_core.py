raw_dishes =[
    {"dish_code": "F301", "category": "main",
    "price": 150000, "status": "available"},
    {"dish_code": "f101 ", "category": "appetizer",
    "price": 55000, "status": "available"},
    {"dish_code": "F202", "category": "dessert",
    "price": 45000, "status": "sold_out"},
    {"dish_code": "F102", "category": "appetizer",
    "price": 65000, "status": "unavailable"},
    {"dish_code": "F302", "category": "main",
    "price": 180000, "status": "available"}
]
    
# Linear Search
def search_dishes(price, status):
    matches = []
    for dish in raw_dishes:
        if dish["price"] == price and dish["status"] == status:
            matches.append(dish)
    return matches
    
# Bubble Sort
def sort_dishes_by_price_desc():
    for i in range(len(raw_dishes) - 1):
        for j in range(len(raw_dishes) - 1 - i):
            if raw_dishes[j]["price"] < raw_dishes[j + 1]["price"]:
                raw_dishes[j], raw_dishes[j + 1] = raw_dishes[j + 1], raw_dishes[j]
    return raw_dishes
            