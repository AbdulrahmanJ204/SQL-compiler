parser grammar UpdateParser;
options {
	tokenVocab = SQLLexer;
}

import BasicParser, OutputParser, CursorParser;

update_statement :
with_cte? UPDATE top_clause? (full_table_name| USER_VARIABLE) SET assignment_list output_clause? (FROM table_source_list)? delete_and_update_where_clause? SEMI? ;

assignment_list: assignment (COMMA assignment)*;

assignment
    : normal_assignment
    | write_assignment
    | udt_method_assignment
    ;

normal_assignment
    : target assignment_operator source
    ;

assignment_operator
    : EQ
    | PLUS_EQ
    | MINUS_EQ
    | STAR_EQ
    | SLASH_EQ
    | PERCENT_EQ
    | AMPERSAND_EQ
    | PIPE_EQ
    | CARET_EQ
    ;

write_assignment
    : full_column_name DOT WRITE
      LPAREN expression COMMA expression COMMA expression RPAREN
    ;

udt_method_assignment
    : full_column_name DOT IDENTIFIER
      LPAREN argument_list? RPAREN;

argument_list
    : expression (COMMA expression)*;

target
    : full_column_name
    | USER_VARIABLE
    ;
source
    : expression | DEFAULT
    ;




