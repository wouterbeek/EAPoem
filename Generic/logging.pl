:- module(
  logging,
  [
    append_to_log/1, % +Format:atom
    append_to_log/2, % +Format:atom
                     % +Arguments:list(term)
    append_to_log/3, % +Category:atom
                     % +Format:atom
                     % +Arguments:list(term)
    close_log_stream/1, % +Stream:atom
    create_log_file/2, % -File:atom
                       % -Stream:atom
    create_log_file/3, % +Situation:atom
                       % -File:atom
                       % -Stream:atom
    current_log_file/1, % ?File:file
    current_log_stream/1, % ?Stream:stream
    disable_log_mode/0,
    enable_log_mode/0,
    end_log/0,
    send_log/1, % +File:atom
    set_current_log_file/1, % ?File:atom
    set_current_log_stream/1, % ?Stream:stream
    set_situation/1,
    start_log/0
  ]
).

/** <module> Logging

Methods for logging.

@author Wouter Beek
@author Sander Latour
@version 2012/05-2012/07, 2013/03
*/

:- use_module(generic(file_ext)).
:- use_module(library(http/http_client)).

:- multifile(prolog:message/1).

:- dynamic(log_mode/1).
:- dynamic(situation/1).

:- dynamic(current_log_file/1).
:- dynamic(current_log_stream/1).

:- assert(user:prolog_file_type(log, log)).



%% append_to_log(+Format:atom) is det.
% Logs the given message in the current log file.
%
% @param Format An atomic message.
% @see Like format/1.

append_to_log(Format):-
  append_to_log(Format, []).

%% append_to_log(+Format:atom, +Arguments:list(term)) is det.
% Logs the given message in the current log file.
%
% @param Format An atomic message.
% @param Arguments A list of terms.
% @see Like format/2.

append_to_log(Format, Arguments):-
  append_to_log(generic, Format, Arguments).

%% append_to_log(+Category:atom, +Format:atom, +Arguments:list(term)) is det.
% Logs the given message in the current log file under the given category.
%
% @param Category An atom.
% @param Format An atomic message.
% @param Arguments A list of terms.

append_to_log(Category, Format, Arguments):-
  format(atom(Message), Format, Arguments),
  append_to_log_(Category, Message).

append_to_log_(_Category, _Message):-
  log_mode(fail),
  !.
append_to_log_(Category, Message):-
  current_log_stream(Stream),
  !,
  date_time(DateTime),
  situation(Situation),
  csv_write_stream(
    Stream,
    [row(Situation, DateTime, Category, Message)],
    [file_type(comma_separated_values)]
  ),
  flush_output(Stream).
append_to_log_(Kind, Message):-
  print_message(error, cannot_log(Kind, Message)).
prolog:message(cannot_log(Kind, Message)):-
  [
    ansi([bold], '[~w] ', [Kind]),
    ansi([], 'Could not log message "', []),
    ansi([faint], '~w', [Message]),
    ansi([], '".', [])
  ].

%% close_log_stream(+Stream) is det.
% Closes the given log stream.
%
% @param Stream A stream.

close_log_stream(Stream):-
  flush_output(Stream),
  close(Stream).

%% create_log_file(-File:atom, -Stream) is det.
% Creates a log file in the log file directory and returns the absolute
% path of that file as well as its stream name.
%
% @param File The atomic name of a file's path.
% @param Stream The atomic name of a file's stream.

create_log_file(File, Stream):-
  situation(Situation),
  create_log_file(Situation, File, Stream).

%% create_log_file(+Situation:atom, -File:atom, -Stream:atom) is det.
% Creates a log file in the log file directory and returns the absolute
% path of that file as well as its stream.
%
% @param Situation An atomic descriptor of a logging situation.
% @param File The atomic name of a file's path.
% @param Stream The atomic name of a file's stream.

create_log_file(Situation, AbsoluteFile, Stream):-
  absolute_file_name(log(Situation), Dir),
  date_directories(Dir, LogDir),
  current_time(FileName),
  create_file(LogDir, FileName, log, AbsoluteFile),
  open(AbsoluteFile, write, Stream, [close_on_abort(true), type(text)]).

disable_log_mode:-
  log_mode(false),
  !.
disable_log_mode:-
  (log_mode(true) -> retract(log_mode(true)) ; true),
  assert(log_mode(false)).

enable_log_mode:-
  log_mode(true),
  !.
enable_log_mode:-
  (log_mode(false) -> retract(log_mode(false)) ; true),
  assert(log_mode(true)).

%% end_log is det.
% Ends the current logging activity.

end_log:-
  log_mode(fail),
  !.
end_log:-
  append_to_log(build, 'Goodnight!', []),
  current_log_file(File),
  (
    send_log(File)
  ;
    true
  ),
  current_log_stream(Stream),
  close_log_stream(Stream).

%% send_log(File) is det.
% Sends the log that is stored in the given file to the logging server.
%
% @param File The atomic name of a file.

send_log(File):-
  open(File, read, Stream, []),
  read_stream_to_codes(Stream, Codes),
  file_base_name(File, Base),
  format(atom(URL), 'http://www.wouterbeek.com/post.php?filename=~w', [Base]),
  catch(http_post(URL, codes('text/xml;charset=utf-8', Codes), Reply, []), _Error, fail),
  send(@pce, write_ln, Reply).

%% set_current_log_file(+File:atom) is det.
% Sets the current file where logging messages are stored to.
%
% @param File The atomic name of a file.

set_current_log_file(File):-
  retractall(current_log_file(_File)),
  assert(current_log_file(File)).

%% set_current_log_stream(+Stream) is det.
% Sets the current stream where logging messages are written to.
%
% @param Stream A stream.

set_current_log_stream(Stream):-
  retractall(current_log_stream(_Stream)),
  assert(current_log_stream(Stream)).

% Already set.
set_situation(Situation):-
  situation(Situation),
  !,
  fail.
% Set for the first (any only) time.
set_situation(Situation):-
  assert(situation(Situation)).

%% start_log is det.
% Starts logging.
% This does nothing in case log mode is turned off.

start_log:-
  log_mode(fail),
  !.
start_log:-
  create_log_file(File, Stream),
  set_current_log_file(File),
  set_current_log_stream(Stream),
  append_to_log(build, 'Goodday!', []).

