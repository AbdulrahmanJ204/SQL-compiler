parser grammar DeleteParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;
delete_statement
    : DELETE top_clause? FROM? delete_target delete_from_extension? where_clause? SEMI?
    ;

top_clause
    : TOP LPAREN add_sub_expression RPAREN PERCENT?
    ;
  
delete_target
    : table_source (AS? IDENTIFIER)?
    | IDENTIFIER
    ;

delete_from_extension
    : FROM joined_table_source
    ;
