% ======================================= %
% The following are the positive examples %
% ======================================= %
parent(bob,george).
parent(alice,george).
parent(sharon, george).

parent(bob,harriet).
parent(alice,harriet).
parent(sharon,harriet).


parent(harriet,ken).
parent(harriet,laura).

parent(melissa,ken).
parent(melissa, laura).


sibling(alice,bob).
sibling(alice,sharon).
sibling(harriet,melissa).
sibling(melissa,harriet).
sibling(sharon,bob).
sibling(sharon,alice).
sibling(bob, alice).
sibling(bob, sharon).

%			     ken 	+	laura
%				/	  		/
%		melissa  &	harriet		+	george
%							 \	  /
%						bob 	& 	alice	& sharon


