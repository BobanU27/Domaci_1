#m) Posljednje veliko slovo u stringu

def get_last_capital(word):
    if len(word) == 0:
        return None
    elif word[-1].isupper():
        return word[-1]
    else:
        return get_last_capital(word[:-1])

# Test funkcije
test_string1 = "Neka Ulazna Recenica"

print("Posljednje veliko slovo u '{}':".format(test_string1), get_last_capital(test_string1))  
