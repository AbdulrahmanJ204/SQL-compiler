parser grammar UpdateParser;
options {
	tokenVocab = SQLLexer;
}

import BasicParser;
update_statement :
UPDATE table_source SET assignment (COMMA assignment)* from_update_clause where_clause? SEMI? ;

assignment :
	target EQ source ;

target
    : column
    | table_alias DOT column
    | USER_VARIABLE
    ;
source
    : expression
    | table_alias DOT column
    ;

from_update_clause:
	FROM table_source (table_alias)? (JOIN table_source (table_alias)? ON search_condition)*;

table_alias
    : AS? IDENTIFIER
    ;
