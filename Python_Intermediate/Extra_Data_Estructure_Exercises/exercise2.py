class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data, next=self.head)
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if self.head is None:
            print("La lista está vacía")
            return 

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print(f"Valor '{data}' no encontrado en la lista")

    def print_all(self):
        if self.head is None:
            print("Lista Vacía")
            return

        current = self.head
        output = ""
        while current is not None:
            output += str(current.data)
            if current.next is not None:
                output += " -> "
            current = current.next
        print(output)


print("\n=== PRUEBA LINKED LIST ===")
ll = LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.print_all()

ll.insert_back(30)
ll.print_all()

ll.delete(10)
ll.print_all()

print("\n--- Casos límite Linked List ---")
ll.delete(20)  
ll.print_all()
ll.delete(99)  
ll.delete(30)  
ll.print_all()