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
plato1 = Node("Plato 1 (Abajo)")
plato2 = Node("Plato 2 (Medio)")
plato3 = Node("Plato 3 (Arriba)")

stack = Stack()
stack.push(plato1)
stack.push(plato2)
stack.push(plato3)

print("Estado de la pila")
stack.print_structure()

print("Haciendo POP (quitando el último que entró):")
removed = stack.pop()
print(f"Nodo removido: {removed.data}")

print("Estado final de la pila")
stack.print_structure

