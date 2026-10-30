class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """Metodo para ingresar dinero a la cuenta."""
        if amount > 0:
            self.balance += amount
            print(f"[✓] Depositado: ${amount:.2f}. Saldo actual: ${self.balance:.2}")
        else:
            print("[!] El monto a depositar debe ser mayor a 0.")

    def withdraw(self, amount):
        """Metodo para retirar dinero a la cuenta."""
        if amount <= 0:
            print("[!] El monto a retirar debe ser mayor a 0.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"[✓] Retirado: ${amount:.2f}. Saldo restante: ${self.balance:.2f}")
        else:
            print("[X] Error: Fondos insuficientes.")


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0.0, min_balance=0.0):
        super().__init__(initial_balance)
        self.min_balance = float(min_balance)

    def withdraw(self, amount):
        """Retira dinero solo si el saldo resultante no cae por debajo del min_balance."""
        if amount <= 0:
            print("[!] El monto a retirar debe ser mayor a 0.")
            return

        if (self.balance - amount) < self.min_balance:
            print(f"X] Error: No se puede retirar ${amount:.2f}. El saldo quedaría por debajo del mínimo permitido (${self.min_balance:.2f}). ")
        else:
            super().withdraw(amount)



print ("=== Prueba Ejercicio 1 ===")
cuenta_ahorros = SavingsAccount(initial_balance=100.0, min_balance=20.0)

cuenta_ahorros.deposit(50.0)
cuenta_ahorros.withdraw(100.0)
cuenta_ahorros.withdraw(40.0)

        