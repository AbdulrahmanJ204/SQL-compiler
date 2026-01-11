parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

where_clause: WHERE search_condition;

join_clause: join_type JOIN table_source_item join_condition;

join_condition: ON search_condition;

join_type: INNER?
    | LEFT OUTER?
    | RIGHT OUTER?
    | FULL OUTER?
    | CROSS
    ;

table_source: table_source_item join_clause*;
table_source_item
    : full_table_name as_alias?
    ;



as_alias: AS? IDENTIFIER;

full_table_name: IDENTIFIER (DOT IDENTIFIER)*;

top_clause: TOP LPAREN add_sub_expression RPAREN PERCENT?;

cursor_name: IDENTIFIER;
column: IDENTIFIER;
column_list: LPAREN column (COMMA column)* RPAREN;

full_column_name: IDENTIFIER (DOT IDENTIFIER)*;