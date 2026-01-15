parser grammar DropParser;
options {
	tokenVocab = SQLLexer;
}

import BasicParser;
drop_statement
    : DROP drop_object SEMI?
    ;

drop_object
    : drop_table
    | drop_view
    | drop_user
    | drop_index
    ;

drop_table
    : TABLE if_exists? full_table_name
    ;

drop_view
    : VIEW if_exists? view_name_list
    ;

drop_user
    : USER if_exists? user_name
    ;
drop_index
    : INDEX if_exists? index_name ON full_table_name
    ;

if_exists
    : IF EXISTS
    ;

view_name_list
    : full_table_name (COMMA full_table_name)*
    ;

