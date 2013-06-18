%======================================%
% Background knowledgebase for sonnets %
%======================================%

% @author: Eszter Fodor
% @version 2.0: 06/2013


%==================%
% Type declaration %
%==================%

/*
prince(X1, X2):-
	rhyme(X1, X2).
*/
:- modeh(*, prince(+end, +end)).
:- modeb(1, rhyme(+end,+end)).
:- modeb(*, not_the_same_line(+end,+end)).

:- determination(prince/2, rhyme/2).
:- determination(prince/2, not_the_same_line/2).

/*
quatrain(X1, X2, X3, X4):-
	rhyme(X1, X3),
	rhyme(X2, X4).
*/
:- modeh(*, quatrain(+end, +end, +end, +end)).
:- modeb(2, rhyme(-end,-end)).
:- modeb(*, not_the_same_line(-end, -end)). 

:- determination(quatrain/4, rhyme/2).
:- determination(quatrain/4, not_the_same_line/2).

/*
sonnet(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14):-
	quatrain(X1,X2,X3,X4),
	quatrain(X5,X6,X7,X8),
	quatrain(X9,X10,X11,X12),
	prince(X13,X14).
*/
:- modeh(*, sonnet(+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end)).
:- modeb(*, quatrain(-end,-end, -end, -end)).
:- modeb(*, prince(-end, -end)).
:- modeb(*, not_the_same_line(-end, -end)).


:- determination(sonnet/14, quatrain/4).
:- determination(sonnet/14, prince/2).
:- determination(sonnet/14, not_the_same_line/2).


not_the_same_line(X, Y):-
	X \== Y.



%================%
% Knowledge base %
%================%

end(a-1).
end(b-2).
end(a-3).
end(b-4).
end(c-5).
end(d-6).
end(c-7).
end(d-8).
end(e-9).
end(f-10).
end(e-11).
end(f-12).
end(g-13).
end(g-14).

rhyme(a-1,a-3).
rhyme(b-2,b-4).
rhyme(c-5,c-7).
rhyme(d-6,d-8).
rhyme(e-9,e-11).
rhyme(f-10,f-12).
rhyme(g-13,g-14).






/*
rhyme(a-_,a-_).
rhyme(b-_,b-_).
rhyme(c-_,c-_).
rhyme(d-_,d-_).
rhyme(e-_,e-_).
rhyme(f-_,f-_).
rhyme(g-_,g-_).
*/



