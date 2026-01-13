parser grammar CreateParser;

options { tokenVocab = SQLLexer; }

import BasicParser;

create_statement
    : create_table
    | create_index
    | create_view
    | create_user
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

create_index
    : CREATE UNIQUE? index_clustering? INDEX index_name
      ON full_table_name index_column_list
      include_clause?
      where_clause_for_index?
      index_with_clause?
      SEMI?
    ;

index_clustering
    : CLUSTERED
    | NONCLUSTERED
    ;

index_column_list
    : LPAREN index_column (COMMA index_column)* RPAREN;

index_column
    : full_column_name (ASC | DESC)?;

include_clause
    : INCLUDE LPAREN full_column_name (COMMA full_column_name)* RPAREN;

where_clause_for_index
    : WHERE search_condition;
index_with_clause
    : WITH LPAREN index_option (COMMA index_option)* RPAREN;

index_option
    : PAD_INDEX EQ (ON | OFF)
    | FILLFACTOR EQ expression
    | IGNORE_DUP_KEY EQ (ON | OFF)
    | ALLOW_ROW_LOCKS EQ (ON | OFF)
    | ALLOW_PAGE_LOCKS EQ (ON | OFF)
    ;


create_view
    : CREATE VIEW full_table_name view_column_list?
      view_with_attributes?
      AS select_statement view_check_option? SEMI?
    ;

view_column_list
    : LPAREN IDENTIFIER (COMMA IDENTIFIER)* RPAREN;

view_with_attributes
    : WITH view_attribute (COMMA view_attribute)*;



create_user
    : CREATE USER user_name create_user_core SEMI?;

create_user_core
    : (FOR | FROM)? LOGIN login_name with_user_options?
    | WITH PASSWORD EQ LITERAL (COMMA create_user_option)*
    | WITHOUT LOGIN with_user_options?
    ;

with_user_options
    : WITH create_user_option (COMMA create_user_option)*;

create_user_option
    : DEFAULT_SCHEMA EQ full_table_name
    | DEFAULT_LANGUAGE EQ default_language_value
    | SID EQ sid_value
    ;

default_language_value
    : NONE
    | LITERAL
    | IDENTIFIER
    ;

login_name: IDENTIFIER;

sid_value
    : LITERAL
    | IDENTIFIER
    ;