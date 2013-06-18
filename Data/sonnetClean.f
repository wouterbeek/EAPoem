%======================================%
% Positive examples for sonnets		   %
%======================================%



/*
quatrain(a_,b_,a_,b_).
quatrain(c_,d_,c_,d_).
quatrain(g_,f_,g_,f_).
*/


/*
sonnet(a_,b_,a_,b_,c_,d_,c_,d_,e_,f_,e_,f_,g_,g_).
sonnet(c_,d_,c_,d_,f_,g_,f_,g_,a_,b_,a_,b_,e_,e_).
*/

sonnet([e-9,a-1,e-11,a-3, 
	f-10,b-2,f-12,b-4, 
	g-13,c-5,g-14,c-7,
	d-6,d-8]).
	
sonnet([f-10,a-1,f-12, a-3,
	g-13,c-5,g-14,c-7,
	e-9,b-4,e-11,b-2,
	d-6,d-8]).	
	
sonnet([c-5,d-6,c-7,d-8, 
	a-1,b-2,a-3,b-4, 
	e-9,f-10,e-11,f-12, 
	g-13,g-14]).
	
sonnet([a-1,b-2,a-3,b-4, 
	c-5,d-6,c-7,d-8, 
	e-9,f-10,e-11,f-12, 
	g-14,g-13]).
	
sonnet([g-13,a-1,g-14,a-3, 
	b-2,c-5,b-4,c-7, 
	d-6,e-9,d-8,e-11, 
	f-12,f-10]).


