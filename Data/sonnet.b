%======================================%
% Background knowledgebase for sonnets %
%======================================%

% Author: Eszter Fodor
% Version 1.0: 06/2013

/* Desired clause:

sonnet(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14):-
	rhyme(X1, X3),
	rhyme(X2, X4),
	rhyme(X5, X7),
	rhyme(X6, X8),
	rhyme(X9, X11),
	rhyme(X10, X12),
	rhyme(X13, X14).

*/

%==================%
% Type declaration %
%==================%

:- modeh(*, rhyme(+ann, +ann)).
:- modeb(*, ann).

:- modeh(*, sonnet(+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann,+ann)).
:- modeb(*, rhyme(-ann,-ann)).


:- determination(sonnet/14, rhyme/2).
:- determination(rhyme/2, ann/1).


%================%
% Knowledge base %
%================%

ann(a).
ann(b).
ann(c).
ann(d).
ann(e).
ann(f).
ann(g).




