#8. Brisanje knjiga s najvišom i najmanjom cijenom


class BookNode:
    def __init__(self, sifra, naziv, sifra_autora, cijena):
        self.book = {
            'sifra': sifra,
            'naziv': naziv,
            'sifra_autora': sifra_autora,
            'cijena': cijena
        }
        self.next = None
        self.prev = None

class DoublyLinkedListBooks:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def print(self):
        current = self.head
        while current:
            print(f"Knjiga: {current.book['naziv']}, Šifra: {current.book['sifra']}, Autor: {current.book['sifra_autora']}, Cijena: {current.book['cijena']} €")
            current = current.next
    
    def append(self, novi_element):
        if not self.head:
            self.head = novi_element
            self.tail = novi_element
        else:
            self.tail.next = novi_element
            novi_element.prev = self.tail
            self.tail = novi_element
    
    def remove_highest_and_lowest(self):
        if not self.head or not self.head.next:
            return
        
        # Pronalazi najvišu i najnižu cijenu
        current = self.head
        highest = float('-inf')
        lowest = float('inf')
        
        while current:
            if current.book['cijena'] > highest:
                highest = current.book['cijena']
            if current.book['cijena'] < lowest:
                lowest = current.book['cijena']
            current = current.next
        
        print(f"Najviša cijena: {highest} €")
        print(f"Najniža cijena: {lowest} €")
        
        # Uklanja knjige s najvišom i najnižom cijenom
        current = self.head
        
        while current:
            next_node = current.next
            
            if current.book['cijena'] == highest or current.book['cijena'] == lowest:
                # Ako je to prvi čvor
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                # Ako je to posljednji čvor
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                # Ako je to čvor u sredini
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            
            current = next_node

# Test funkcije
b1 = BookNode(101, "Python Programming", 201, 35.99)
b2 = BookNode(102, "Data Structures and Algorithms", 202, 49.99)
b3 = BookNode(103, "Web Development Basics", 203, 25.50)
b4 = BookNode(104, "Machine Learning", 204, 65.75)
b5 = BookNode(105, "Database Design", 205, 42.25)
b6 = BookNode(106, "Artificial Intelligence", 206, 55.50)
b7 = BookNode(107, "Computer Networks", 207, 38.75)

book_list = DoublyLinkedListBooks()
for book in [b1, b2, b3, b4, b5, b6, b7]:
    book_list.append(book)

print(" Sve knjige:")
book_list.print()

print("\n Uklanjanje knjiga s najvišom i najnižom cijenom:")
book_list.remove_highest_and_lowest()

print("\n Knjige nakon uklanjanja:")
book_list.print()