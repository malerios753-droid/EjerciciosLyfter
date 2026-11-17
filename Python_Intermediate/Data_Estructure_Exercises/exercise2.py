class DoubleNode:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class Deque:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

        if head is not None:
            curr = head
            while curr.next is not None:
                curr = curr.next
            self.tail = curr

    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("El Deque está vacío")
            return None

        removed_node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

        removed_node.next = None
        removed_node.previous = None 
        return removed_node

    def pop_right(self):
        if self.tail is None:
            print("El Deque está vacío")
            return None

        removed_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None 
        else:
            self.tail = self.tail.previous
            self.tail.next = None

        removed_node.next = None
        removed_node.previous = None
        return removed_node

    def print_structure(self):
        current_node = self.head
        output = ""
        while current_node is not None:
            output += f"[{current_node.data}] <-> "
            current_node = current_node.next
        output += "None"
        print(output)

print("\n=== PRUEBA DOUBLE ENDED QUEUE ===")
deque = Deque()

print("Agregando por la derecha: B y C")
deque.push_right(DoubleNode("B"))
deque.push_right(DoubleNode("C"))
deque.print_structure()

print("Agregando por la izquierda: A")
deque.push_left(DoubleNode("A"))
deque.print_structure()

print("\nHaciendo POP_LEFT (quita A):")
removed_left = deque.pop_left()
print(f"Nodo removido por la izquierda: {removed_left.data}")
deque.print_structure()

print("\nHaciendo POP_RIGHT (quita C):")
removed_right = deque.pop_right()
print(f"Nodo removido por la derecha: {removed_right.data}")
deque.print_structure()

print("\n--- Probando caso límite: Un solo elemento ---")

last_node = deque.pop_left()
print(f"Último nodo removido: {last_node.data}")
deque.print_structure()

print("\n--- Probando caso límite: Deque vacío ---")
deque.pop_left() 
deque.pop_right()

deque.push_left(DoubleNode("Único"))
single_right = deque.pop_right()
print(f"Nodo único removido con pop_right: {single_right.data}")
deque.print_structure()
    
