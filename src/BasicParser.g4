parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser;

where_clause: WHERE search_condition;

join_clause: join_type JOIN table_source_item join_condition;

having_clause: HAVING search_condition;

group_by_clause: GROUP BY group_by_item_list (WITH ROLLUP | WITH CUBE)?;

group_by_item_list: expression (expression)*;

order_by_clause: ORDER BY order_by_list order_by_offset?;

order_by_offset: OFFSET expression ROWS (FETCH NEXT expression ROWS ONLY)?;

order_by_list: order_by_item (COMMA order_by_item)*;

order_by_item: expression (DESC|ASC)?;

join_condition: ON search_condition;

join_type: INNER?
    | LEFT OUTER?
    | RIGHT OUTER?
    | FULL OUTER?
    | CROSS
    ;

table_source: table_source_item join_clause*;
table_source_item
    : (full_table_name  | derived_table) as_alias?
    ;

derived_table
    : LPAREN select_statement RPAREN
    ;

as_alias: AS? IDENTIFIER;

full_table_name: IDENTIFIER (DOT IDENTIFIER)*;

top_clause: TOP LPAREN expression RPAREN PERCENT?;
top_count
    : expression
    | LPAREN expression RPAREN
    ;
select_top_clause: TOP top_count PERCENT?;

cursor_name: IDENTIFIER;
full_column_name: IDENTIFIER (DOT IDENTIFIER)*;
column_list: LPAREN full_column_name (COMMA full_column_name)* RPAREN;
operators: EQ | NEQ | LTE | GTE | LT | GT;

function_call
    : IDENTIFIER LPAREN function_arguments? RPAREN
    ;

function_arguments
    : STAR
    | expression (COMMA expression)*
    ;

column_type
    : type_name type_length? nullability?;

type_name
    : full_table_name;

type_length
    : LPAREN expression (COMMA expression)? RPAREN ;

nullability
    : NULL
    | NOT NULL
    ;

column_definition
    : full_column_name column_type ;

table_constraint
    : CONSTRAINT IDENTIFIER? constraint_body | constraint_body ;

constraint_body
    : pk_or_unique_constraint
    | foreign_key_constraint
    | check_constraint
    ;

pk_or_unique_constraint
    : (PRIMARY KEY | UNIQUE)
      LPAREN full_column_name (COMMA full_column_name)* RPAREN  ;

foreign_key_constraint
    : FOREIGN KEY
      LPAREN full_column_name (COMMA full_column_name)* RPAREN
      REFERENCES full_table_name
      LPAREN full_column_name (COMMA full_column_name)* RPAREN   ;

check_constraint
    : CHECK LPAREN search_condition RPAREN ;
