recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "jambon_beurre": ["pain", "beurre", "jambon", "salade"]
}

def recette_realizable(ingredients, ingredients_recette):
    return all(item in ingredients for item in ingredients_recette)

def suggestions_recettes(ingredients):
    return list(filter(lambda recette: recette_realizable(ingredients, recettes[recette]), recettes))