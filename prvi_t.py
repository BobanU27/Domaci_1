#t) Prebrojavanje parnih cifara

def count_even_digits(number):
    if number == 0:
        return 0
    
    # Uzimanje posljednje cifre
    last_digit = number % 10
    
    # Provjera da li je parna
    is_even = 1 if last_digit % 2 == 0 else 0
    
    # Rekurzivni poziv za ostatak broja
    return is_even + count_even_digits(number // 10)

# Test funkcije
test_broj1 = 246802
test_broj2 = 13579
print("Broj parnih cifara u {}: {}".format(test_broj1, count_even_digits(test_broj1)))  # Treba da vrati 6
print("Broj parnih cifara u {}: {}".format(test_broj2, count_even_digits(test_broj2)))  # Treba da vrati 0