parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser, OutputParser, CursorParser;


delete_statement
    : DELETE top_clause? FROM? table_source output_clause? (FROM  table_source_list)? delete_where_clause? SEMI?
    ;

  
delete_where_clause
    : WHERE (search_condition | CURRENT OF cursor_name)
    ;

