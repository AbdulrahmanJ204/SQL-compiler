parser grammar SQLParser;

options {
	tokenVocab = SQLLexer;
}

tsql_file: statement* EOF;

statement: select_statement;

//! ╔══════════════════════════════════════════╗
//! ║━━━━━━━━━━━━<SELECT STATEMENT>━━━━━━━━━━━━║
//! ╚══════════════════════════════════════════╝
select_statement:
	SELECT select_list FROM table_source where_clause? SEMI?;

select_list: STAR | column (COMMA column)*;

table_source: IDENTIFIER;

column: IDENTIFIER;

where_clause: WHERE search_condition;

search_condition: or_expression;

or_expression: or_expression OR or_expression | and_expression;

and_expression:
	and_expression AND and_expression
	| paren_expression;

paren_expression: LPAREN search_condition RPAREN | predicate;

predicate: add_sub_expression OPERATOR add_sub_expression;

add_sub_expression: add_sub_expression (PLUS | MINUS) add_sub_expression | mul_div_expression;

mul_div_expression: mul_div_expression (STAR | SLASH) mul_div_expression | arth_paren_expression;
arth_paren_expression: LPAREN add_sub_expression RPAREN | expression;

expression: (IDENTIFIER | LITERAL);