parser grammar AlterParser;

options { tokenVocab = SQLLexer; }

import BasicParser;
alter_statement
    : alter_table
    | alter_index
    | alter_view
    | alter_user
    | alter_function
    ;

alter_table
    : ALTER TABLE full_table_name table_action (COMMA table_action)* SEMI? ;

table_action
    : table_alter_column
    | table_add
    | table_rename_column ;

table_alter_column
    : ALTER COLUMN full_column_name column_type ;

table_add
    : ADD table_add_item (COMMA table_add_item)*
    ;

table_add_item
    : column_definition
    | table_constraint
    ;

table_rename_column
    : RENAME COLUMN full_column_name TO IDENTIFIER
    ;

alter_index
    : ALTER INDEX (index_name | ALL) ON full_table_name index_action SEMI?;

index_action
    : REBUILD rebuild_options?
    | REORGANIZE reorganize_options?
    | DISABLE
    | RENAME TO index_name
    ;

index_name : IDENTIFIER;

rebuild_options
    : WITH LPAREN rebuild_option (COMMA rebuild_option)* RPAREN ;

rebuild_option
    : FILLFACTOR EQ expression
    | SORT_IN_TEMPDB EQ (ON | OFF)
    | ONLINE EQ (ON | OFF)
    | MAXDOP EQ expression ;

reorganize_options
    : WITH LPAREN reorganize_option (COMMA reorganize_option)* RPAREN ;

reorganize_option
    : LOB_COMPACTION EQ (ON | OFF) ;

alter_view
    : ALTER VIEW full_table_name column_list? AS select_statement view_check_option? SEMI? ;
view_check_option
    : WITH CHECK OPTION ;

alter_user
    : ALTER USER user_name WITH user_option (COMMA user_option)* SEMI?;

user_option
    : NAME EQ IDENTIFIER
    | DEFAULT_SCHEMA EQ (IDENTIFIER | NULL)
    | LOGIN EQ IDENTIFIER
    | PASSWORD EQ LITERAL (OLD_PASSWORD EQ LITERAL)?
    | DEFAULT_LANGUAGE EQ (NONE | LITERAL | IDENTIFIER)
    | ALLOW_ENCRYPTED_VALUE_MODIFICATIONS EQ (ON | OFF);

alter_function
    : ALTER FUNCTION function_name function_parameters? returns_clause function_as function_body SEMI? ;

returns_clause
    : RETURNS return_data_type ;

function_as : AS? ;

function_body
    : BEGIN .*? RETURN expression END
    | RETURN LPAREN? select_statement RPAREN?
    ;
