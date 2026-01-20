parser grammar SelectParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;


select_statement
    : with_cte? query_expression order_by_clause? SEMI?;

query_expression
    : query_specification
      set_operators_list
    | LPAREN query_expression RPAREN
      set_operators_list
    ;


set_operators_list : (set_operators query_specification)*;

query_specification:
 SELECT select_modifier select_list
      (INTO full_table_name)?
      (FROM table_source_list)?
      where_clause?
      group_by_clause?
      having_clause?
    ;

select_modifier
    :
    | ALL
    | DISTINCT
    | ALL select_top_clause
    | DISTINCT select_top_clause
    | select_top_clause

    ;

select_list
     : select_list_item (COMMA select_list_item)*;

select_list_item
    : full_table_name DOT STAR
    | STAR
    | select_list_element
    ;

select_list_element
    : expression_alias
    | expression (EQ | PLUS_EQ | MINUS_EQ | STAR_EQ | SLASH_EQ | PERCENT_EQ| AMPERSAND_EQ | CARET_EQ | PIPE_EQ) expression
    ;


top_count
    : expression
    | LPAREN expression RPAREN
    ;
select_top_clause: TOP top_count PERCENT?;


