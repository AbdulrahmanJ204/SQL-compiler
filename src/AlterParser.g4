parser grammar AlterParser;

options { tokenVocab = SQLLexer; }

import BasicParser;

alter_table_statement
    : ALTER TABLE full_table_name alter_table_action+ SEMI?
    ;

alter_table_action
    : alter_column_action
    | add_action
    ;

alter_column_action
    : ALTER COLUMN full_column_name column_type
    ;

add_action
    : ADD add_item (COMMA add_item)*
    ;

add_item
    : column_definition
    | table_constraint
    ;
