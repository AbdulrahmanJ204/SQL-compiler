parser grammar InsertParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser,SelectParser,OutputParser;

insert_statement:
	INSERT
	top_clause?
	INTO?
	(full_table_name | USER_VARIABLE)
	column_list?
	output_clause?
	insert_source SEMI?;


insert_source : values_source | select_statement| default_values;

default_values : DEFAULT VALUES;

values_source: VALUES values_list (COMMA values_list)*;
values_list :LPAREN value (COMMA value)* RPAREN ;
value : expression|DEFAULT;