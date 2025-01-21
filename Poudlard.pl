suspect(drago).
suspect(neville).
suspect(ginny).

declaration(drago, innocent(neville)).
declaration(neville, innocent(ginny)).
declaration(ginny, innocent(drago)).
declaration(ginny, innocent(neville)).

innocent(X) :- \+ coupable(X).

coupable(X) :- suspect(X), \+ innocent(X).

un_seul_coupable([X]) :- coupable(X).
un_seul_coupable([X|T]) :- innocent(X), un_seul_coupable(T).

trouver_coupable(Coupable) :-
    findall(S, suspect(S), Suspects),
    un_seul_coupable(Suspects),
    member(Coupable, Suspects),
    coupable(Coupable).
