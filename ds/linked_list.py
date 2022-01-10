class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        

class Linked_List:
    def __init__(self):
        self.head = None
        self.last = None
            
    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = self.last.next
    
    def print(self):
        pointer = self.head
        while pointer != None:
            print(pointer.value, end='')
            print('->', end='')
            pointer = pointer.next
        print('None')
    
    def delete(self, value):
        if self.head == None:
            return IndexError("empty")
        pointer = self.head
        prev = None
        while pointer.value != value:
            if pointer == None:
                return ("there is no value in linked list")
            prev = pointer
            pointer = pointer.next
        prev.next = pointer.next
        pointer.next = None
        if prev.next == None:
            self.last = prev
        
            
                
        


list = Linked_List()
list.insert(3)
list.insert(5)
list.insert(1)
list.insert(10)
list.print()
list.delete(1)
list.print()
list.delete(10)
list.print()
list.insert(7)
list.print()
            