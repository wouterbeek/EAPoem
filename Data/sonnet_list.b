%==============================================%
% Background knowledge for sonnets using Lists %
%==============================================%

% @author: Eszter Fodor
% @version 2.2: 06/2013

%==================%
% Type declaration %
%==================%

:- modeh(*, prince([+end, +end])).
:- modeb(1, rhyme(+end,+end)).
:- determination(prince/1, rhyme/2).

:- modeh(*, quatrain([+end, +end, +end, +end])).
:- modeb(2, rhyme(-end, -end)).
:- determination(quatrain/1,rhyme/2).

:- modeh(*, sonnet([+end,+end,+end,+end, +end,+end,+end,+end,+end,+end,+end,+end,+end,+end])).
:- modeb(*, quatrain([-end,-end,-end,-end])).
:- modeb(*, prince([-end, -end])).
:- determination(sonnet/1,quatrain/1).
:- determination(sonnet/1,prince/1).







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

