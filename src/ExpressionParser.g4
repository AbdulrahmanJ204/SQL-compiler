parser grammar ExpressionParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
import SelectParser;

search_condition: or_expression;

or_expression: and_expression (OR and_expression)*;

and_expression:
	predicate_expression (AND predicate_expression)*;

predicate_expression:
	LPAREN search_condition RPAREN
	| predicate;

predicate
    : comparison_predicate
    | in_predicate
    | between_predicate
    | like_predicate
    | null_predicate
    | exists_predicate
    ;
comparison_predicate: expression (operators expression)*;
in_predicate:expression NOT? IN LPAREN in_list RPAREN;
in_list: expression (COMMA expression)*;
between_predicate: expression NOT? BETWEEN expression AND expression ;
like_predicate: expression NOT? LIKE expression ;
null_predicate:expression IS NOT? NULL;
exists_predicate:NOT? EXISTS derived_table ;

expression: add_sub_expression;

add_sub_expression:
	mul_div_expression ((PLUS | MINUS) mul_div_expression)*;

mul_div_expression:
	primary_expression ((STAR | SLASH) primary_expression)*;

primary_expression:
	LPAREN expression RPAREN
	| full_column_name
	| function_call
	| LITERAL| NULL| USER_VARIABLE|derived_table;

