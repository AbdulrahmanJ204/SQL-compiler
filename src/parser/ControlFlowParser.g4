parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser, SQLParser, BasicParser;

// 30 min

control_flow_statement: while_clause|statement_block | if_clause| break_statement|continue_statement;
while_clause: WHILE search_condition (statement)* SEMI?;
if_clause: IF search_condition (statement)+ else_clause?;
else_clause: ELSE (statement)+;
break_statement: BREAK SEMI?;
continue_statement: CONTINUE SEMI?;



