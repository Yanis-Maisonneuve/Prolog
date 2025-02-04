from functools import reduce

# Utilisation de sum()
def somme_fonctionnelle_sum(liste):
    return sum(liste)

# Utilisation de reduce()
def somme_fonctionnelle_reduce(liste):
    return reduce(lambda x, y: x + y, liste)

def somme_imperative(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

# Essaies
print(somme_imperative([1, 2, 3, 4]))
print(somme_fonctionnelle_sum([1, 2, 3, 4]))  # Output: 10
print(somme_fonctionnelle_reduce([1, 2, 3, 4]))  # Output: 10