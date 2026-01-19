parser grammar VariableParser;


options {
	tokenVocab = SQLLexer;
}


import BasicParser, CursorParser;


declare_var: DECLARE declare_var_list SEMI?;
declare_var_list:declare_var_item (COMMA declare_var_item)* ;

declare_var_item:
        scalar_var| cursor_var| table_var;

scalar_var: USER_VARIABLE AS? datatype (EQ expression)?;

cursor_var: USER_VARIABLE CURSOR;

table_var: USER_VARIABLE AS? TABLE table_type_element_list ;

set_variable: SET set_vars SEMI?;
set_vars: select_set_variable_item | set_user_eq_cursor;
set_user_eq_cursor: USER_VARIABLE EQ ( cursor_name | set_declare_cursor_item );
select_set_variable_item: USER_VARIABLE (EQ | PLUS_EQ | MINUS_EQ | STAR_EQ | SLASH_EQ | PERCENT_EQ| AMPERSAND_EQ | CARET_EQ | PIPE_EQ) expression;
