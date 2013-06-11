:- modeh(*,parent(+person,-person)).
:- modeb(*,father(+person,-person)).

:- determination(parent/2,father/2).

person(a).
person(b).
person(c).
person(d).

father(a,b).
father(b,c).
father(c,d).

