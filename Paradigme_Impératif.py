#Saisie des données
def saisir_donnees():
    noms = []
    notes = []
    nb_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))
    for i in range(nb_etudiants):
        nom = input(f"Nom de l’étudiant {i + 1} : ")
        note = float(input(f"Note de {nom} : "))
        noms.append(nom)
        notes.append(note)
    return noms, notes

#Calcul de la moyenne
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

#Répartition des étudiants
def afficher_repartition(noms, notes):
    reussite = [noms[i] for i in range(len(notes)) if notes[i] >= 10]
    echec = [noms[i] for i in range(len(notes)) if notes[i] < 10]
    print(f"Étudiants ayant réussi : {', '.join(reussite)}")
    print(f"Étudiants en échec : {', '.join(echec)}")

#Meilleure note
def meilleure_note(noms, notes):
    max_note = max(notes)
    index_max = notes.index(max_note)
    print(f"L’étudiant ayant la meilleure note est {noms[index_max]} avec {max_note}.")

def rechercher_etudiant(noms, notes, nom_recherche):
        if nom_recherche in noms:
            index = noms.index(nom_recherche)
            print(f"{nom_recherche} a obtenu la note de {notes[index]}.")
        else:
            print(f"{nom_recherche} n'est pas dans la liste des étudiants.")

# Programme principal
def main():
    noms, notes = saisir_donnees()
    moyenne = calculer_moyenne(notes)
    print(f"La moyenne de la classe est de {moyenne:.2f}.")
    afficher_repartition(noms, notes)
    meilleure_note(noms, notes)

# Recherche d'un étudiant par son nom
    nom_recherche = input("Entrez le nom de l'étudiant à rechercher : ")
    rechercher_etudiant(noms, notes, nom_recherche)

if __name__ == "__main__":
    main()