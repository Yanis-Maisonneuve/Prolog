liste_globale = []

def ajouter_fonctionnel(liste, element):
    return liste + [element]

def ajouter_imperatif(liste, element):
    liste.append(element)

#Essaies
liste = [1, 2]
nouvelle_liste = ajouter_fonctionnel(liste, 3)
print(liste)  # Output: [1, 2]
print(nouvelle_liste)  # Output: [1, 2, 3]

ajouter_imperatif(liste_globale, 1)
ajouter_imperatif(liste_globale, 2)
print(liste_globale)  # Output: [1, 2]