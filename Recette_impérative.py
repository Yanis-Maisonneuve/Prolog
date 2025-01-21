recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "jambon_beurre": ["pain", "beurre", "jambon", "salade"]
}

def suggestions_recettes(ingredients):
    suggestions = []
    for recette, ingredients_recette in recettes.items():
        if all(item in ingredients for item in ingredients_recette):
            suggestions.append(recette)
    return suggestions