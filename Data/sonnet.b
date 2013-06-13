%======================================%
% Background knowledgebase for sonnets %
%======================================%

% @author: Eszter Fodor
% @version: 06/2013

/* Desired clauses:

prince(X1,X2):-
	X1 == X2.
	
quatrain(X1,X2,X3,X4):-
	X1 == X3,
	X2 == X4.

sonnet(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14):-
	quatrain(X1,X2,X3,X4),
	quatrain(X5,X6,X7,X8),
	quatrain(X9,X10,X11,X12),
	prince(X13,X14).

*/

%==================%
% Type declaration %
%==================%

:- modeh(*, prince(+end, +end)).
:- modeb(1, (-end) = (-end)).

:- modeh(*, quatrain(+end, +end, +end, +end)).
:- modeb(2, (-end) = (-end)).


:- modeh(*, sonnet(+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end)).
:- modeb(3, quatrain(-end,-end, -end, -end)).
:- modeb(1, prince(-end, -end)).

:- determination(sonnet/14, quatrain/4).
:- determination(quatrain/4, '='/2).
:- determination(prince/2, '='/2).


%================%
% Knowledge base %
%================%

end(a).
end(b).
end(c).
end(d).
end(e).
end(f).
end(g).




