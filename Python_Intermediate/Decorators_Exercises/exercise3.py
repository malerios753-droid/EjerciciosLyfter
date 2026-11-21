from datetime import date


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        calculated_age = today.year - self.date_of_birth.year
        has_not_passed_birthday = (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        if has_not_passed_birthday:
            calculated_age -= 1
        return calculated_age



def adults_only(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("[!] El primer parámetro debe ser un objeto de tipo User.")

        if user.age < 18:
            raise PermissionError(f"[X] Acceso denegado: {user.name} tiene {user.age} años.")

        return func(user, *args, **kwargs)

    return wrapper


# --- PRUEBA DEL EJERCICIO 3 ---
@adults_only
def enter_vip_club(user):
    print(f"[✓] Bienvenid@ al club VIP, {user.name}! (Edad: {user.age} años)")


adult_user = User("Carlos", date(1998, 5, 15))
minor_user = User("Lucía", date(2012, 8, 20))

enter_vip_club(adult_user)