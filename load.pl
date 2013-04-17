% The load file for the EAPoem project.

% Module for documentation server.
:- use_module(library(doc_http)).
% Module for debug monitor.
:- use_module(library(swi_ide)).



load:-
  source_file(load, ThisFile),
  file_directory_name(ThisFile, ThisDirectory),
  assert(user:file_search_path(project, ThisDirectory)),
  
  % This project uses the PGC library.
  assert(user:file_search_path(generic, project('PrologGenericsCollection'))),
  
  % Use the swipl debug monitor for viewing debug messages.
  prolog_ide(debug_monitor),

  % Start the plDoc documentation server.
  doc_server(2222, [edit(true)]),

  use_module(project(aleph6)).

:- load.
