class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("El Sytack esta vacio")
            return None

        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node

    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(f" {current_node.data} ")
            current_node = current_node.next
        print("------------------------")


print("=== PRUEBA STACK ===")
plate1 = Node("Plato 1 (Abajo)")
plate2 = Node("Plato 2 (Medio)")
plate3 = Node("Plato 3 (Arriba)")

stack = Stack()
stack.push(plate1)
stack.push(plate2)
stack.push(plate3)

print("Estado de la pila")
stack.print_structure()

print("Haciendo POP (quitando el último que entró):")
removed = stack.pop()
print(f"Nodo removido: {removed.data}")

print("Estado final de la pila")
stack.print_structure()

print("\n--- Probando caso límite: Stack vacío ---")
empty_stack = Stack()
empty_stack.pop()

