class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary 


    @property
    def name(self):
        """Permite leer el nombre usando 'employee.ame."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Permite modificar el nombre de manera controlada."""
        if isinstance(new_name, str) and new_name.strip() != "":
            self._name = new_name
        else:
            print("[!] El nombre debe ser una cadena válida.")

    @property
    def salary(self):
        """Permite consultar el salario usando 'employee.salary'."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Valida que el salario NUNCA sea menor a 0."""
        if value < 0:
            raise ValueError("[!] Error: El salario no puede ser negativo.")
        self._salary = float(value)

    
    def promote(self, percentage):
        """Incrementa el salario segun un porsentaje dado (ej: 0.1 para 10%)."""
        if percentage > 0:
            increase = self._salary * percentage
            self.salary += increase
        else:
            print("[!] El porcentaje de aumento debe ser mayor a 0.")


print("=== Prueba Ejercicio Extra 1 ===")
employee = Employee("Ana", 1000)
print(f"Salario inicial de {employee.name}: ${employee.salary:.2f}")

employee.promote(0.1)
print(f"Salario con auento: ${employee.salary:.2f}")
