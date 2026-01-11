parser grammar ExpressionParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;

search_condition: or_expression;

or_expression: and_expression (OR and_expression)*;

and_expression:
	predicate_expression (AND predicate_expression)*;

predicate_expression:
	LPAREN search_condition RPAREN
	| predicate;

predicate
    : add_sub_expression (OPERATOR add_sub_expression)*
    | full_column_name BETWEEN add_sub_expression AND add_sub_expression
    | full_column_name IS NULL
    | full_column_name IS NOT NULL
    | full_column_name IN LPAREN expression (COMMA expression)* RPAREN
    ;

expression: add_sub_expression;

add_sub_expression:
	mul_div_expression ((PLUS | MINUS) mul_div_expression)*;

mul_div_expression:
	primary_expression ((STAR | SLASH) primary_expression)*;

primary_expression:
	LPAREN expression RPAREN
	| full_column_name
	| LITERAL;

