parser grammar ExpressionParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser, SelectParser;

search_condition: or_expression;

or_expression: and_expression (OR and_expression)*;

and_expression:
	not_expression (AND not_expression)*;

not_expression: predicate_expression|NOT not_expression  ;

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
comparison_predicate: expression operators (expression | quantified_subquery);
quantified_subquery
    : (ALL | ANY | SOME) LPAREN select_statement RPAREN
    ;
in_predicate:expression NOT? IN LPAREN (in_list | select_statement) RPAREN;
in_list: expression (COMMA expression)*;
between_predicate: expression NOT? BETWEEN expression AND expression ;
like_predicate: expression NOT? LIKE expression ;
null_predicate:expression IS NOT? NULL;
exists_predicate:NOT? EXISTS derived_table ;


expression: or_bitwise_expression;

or_bitwise_expression: xor_bitwise_expression (PIPE xor_bitwise_expression)*;

xor_bitwise_expression: and_bitwise_expression (CARET and_bitwise_expression)*;

and_bitwise_expression: add_sub_expression (AMPERSAND add_sub_expression)*;

add_sub_expression:
	mul_div_expression ((PLUS | MINUS) mul_div_expression)*;

mul_div_expression:
	unary_expression ((STAR | SLASH | PERCENT_OP) unary_expression)*;

unary_expression: (PLUS | MINUS)* primary_expression;

primary_expression:
	LPAREN expression RPAREN
	| case_expression
	| full_column_name
	| function_call
	| datatype
	| literal
	| NULL
	| USER_VARIABLE
	| SYSTEM_VARIABLE
	| derived_table;


case_expression
    : CASE case_body END
    ;
case_body
    : simple_case
    | searched_case
    ;
simple_case
    : expression case_when_expression+ case_else_clause?
    ;

case_when_expression
    : WHEN expression THEN expression
    ;
searched_case
    : case_when_condition+ case_else_clause?
    ;

case_when_condition
    : WHEN search_condition THEN expression
    ;
case_else_clause
    : ELSE expression
    ;
