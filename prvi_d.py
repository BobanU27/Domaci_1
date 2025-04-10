#1. Rekurzija
#d) Rekurzivno štampanje liste

def print_list_recursive(lista):
    if len(lista) == 0:
        return
    print(lista[0])
    print_list_recursive(lista[1:])

# Test funkcije
test_lista = [42, 17, 33, 88, 91]
print("Štampanje liste rekurzivno:")
print_list_recursive(test_lista)