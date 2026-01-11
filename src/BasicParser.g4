parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

where_clause: WHERE search_condition;

joined_table_source: table_source (join_clause)*;

join_clause: INNER? JOIN table_source ON search_condition;

table_source: full_table_name as_alias?;

as_alias: AS? IDENTIFIER;

full_table_name: IDENTIFIER (DOT IDENTIFIER)*;