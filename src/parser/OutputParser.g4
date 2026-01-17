parser grammar OutputParser;

options {
	tokenVocab = SQLLexer;
}

import BasicParser;


output_clause: OUTPUT output_select_list (INTO output_into_clause)?;

output_select_list: output_select_list_item (COMMA output_select_list_item)*;
output_select_list_item: expression | ((IDENTIFIER|INSERTED|DELETED) DOT STAR as_alias?) ;

output_into_clause
    : USER_VARIABLE | full_table_name column_list?
    ;

