parser grammar CursorParser;

options {
    tokenVocab = SQLLexer;
}

import BasicParser, SelectParser;

/* =======================
   Cursor declaration
   ======================= */

declare_cursor
    : DECLARE cursor_name pre_cursor_options CURSOR cursor_definition SEMI?
    ;

/*
 * Options that appear BEFORE the CURSOR keyword
 * (only valid in syntax #2)
 */
pre_cursor_options
    : INSENSITIVE? SCROLL?
    ;

/*
 * Options that appear AFTER the CURSOR keyword
 * (syntax #1 + shared parts)
 */
cursor_definition
    : cursor_scope?
      cursor_scroll?
      cursor_type?
      cursor_concurrency?
      cursor_warning?
      cursor_for_clause
      cursor_update_clause?
    ;

/* =======================
   Cursor options
   ======================= */

cursor_scope
    : LOCAL
    | GLOBAL
    ;

cursor_scroll
    : FORWARD_ONLY
    | SCROLL
    ;

cursor_type
    : STATIC
    | KEYSET
    | DYNAMIC
    | FAST_FORWARD
    ;

/*
 * READ_ONLY is valid in BOTH syntaxes
 */
cursor_concurrency
    : READ_ONLY
    | SCROLL_LOCKS
    | OPTIMISTIC
    ;

cursor_warning
    : TYPE_WARNING
    ;

/* =======================
   Cursor query clauses
   ======================= */

cursor_for_clause
    : FOR select_statement
    ;

/*
 * UPDATE clause supports both:
 *   FOR UPDATE
 *   FOR READ_ONLY
 */
cursor_update_clause
    : (FOR READ_ONLY)
    | (FOR UPDATE cursor_update_columns?)
    ;

cursor_update_columns
    : OF full_column_name (COMMA full_column_name)*
    ;

/* =======================
   Cursor lifecycle
   ======================= */

open_cursor
    : OPEN cursor_name SEMI?
    ;

close_cursor
    : CLOSE cursor_name SEMI?
    ;

deallocate_cursor
    : DEALLOCATE cursor_name SEMI?
    ;

/* =======================
   FETCH
   ======================= */

fetch_row
    : FETCH fetch_direction? FROM cursor_name fetch_into_clause? SEMI?
    ;

fetch_direction
    : NEXT
    | PRIOR
    | FIRST
    | LAST
    | ABSOLUTE fetch_offset
    | RELATIVE fetch_offset
    ;

fetch_offset
    : literal
    | USER_VARIABLE
    ;

fetch_into_clause
    : INTO user_variable_list
    ;

/* =======================
   Identifiers
   ======================= */

cursor_name
    : GLOBAL? IDENTIFIER
    | USER_VARIABLE
    ;
