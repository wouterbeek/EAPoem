% Simple illustration of the use of Aleph to induce family relationships.
% Author: Jian Huang
% Date: 01/05/2007

% ========================================= %
% This section is the type declaration      %
% ========================================= %

:- modeh(*,parent(+person,-person)).
:- modeb(*,father(+person,-person)).
:- modeb(*,mother(+person,-person)).

:- determination(parent/2,father/2).
:- determination(parent/2,mother/2).

% ======================================== %
% This section is the background knowledge %
% ======================================== %

person(ken).
person(laura).
person(george).
person(harriet).
person(bob).
person(alice).

father(bob, george).
father(alice, george).
father(harriet, ken).

mother(bob, harriet).
mother(alice, harriet).
mother(harriet, laura).