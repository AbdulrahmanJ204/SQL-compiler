parser grammar SelectParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;

select_statement:
	SELECT select_list FROM table_source where_clause? SEMI?;

select_list: STAR | select_list_element (COMMA select_list_element)*;

select_list_element
    : expression as_alias?
    ;

