products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]


category_totals = {}


for product in products:
    category = product["category"]
    price = product["price"]
    
    
    if category in category_totals:
        category_totals[category] += price
    else:
        category_totals[category] = price


print(category_totals)