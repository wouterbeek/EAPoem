project_name('EAPoem').

load_eapoem:-
  source_file(load_eapoem, ThisFile),
  file_directory_name(ThisFile, ThisDirectory),
  assert(user:file_search_path(project, ThisDirectory)),
  
  assert(user:file_search_path(data, project('Data'))),
  assert(user:file_search_path(sonnet, data('SonnetsRhymeAnnotated'))),
  assert(user:file_search_path(train, sonnet('Train'))),
  assert(user:file_search_path(test, sonnet('Test'))),
  
  % Load the PGC.
  assert(user:file_search_path(pgc, project('PGC'))),
  (
    predicate_property(debug, visible)
  ->
    ensure_loaded(pgc(debug))
  ;
    ensure_loaded(pgc(load))
  ),
  
  % EAPoem main module.
  ensure_loaded(project(eapoem)).
:- load_eapoem.

