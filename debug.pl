% Debug file for the EAPoem project.

% On Windows 8 I have had the pleasure of swipl defaulting to the
% =text= encoding. This did _not_ process special characters correctly.
:- set_prolog_flag(encoding, utf8).

:- assert(user:debug).

:- [load].

