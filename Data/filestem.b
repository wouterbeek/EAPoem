:- mode(1,mem(+number,+list)).
:- mode(1,dec(+integer,-integer)).
:- mode(1,mult(+integer,+integer,-integer)).
:- mode(1,plus(+integer,+integer,-integer)).
:- mode(1,(+integer)=(#integer)).
:- mode(*,has_car(+train,-car)).
:- determination(eastbound/1,has_car/2).
:- determination(mult/3,mult/3).
:- determination(p/1,'='/2).
