parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
delete_statement
    : DELETE top_clause? FROM? delete_target delete_from_extension? delete_where_clause? SEMI?
    ;
  
delete_target
    : table_source ;

delete_from_extension
    : FROM  table_source (join_clause)*
    ;
  
delete_where_clause
    : WHERE search_condition
    | WHERE CURRENT OF cursor_name
    ;
