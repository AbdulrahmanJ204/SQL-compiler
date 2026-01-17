parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser, SQLParser, BasicParser;


control_flow_statement: while_clause|statement_block | if_clause| break_statement|continue_statement;
while_clause: WHILE search_condition (statement)* SEMI?;
if_clause: IF search_condition (statement)+ (ELSE (statement)+ )?;
break_statement: BREAK SEMI?;
continue_statement: CONTINUE SEMI?;