parser grammar basicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

table_source
    : object_name
    ;

column
    : object_name
    ;

where_clause: WHERE search_condition;
 
object_name
    : IDENTIFIER (DOT IDENTIFIER)*
    ;
 
table_with_alias: table_source (AS? IDENTIFIER)?;

joined_table_source: table_with_alias (join_clause)*;

join_clause: INNER? JOIN table_with_alias ON search_condition;
 






 
