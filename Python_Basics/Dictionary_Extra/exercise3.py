employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]


grouped_by_department = {}


for employee in employees:
    department = employee["department"]
    
    
    if department not in grouped_by_department:
        grouped_by_department[department] = []
    
    
    grouped_by_department[department].append(employee)

print(grouped_by_department)