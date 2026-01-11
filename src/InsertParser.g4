parser grammar InsertParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
import SelectParser;

insert_statement:
	INSERT 
	top_clause?
	INTO?
	table_source 
	column_list?
	insert_source SEMI?;


insert_source : values_source | select_statement| default_values;

default_values : DEFAULT VALUES;

values_source: VALUES values_list (COMMA values_list)*;
values_list :LPAREN value (COMMA value)* RPAREN ;
value : LITERAL |IDENTIFIER | NULL;