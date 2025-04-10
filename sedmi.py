#7. Dvostruko olančana lista za studente

class StudentNode:
    def __init__(self, ime, prezime, godina, prosjek):
        self.student = {'ime': ime, 'prezime': prezime, 'godina': godina, 'prosjek': prosjek}
        self.next = None
        self.prev = None

class DoublyLinkedListStudents:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def print(self):
        current = self.head
        while current:
            print(f"Student: {current.student['ime']} {current.student['prezime']}, Godina: {current.student['godina']}, Prosjek: {current.student['prosjek']}")
            current = current.next
    
    def append(self, novi_element):
        if not self.head:
            self.head = novi_element
            self.tail = novi_element
        else:
            self.tail.next = novi_element
            novi_element.prev = self.tail
            self.tail = novi_element
    
    def prosjek_by_year(self, year):
        current = self.head
        count = 0
        suma = 0
        
        while current:
            if current.student['godina'] == year:
                count += 1
                suma += current.student['prosjek']
            current = current.next
        
        return suma / count if count != 0 else None
    
    def print_before_index_reverse(self, index):
        if index <= 0:
            return
        
        current = self.head
        position = 1
        
        # Pronalazi element na zadatom indeksu
        while current and position < index:
            current = current.next
            position += 1
        
        if not current:
            return
        
        # Štampa elemente unazad do početka liste
        prev_node = current.prev
        while prev_node:
            print(f"Student: {prev_node.student['ime']} {prev_node.student['prezime']}, Godina: {prev_node.student['godina']}, Prosjek: {prev_node.student['prosjek']}")
            prev_node = prev_node.prev

# Test funkcije
s1 = StudentNode("Ana", "Marković", 1, 8.5)
s2 = StudentNode("Marko", "Petrović", 2, 9.2)
s3 = StudentNode("Jelena", "Nikolić", 3, 7.8)
s4 = StudentNode("Stefan", "Jovanović", 1, 8.9)
s5 = StudentNode("Milica", "Đorđević", 2, 9.5)
s6 = StudentNode("Nikola", "Stanković", 3, 8.2)
s7 = StudentNode("Tamara", "Popović", 1, 9.0)

student_lista = DoublyLinkedListStudents()
for student in [s1, s2, s3, s4, s5, s6, s7]:
    student_lista.append(student)

print(" Svi studenti:")
student_lista.print()

print("\n Prosječna ocjena studenata prve godine:")
print(student_lista.prosjek_by_year(1))

print("\n Studenti prije indeksa 5 (unazad):")
student_lista.print_before_index_reverse(5)