class DoublyNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            print("La lista doble está vacía")
            return

        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                current.next = None
                current.prev = None
                return

            current = current.next

        print(f"Valor '{data}' no encontrado")

    def print_forward(self):
        if self.head is None:
            print("Lista vacía")
            return

        current = self.head
        output = ""
        while current is not None:
            output += str(current.data)
            if current.next is not None:
                output += " -> "
            current = current.next
        print(output)

    def print_backward(self):
        if self.tail is None:
            print("Lista vacía")
            return

        current = self.tail
        output = ""
        while current is not None:
            output += str(current.data)
            if current.prev is not None:
                output += " -> "
            current = current.prev
        print(output)


print("\n=== PRUEBA DOUBLY LINKED LIST ===")
dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")

print("Forward:")
dll.print_forward()  
print("Backward:")
dll.print_backward()  

print("\nAgregando X al inicio (prepend):")
dll.prepend("X")
dll.print_forward()   
dll.print_backward()  

print("\nEliminando B:")
dll.delete("B")
dll.print_forward()   
dll.print_backward() 


print("\n--- Casos límite Doubly Linked List ---")
dll.delete("X")       
dll.delete("C")       
dll.print_forward()
dll.delete("A")       
dll.print_forward()
dll.delete("Z")
                
        
        
