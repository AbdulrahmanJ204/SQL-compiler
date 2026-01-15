parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser, OutputParser, CursorParser;


delete_statement
    : DELETE top_clause? FROM? table_source output_clause? (FROM  table_source_list)? delete_and_update_where_clause? SEMI?
    ;


