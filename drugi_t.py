#t) Prebrojavanje elemenata većih od zadate vrijednosti

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        if not self.head:
            self.head = new_element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next
    
    def custom_count(self, value):
        count = 0
        current = self.head
        
        while current:
            if current.value > value:
                count += 1
            current = current.next
            
        return count

# Test funkcije
l1 = LinkedList()
for value in [12, 5, 18, 9, 25, 7]:
    l1.append(Node(value))

print("Lista:")
l1.print_list()

threshold = 10
print(f"Broj elemenata većih od {threshold}:", l1.custom_count(threshold))  