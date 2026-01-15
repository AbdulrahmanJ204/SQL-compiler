parser grammar SelectParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;

select_statement:
	SELECT select_modifier select_list (INTO full_table_name)? (FROM table_source_list where_clause? group_by_clause? having_clause? order_by_clause?)? SEMI?;

select_list
    : STAR
    | select_list_item (COMMA select_list_item)*
    ;

select_list_item
    : full_table_name DOT STAR
    | STAR
    | select_list_element
    ;

select_list_element
    : expression as_alias?
    | expression (EQ | PLUS_EQ | MINUS_EQ | STAR_EQ | SLASH_EQ | PERCENT_EQ| AMPERSAND_EQ | CARET_EQ | PIPE_EQ) expression
    ;

select_modifier: DISTINCT? select_top_clause?;

