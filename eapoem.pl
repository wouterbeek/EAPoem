:- module(
  eapoem,
  [
  ]
).

/** <module> EAPoem

Edgar Allan Poem

@author Eszter Fodor, Wouter Beek
@version 2013/05
*/

:- use_module(generics(db_ext)).
:- use_module(library(csv)).
:- use_module(library(double_metaphone)).
:- use_module(project(poem)).
:- use_module(server(wallace)).

:- db_add_novel(user:prolog_file_type(csv, csv)).



test:-
  absolute_file_name(
    project(shakespeare),
    File,
    [access(read), file_type(csv)]
  ),
  csv_read_file(File, Rows, [match_arity(false)]),
  flag(csv_row, _OldID, 1),
  forall(
    member(Row, Rows),
    (
      flag(csv_row, ID, ID + 1),
      format(user_output, '~w: ~w\n', [ID, Row])
    )
  ),
  Sentence = 'Double metafone in werking.',
  double_metaphone(Sentence, Phones),
  format(user_output, 'Sentence:\t~w\nPhones:\t~w\n', [Sentence, Phones]).
:- test.

