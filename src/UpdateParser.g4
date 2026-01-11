parser grammar UpdateParser;
options {
	tokenVocab = SQLLexer;
}

import BasicParser;
update_statement :
UPDATE table_source SET assignment (COMMA assignment)* from_update_clause? where_clause? SEMI? ;

assignment :
	target OPERATOR source ;

target
    : column
    | as_alias DOT column
    | USER_VARIABLE
    ;
source
    : expression
    | as_alias DOT column
    ;

from_update_clause:
	FROM table_source (as_alias)? (JOIN table_source (as_alias)? ON search_condition)*;


