parser grammar expressionParser;

options {
	tokenVocab = SQLLexer;
}

search_condition: or_expression;

or_expression: and_expression (OR and_expression)*;

and_expression: paren_expression (AND paren_expression)*;

paren_expression: LPAREN search_condition RPAREN | predicate;

predicate: add_sub_expression (OPERATOR add_sub_expression)*;

add_sub_expression:
	mul_div_expression ((PLUS | MINUS) mul_div_expression)*;

mul_div_expression:
	arth_paren_expression ((STAR | SLASH) arth_paren_expression)*;
arth_paren_expression:
	LPAREN add_sub_expression RPAREN
	| expression;

expression: (qualified_name | LITERAL);
 
qualified_name
    : IDENTIFIER (DOT IDENTIFIER)*
    ;
 
