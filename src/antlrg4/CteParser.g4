parser grammar CteParser;


options {
	tokenVocab = SQLLexer;
}


import BasicParser, SelectParser;

with_cte:WITH common_table_expression_list;

common_table_expression_list: common_table_expression (COMMA common_table_expression)*;

common_table_expression: IDENTIFIER column_list? AS LPAREN cte_query_definition_list RPAREN;

cte_query_definition_list: select_statement (set_operators select_statement)*;