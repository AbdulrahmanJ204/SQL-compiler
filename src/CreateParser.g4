parser grammar CreateParser;

options { tokenVocab = SQLLexer; }

import BasicParser;

create_statement
    : create_table
    ;

create_table
    : CREATE TABLE full_table_name create_table_body SEMI?
    ;

create_table_body
    : LPAREN create_table_element_list RPAREN
    ;

create_table_element_list
    : create_table_element (COMMA create_table_element)*
    ;

create_table_element
    : column_definition
    | table_constraint
    ;
