parser grammar CursorParser;


options {
	tokenVocab = SQLLexer;
}


import BasicParser, SelectParser;

declare_cursor: DECLARE cursor_name set_declare_cursor_item SEMI?;


set_declare_cursor_item:
    CURSOR(LOCAL|GLOBAL)?
    (FORWARD_ONLY | SCROLL)?
    ( STATIC | KEYSET | DYNAMIC | FAST_FORWARD )?
    ( READ_ONLY | SCROLL_LOCKS | OPTIMISTIC )?
    ( TYPE_WARNING )?
    FOR select_statement
    ( FOR UPDATE ( OF full_column_name (COMMA full_column_name)* )? )?;

close_cursor: CLOSE cursor_name SEMI?;

open_cursor: OPEN cursor_name SEMI?;

fetch_row: FETCH   ( (
        NEXT | PRIOR | FIRST | LAST
        | ABSOLUTE ( LITERAL | USER_VARIABLE )
        | RELATIVE ( LITERAL | USER_VARIABLE )
    )? FROM )?
    cursor_name (INTO user_variable_list*)? SEMI?;

deallocate_cursor: DEALLOCATE cursor_name SEMI?;

cursor_name: (GLOBAL? IDENTIFIER) | USER_VARIABLE;


