female(lakshmi).
female(sitha).
female(geetha).
female(raaji).


male(raj).
male(shiva).
male(vijay).
male(prem).

parent(lakshmi,shiva).
parent(sitha,vijay).
parent(lakshmi,prem).
parent(geetha,shiva).
parent(lakshmi,shiva).
parent(raaji,shiva).
parent(sitha,shiva).
parent(lakshmi,vijay).

mother(X,Y):-parent(X,Y),female(X)
father(X,Y):-parent(X,Y),male(X)
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X)
mother(X,Y):-parent(Z,X),parent(Z,Y),male(X)





