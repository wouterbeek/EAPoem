:- module(
  eapoem,
  [
  	read_poem/1,
  	shakespeare_csv/0,
    test_double_metaphone/0,
    create_metaphone_file/0
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


%! read_poem(+Poem: atom, -Cats: list) is det.
% Reads the poem (xml) and returns the rhyme annotation list
read_poem(Cats):-
	absolute_file_name(train(.), Directory, [access(read), file_type(directory)]),
    directory_files(Directory, LocalNames),
	findall(
		Cat,
		(
		    member(LocalName, LocalNames),
		    (
			    catch(absolute_file_name(train(LocalName), File, [access(read), file_type(xml)]), _, fail)
		    ->
				load_structure(File, DOM, []),
				xpath(DOM, //phoneme(@category), Cat)
			;
				true
			)
		),
		Cats
	).
	


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
  
  
% ======================================================= %
  
create_metaphone_file:-
	open('words_unique.txt', read, Stream),
	read_file(Stream, WordList),
	test(WordList), 
	close(Stream).

% TODO: stream moet pas na het schrijven van alle regels gesloten worden	
test([H|T]):-
	open('output.txt', write, StreamOut),
	double_metaphone(H, Meta),
	write(StreamOut, Meta),
	nl(StreamOut),
	close(StreamOut),
	test(T).	


read_file(Stream,[]) :-
    at_end_of_stream(Stream).
    
read_file(Stream,[X|L]) :-
    \+ at_end_of_stream(Stream),
    read(Stream,X),
    read_file(Stream,L).	

	

