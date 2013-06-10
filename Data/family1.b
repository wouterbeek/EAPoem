% Simple illustration of the use of Aleph6 to induce family relationships.
% Author: Eszter Fodor
% Version: 06/2013


% ========================================= %
% This section is the type declaration      %
% ========================================= %

:- modeh(*,parent(+person,-person)).
:- modeb(*,father(+person,-person)).
:- modeb(*,mother(+person,-person)).

:- modeh(*,sibling(+person,+person)).
:- modeb(*,father(+person,+person)).
:- modeb(*,mother(+person,+person)).


:- determination(parent/2,father/2).
:- determination(parent/2,mother/2).

:- determination(sibling/2, father/2).
:- determination(sibling/2, mother/2).
:- determination(sibling/2, parent/2).


% ======================================== %
% This section is the background knowledge %
% ======================================== %

person(ken).
person(laura).
person(george).
person(harriet).
person(melissa).
person(bob).
person(alice).
person(sharon).


father(bob,george).
father(alice,george).
father(harriet,ken).
father(melissa,ken).
father(sharon,george).

mother(bob,harriet).
mother(alice,harriet).
mother(harriet,laura).
mother(melissa,laura).
mother(sharon,harriet).


%			     ken 	+	laura	
%				/	  		/
%		melissa  &	harriet		+	george
%							 \	  /
%						bob 	& 	alice	& sharon







