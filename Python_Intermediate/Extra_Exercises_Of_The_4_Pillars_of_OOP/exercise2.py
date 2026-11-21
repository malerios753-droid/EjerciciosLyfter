from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_role(self):
        """Metodo abstracto: cada clase hija debe devolver su rol."""
        pass

    @abstractmethod
    def has_permission(self, permission):
        """Metodo abstracto: cada clase hija debe evaluar los permisos."""
        pass

class AdminUser(User):
    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True

class RegularUser(User):
    def __init__(self, username, allowed_permissions=None):
        super().__init__(username)
        if allowed_permissions is None:
            self.allowed_permissions = ["read"]
        else:
            self.allowed_permissions = allowed_permissions

    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        return permission in self.allowed_permissions



print("\n=== Prueba Ejercicio Extra 2 ===")
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(f"¿{user1.username} ({user1.get_role()}) tiene permiso 'delete'?: {user1.has_permission('delete')}")
print(f"¿{user2.username} ({user2.get_role()}) tiene permiso 'delete'?: {user2.has_permission('delete')}")
print(f"¿{user2.username} ({user2.get_role()}) tiene permiso 'read'?: {user2.has_permission('read')}")

    