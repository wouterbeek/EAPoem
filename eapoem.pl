:- module(
  eapoem,
  [
  	xmlTest/1,
  	shakespeare_csv/0,
    test_double_metaphone/0
  ]
).

/** <module> EAPoem

Edgar Allan Poem

@author Eszter Fodor
@author Wouter Beek
@version 2013/05
*/

:- use_module(dbnl(dbnl)).
:- use_module(generics(db_ext)).
:- use_module(library(csv)).
:- use_module(library(double_metaphone)).
:- use_module(server(wallace)).
:- use_module(library(xpath)).
:- use_module(library(sgml)).
:- use_module(ilp(aleph6)).

:- db_add_novel(user:prolog_file_type(csv, csv)).
:- db_add_novel(user:prolog_file_type(xml, xml)).


xmlTest(Cats):-
	absolute_file_name(sonnet(sonnet1ann), File, [access(read), file_type(xml)]),
	load_structure(File, DOM, []),
	findall(Cat, xpath(DOM, //phoneme(@category), Cat), Cats).
	


shakespeare_csv:-
  absolute_file_name(project(shakespeare), File, [access(read), file_type(csv)]),
  csv_read_file(File, Rows, [match_arity(false)]),
  flag(csv_row, _OldID, 1),
  forall(
    member(Row, Rows),
    (
      flag(csv_row, ID, ID + 1),
      format(user_output, '~w: ~w\n', [ID, Row])
    )
  ).

% Double metaphone.
test_double_metaphone:-
  Word = 'voorbeeld',
  double_metaphone(Word, Phones),
  format(user_output, 'Word:\t~w\nPhones:\t~w\n', [Word, Phones]).

