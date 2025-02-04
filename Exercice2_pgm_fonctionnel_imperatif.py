def filtrer_pairs_fonctionnel(liste):
    return list(filter(lambda x: x % 2 == 0, liste))

def filtrer_pairs_imperatif(liste):
    pairs = []
    for element in liste:
        if element % 2 == 0:
            pairs.append(element)
    return pairs

# Essaies
print(filtrer_pairs_imperatif([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]
print(filtrer_pairs_fonctionnel([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]