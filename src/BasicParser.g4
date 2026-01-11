parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

where_clause: WHERE search_condition;

join_clause: INNER? JOIN table_source ON search_condition;

table_source: full_table_name as_alias?;

as_alias: AS? IDENTIFIER;

full_table_name: IDENTIFIER (DOT IDENTIFIER)*;

top_clause: TOP LPAREN add_sub_expression RPAREN PERCENT?;

cursor_name: IDENTIFIER;
column: IDENTIFIER;
column_list: LPAREN column (COMMA column)* RPAREN;

full_column_name: IDENTIFIER (DOT IDENTIFIER)*;