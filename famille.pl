%faits

homme('pierre').
homme('marc').
homme('paul').

femme('marie').
femme('sophie').
femme('julie').

parent('pierre', 'paul').
parent('marie', 'paul').
parent('marc' , 'sophie').
parent('jacques', 'marc').
parent('julie', 'sophie').

%Jacques est le p�re de marc
%Marc a des enfants (sophie)

pere(X, Y) :- homme(X), parent(X, Y), write(X), write(' est le pere de '), write(Y), nl.
mere(X, Y) :- femme(X), parent(X, Y), write(X), write(' est la mere de '), write(Y), nl.

grandparent(X, Y) :- parent(X, Z), parent(Z, Y), write(X), write(' est le grand-parent de '), write(Y), nl.
grandpere(X, Y) :- homme(X), grandparent(X, Y), write(X), write(' est le grand-pere de '), write(Y), nl.
grandmere(X, Y) :- femme(X), grandparent(X, Y), write(X), write(' est la grand-mere de '), write(Y), nl.


%On ne sait pas qui est le grand pere de Paul avec les faits actuel
%Jacques est bien le grand pere de Sophie

frereousoeur(X, Y) :- parent(Z, X), parent(Z, Y), X = Y, write(X), write(' est le frere ou la soeur de '), write(Y), nl.
frere(X, Y) :- homme(X), frereousoeur(X, Y) , write(X), write(' est le frere de '), write(Y), nl.
soeur(X, Y) :- femme(X), frereousoeur(X, Y) , write(X), write('est la soeur de '), write(Y), nl.

%Paul n'as pas de frere ou de soeur avec les faits actuel

%Requete
%findall(X, homme(X), L).
%findall(X, parent(X, sophie), L).

longueur([], 0).
longueur([_ | Queue], N) :- longueur(Queue, M), N is M + 1.

elementpresent(X, [X|]).
elementpresent(X, [|T]) :- element_present(X, T).

oncle(X, Y) :- frere(X, Z), parent(Z, Y).
tante(X, Y) :- soeur(X, Z), parent(Z, Y).

%Marc n'est pas l'oncle de Paul avec les faits actuel
%Sophie n'as pas oncle avec les faits actuel


cousin(X, Y) :- parent(Z, X), frereousoeur(Z,W), parent(W, Y).


