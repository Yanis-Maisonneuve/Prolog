% Définition des faits : chaque recette et ses ingrédients
recette(pizza, [farine, eau, sel, levure, tomate, fromage]).
recette(salade, [laitue, tomate, concombre, vinaigre, huile]).
recette(pates_carbonara, [pates, creme, lardons, fromage, sel, poivre]).
recette(omelette, [oeufs, sel, poivre, fromage, herbes]).
recette(sandwich_jambon_beurre, [pain, beurre, jambon, salade]).

% Règle pour vérifier si tous les ingrédients d'une recette sont disponibles
recette_possible(Recette, IngredientsDisponibles) :-
    recette(Recette, IngredientsRecette),
    subset(IngredientsRecette, IngredientsDisponibles).

% Vérification si une liste est un sous-ensemble d'une autre
subset([], _).
subset([H|T], L) :- member(H, L), subset(T, L).
