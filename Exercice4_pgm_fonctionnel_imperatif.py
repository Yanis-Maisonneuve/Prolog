def carre_elements_fonctionnel(liste):
    return list(map(lambda x: x ** 2, liste))

def carre_elements_imperatif(liste):
    result = []
    for element in liste:
        result.append(element ** 2)
    return result

#Essaies
print(carre_elements_fonctionnel([1, 2, 3, 4]))
print(carre_elements_imperatif([1, 2, 3, 4]))