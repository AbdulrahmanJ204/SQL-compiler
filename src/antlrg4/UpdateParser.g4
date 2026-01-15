parser grammar UpdateParser;
options {
	tokenVocab = SQLLexer;
}

import BasicParser, OutputParser, CursorParser;

update_statement :
UPDATE top_clause? (full_table_name| USER_VARIABLE) SET assignment_list output_clause? (FROM table_source_list)? delete_and_update_where_clause? SEMI? ;

assignment_list: assignment (COMMA assignment)*;

assignment :
	target EQ source ;

target
    : full_column_name
    | USER_VARIABLE
    ;
source
    : expression | DEFAULT
    ;




