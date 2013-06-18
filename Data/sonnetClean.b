%===============================================================%
% Background knowledge for sonnets without quatrains and prince %
%===============================================================%

/*
:- modeh(*, sonnet(+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end,+end)).
:- modeb(7, rhyme(-end, -end)).
:- modeb(*, not_the_same_line(+end, +end)).

:- determination(sonnet/14, rhyme/2).
:- determination(sonnet/14, not_the_same_line/2).
*/


not_the_same_line(X, Y):-
	X \== Y.
	

/*
rhyme(a-_,a-_).
rhyme(b-_,b-_).
rhyme(c-_,c-_).
rhyme(d-_,d-_).
rhyme(e-_,e-_).
rhyme(f-_,f-_).
rhyme(g-_,g-_).
*/



%========== AS A LIST =========%
:- modeh(*, sonnet([+end,+end,+end,+end, +end,+end,+end,+end,+end,+end,+end,+end,+end,+end])).
:- modeb(*, rhyme(-end, -end)).
%:- modeb(*, not_the_same_line(+end, +end)).

:- determination(sonnet/1, rhyme/2).
:- determination(sonnet/1, not_the_same_line/2).

rhyme(a-1,a-3).
rhyme(b-2,b-4).
rhyme(c-5,c-7).
rhyme(d-6,d-8).
rhyme(e-9,e-11).
rhyme(f-10,f-12).
rhyme(g-13,g-14).

rhyme(a-3,a-1).
rhyme(b-4,b-2).
rhyme(c-7,c-5).
rhyme(d-6,d-7).
rhyme(e-11,e-9).
rhyme(f-12,f-10).
rhyme(g-14,g-13).














