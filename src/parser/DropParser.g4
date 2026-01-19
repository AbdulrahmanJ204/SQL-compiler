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

view_name_list
    : full_table_name (COMMA full_table_name)*;

drop_user
    : USER if_exists? user_name
    ;
drop_index
    : INDEX drop_index_item (COMMA drop_index_item)*;

drop_index_item
    : if_exists? index_name ON full_table_name drop_index_with_clause?;

if_exists: IF EXISTS;

drop_index_with_clause
    : WITH LPAREN drop_index_option (COMMA drop_index_option)* RPAREN;

drop_index_option
    : MAXDOP EQ expression
    | ONLINE EQ (ON | OFF)
    | MOVE TO drop_move_target
    | FILESTREAM_ON drop_filestream_target
    ;

drop_move_target
    : partition_target
    | IDENTIFIER
    ;
drop_filestream_target
    : partition_target
    | IDENTIFIER
    ;



