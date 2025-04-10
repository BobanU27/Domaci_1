#f) Najveći element liste rekurzivno

def max_liste(lista):
    max_val = float('-inf')
    
    def pom_max_liste(lista):
        nonlocal max_val
        if len(lista) == 0:
            return max_val
        else:
            if lista[0] > max_val:
                max_val = lista[0]
            return pom_max_liste(lista[1:])
    
    return pom_max_liste(lista)

# Test funkcije
test_lista = [23, 45, 12, 67, 34, 56]
print("Najveći element liste:", max_liste(test_lista)) 