def factorielle_fonctionnelle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle_fonctionnelle(n - 1)

def factorielle_imperative(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

#Essaies
print(factorielle_fonctionnelle(5))
print(factorielle_imperative(5))