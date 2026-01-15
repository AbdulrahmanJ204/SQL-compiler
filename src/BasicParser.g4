parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser, SQLParser;

where_clause: WHERE search_condition;

join_clause: join_type JOIN table_source_item join_condition;

having_clause: HAVING search_condition;

group_by_clause: GROUP BY group_by_item_list (WITH ROLLUP | WITH CUBE)?;

group_by_item_list: expression (COMMA expression)*;

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
table_source_list: table_source (COMMA table_source)*;
table_source_item
    : (full_table_name  | derived_table | USER_VARIABLE) as_alias?
    ;

derived_table
    : LPAREN select_statement RPAREN
    ;

as_alias: AS? IDENTIFIER;

full_table_name: IDENTIFIER (DOT IDENTIFIER)*;

top_clause: TOP LPAREN expression RPAREN PERCENT?;

set_operators: (UNION ALL?) | EXCEPT | INTERSECT;

top_count
    : expression
    | LPAREN expression RPAREN
    ;
select_top_clause: TOP top_count PERCENT?;

full_column_name: (IDENTIFIER | DELETED | INSERTED) (DOT IDENTIFIER)*;
column_list: LPAREN full_column_name (COMMA full_column_name)* RPAREN;

user_variable_list: USER_VARIABLE (COMMA USER_VARIABLE)*;

operators: EQ | NEQ | LTE | GTE | LT | GT ;

column_type
    : datatype nullability?;

datatype
    : full_table_name
    | INT
    | BIGINT
    | SMALLINT
    | TINYINT
    | decimal_data_type
    | numeric_data_type
    | FLOAT
    | REAL
    | BIT
    | char_data_type
    | nchar_data_type
    | varchar_data_type
    | nvarchar_data_type
    | TEXT
    | NTEXT
    | DATE
    | DATETIME
    | time_data_type
    | binary_data_type
    | varbinary_data_type
    ;

decimal_data_type: DECIMAL (LPAREN LITERAL (COMMA LITERAL)? RPAREN)?;
numeric_data_type: NUMERIC (LPAREN LITERAL (COMMA LITERAL)? RPAREN)? ;
char_data_type:CHAR (LPAREN LITERAL RPAREN)?;
nchar_data_type:NCHAR (LPAREN LITERAL RPAREN)?;
binary_data_type:BINARY (LPAREN LITERAL RPAREN)?;
varchar_data_type:NVARCHAR (LPAREN (LITERAL|MAX) RPAREN)?;
nvarchar_data_type:VARCHAR (LPAREN (LITERAL|MAX) RPAREN)?;
varbinary_data_type:VARBINARY (LPAREN (LITERAL|MAX) RPAREN)?;
time_data_type:TIME|DATETIME2|DATETIMEOFFSET (LPAREN LITERAL RPAREN)?;

function_call
    : (IDENTIFIER DOT)? (IDENTIFIER|MAX) LPAREN function_arguments? RPAREN
    ;

function_arguments
    : STAR
    | expression (COMMA expression)*
    ;


nullability
    : NULL
    | NOT NULL
    ;

column_definition
    : full_column_name column_type column_constraint* ;


column_constraint
    : PRIMARY KEY
    | UNIQUE
    | NOT NULL
    | NULL
    | DEFAULT LITERAL
    | IDENTITY
    ;

table_constraint
    : CONSTRAINT IDENTIFIER? constraint_body ;

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
user_name : IDENTIFIER  ;

function_name : full_table_name  ;

function_parameters
    : LPAREN function_parameter_list? RPAREN  ;

function_parameter_list
    : function_parameter (COMMA function_parameter)*;

function_parameter
    : USER_VARIABLE AS?  datatype  (NULL | NOT NULL)? (EQ default_value)? (READONLY)?;

default_value
    : LITERAL
    | NULL
    ;

return_data_type
    : column_type | TABLE;

index_name : IDENTIFIER;


view_attribute
    : ENCRYPTION
    | SCHEMABINDING
    | VIEW_METADATA
    ;

view_check_option : WITH CHECK OPTION ;