class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Crea un nodo con el dato y lo agrega al final de la cola."""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """Elimina el primer nodo de la cola y retorna su dato."""
        if self.head is None:
            print("La cola está vacía")
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_data

    def print_all(self):
        """Imprime todos los elementos de la cola en orden (A -> B -> C)."""
        if self.head is None:
            print("Cola vacía")
            return

        current = self.head
        output = ""
        while current is not None:
            output += str(current.data)
            if current.next is not None:
                output += " -> "
            current = current.next
        print(output)


print("=== PRUEBA QUEUE ===")
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()

removed = q.dequeue()
print(f'Elemento eliminado: "{removed}"')  
q.print_all()

print("\n--- Casos límite Queue ---")
q.dequeue() 
q.dequeue()  
q.print_all()  
q.dequeue()

    

