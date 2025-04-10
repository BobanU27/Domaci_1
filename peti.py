#5. Dvostruko olančana lista za filmove

class FilmNode:
    def __init__(self, naziv, zanr, godina, ocjena):
        self.film = {'naziv': naziv, 'zanr': zanr, 'godina': godina, 'ocjena': ocjena}
        self.next = None
        self.prev = None

class DoublyLinkedListFilms:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def print(self):
        current = self.head
        while current:
            print(f"Naziv: {current.film['naziv']}, Žanr: {current.film['zanr']}, Godina: {current.film['godina']}, Ocjena: {current.film['ocjena']}")
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
            if current.film['godina'] == year:
                count += 1
                suma += current.film['ocjena']
            current = current.next
        
        return suma / count if count != 0 else None
    
    def film_by_year(self, year):
        current = self.head
        while current:
            if current.film['godina'] >= year:
                print(f"Naziv: {current.film['naziv']}, Žanr: {current.film['zanr']}, Godina: {current.film['godina']}, Ocjena: {current.film['ocjena']}")
            current = current.next
    
    def film_by_zanr(self, zanr):
        current = self.head
        count = 0
        while current:
            if current.film['zanr'] == zanr:
                count += 1
            current = current.next
        return count

# Test funkcije
f1 = FilmNode("Dune", "Sci-Fi", 2021, 8.5)
f2 = FilmNode("The Godfather", "Crime", 1972, 9.2)
f3 = FilmNode("Oppenheimer", "Drama", 2023, 8.9)
f4 = FilmNode("Barbie", "Comedy", 2023, 7.5)
f5 = FilmNode("Avatar", "Sci-Fi", 2009, 7.9)
f6 = FilmNode("Joker", "Drama", 2019, 8.4)
f7 = FilmNode("Spider-Man", "Action", 2021, 8.2)

film_lista = DoublyLinkedListFilms()
for film in [f1, f2, f3, f4, f5, f6, f7]:
    film_lista.append(film)

print("Svi filmovi:")
film_lista.print()

print("\n Prosječna ocjena filmova iz 2021:")
print(film_lista.prosjek_by_year(2021))

print("\n Filmovi iz 2019 i noviji:")
film_lista.film_by_year(2019)

print("\n Broj Sci-Fi filmova:")
print(film_lista.film_by_zanr("Sci-Fi"))

print("\n Broj Drama filmova:")
print(film_lista.film_by_zanr("Drama"))