parser grammar BasicParser;

options {
	tokenVocab = SQLLexer;
}

import ExpressionParser, SQLParser,CreateParser;

where_clause: WHERE search_condition;
delete_and_update_where_clause
    : where_clause | (WHERE CURRENT OF cursor_name)
    ;

join_clause: join_type JOIN table_source_item join_condition?;

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

table_source_list: table_source (COMMA table_source)*;
table_source: table_source_item join_clause* |function_call;
table_source_item
    : (full_table_name  | derived_table | USER_VARIABLE) as_alias?
    ;

derived_table
    : LPAREN select_statement RPAREN
    ;

as_alias: AS? expression;

full_table_name: IDENTIFIER (DOT IDENTIFIER)*;

top_clause: TOP LPAREN expression RPAREN PERCENT?;

set_operators: (UNION ALL?) | EXCEPT | INTERSECT;



full_column_name: (IDENTIFIER | DELETED | INSERTED) (DOT IDENTIFIER)*;
column_list: LPAREN full_column_name (COMMA full_column_name)* RPAREN;

user_variable_list: USER_VARIABLE (COMMA USER_VARIABLE)*;

operators: EQ | NEQ | LTE | GTE | LT | GT ;


column_type
    : datatype SPARSE? nullability_clause;

nullability_clause
    :NOT NULL
    |
    NULL?
    ;

datatype
    : single_word_data_type
    | decimal_numeric_data_type
    | char_nchar_binary_data_type
    | varchar_nvarchar_varbinary_data_type
    | time_data_type
    ;

single_word_data_type: INT
    | BIGINT
    | SMALLINT
    | TINYINT
    | UNIQUEIDENTIFIER
    | MONEY
    | FLOAT
    | REAL
    | BIT
    | TEXT
    | NTEXT
    | DATE
    | DATETIME
    | XML;

decimal_numeric_data_type:( DECIMAL|NUMERIC) literal_pair?;

char_nchar_binary_data_type:(CHAR |NCHAR |BINARY) paren_literal?;


varchar_nvarchar_varbinary_data_type: (VARCHAR| NVARCHAR  |VARBINARY) paren_literal_max?;


// TODO : Impelement This
time_data_type: (TIME| DATETIME2 | DATETIMEOFFSET ) paren_literal?;


literal_pair : LPAREN literal (COMMA literal)? RPAREN;
paren_literal:LPAREN literal RPAREN;
paren_literal_max: LPAREN (literal|MAX) RPAREN;



function_call
    : (IDENTIFIER DOT)? (IDENTIFIER|MAX|DEFAULT) LPAREN function_arguments? RPAREN
    ;

function_arguments
    : STAR
    | expression_alias_list
    ;

expression_alias_list: expression_alias (COMMA expression_alias)*;
expression_alias: expression as_alias?;
// CONFIRMED



column_definition
    : default_column_definition
    | computed_column_definition
    | column_as
    ;

column_constraint_list: column_constraint*;

column_as : full_column_name as_alias;
computed_column_definition
    : full_column_name AS expression PERSISTED?
    ;

column_constraint
    : (CONSTRAINT IDENTIFIER)? column_constraint_body
    ;
column_constraint_body
    : default_col_constraint
    | pk_col_constraint
    | unique_col_constraint
    | single_word_constrain
    | identity_col_constraint
    | col_foreign_key_constraint
    | check_constraint
    ;
single_word_constrain:
     NOT NULL
    | NULL
    | ROWGUIDCOL
    ;


pk_col_constraint: PRIMARY KEY; // clusterd by default
unique_col_constraint: UNIQUE ;

identity_col_constraint: IDENTITY (LPAREN NUMBER_LITERAL COMMA NUMBER_LITERAL RPAREN)?;
check_constraint
    : CHECK LPAREN search_condition RPAREN ;

col_foreign_key_constraint: (FOREIGN KEY)? REFERENCES full_table_name column_list;

default_col_constraint
    : DEFAULT default_value_expr with_values_clause?;

with_values_clause: WITH VALUES;

default_value_expr
    : literal
    | niladic_function
    | (function_call | LPAREN function_call RPAREN)
    ;

niladic_function
    : USER
    | SYSTEM_USER
    | CURRENT_USER
    ;


table_constraint
    : (CONSTRAINT IDENTIFIER)? table_constraint_body
    ;

// no override
table_constraint_body
    : pk_table_constraint
    | unique_table_constraint
    | fk_table_constraint
    | check_constraint
    | default_table_constraint
    ;

pk_table_constraint
    : PRIMARY KEY (CLUSTERED | NONCLUSTERED)?
      index_column_list
      index_with_clause?
    ;

unique_table_constraint
    : UNIQUE (CLUSTERED | NONCLUSTERED)?
      index_column_list
      index_with_clause?
    ;


fk_table_constraint
    : FOREIGN KEY
      column_list
      REFERENCES full_table_name
      column_list
    ;


default_table_constraint
    : DEFAULT default_value_expr FOR full_column_name;

user_name : IDENTIFIER  ;


table_type_definition
    :TABLE table_type_element_list;
table_type_element_list:LPAREN table_type_element (COMMA table_type_element)* RPAREN;

table_type_element
    : column_definition
    | table_constraint
    ;

go_statement: ((USE IDENTIFIER )| GO) SEMI?;

statement_block: BEGIN SEMI? (statement)+ END SEMI?;

print_clause: PRINT expression SEMI?;

literal: NUMBER_LITERAL |TRUE |FALSE |BIT_STRING_LITERAL |MONEY_LITERAL |HEX_LITERAL |STRING_LITERAL |UNICODE_STRING_LITERAL;

with_partition_number_expression:WITH LPAREN PARTITIONS partition_number_expression_list RPAREN;

partition_number_expression_list: LPAREN partition_number_expression (COMMA partition_number_expression)*  RPAREN;
partition_number_expression: range | literal;
range: literal TO literal;

// TODO : complete After ONLYONE checks it
function_name : full_table_name  ;

function_parameters
    : LPAREN function_parameter_list? RPAREN  ;

function_parameter_list
    : function_parameter (COMMA function_parameter)*;

function_parameter
    : USER_VARIABLE AS?  datatype  (NULL | NOT NULL)? (EQ default_value)? (READONLY)?;

default_value
    : literal
    | NULL
    ;



index_name : IDENTIFIER;

view_attribute
    : ENCRYPTION
    | SCHEMABINDING
    | VIEW_METADATA
    ;

view_check_option : WITH CHECK OPTION ;

// These Are Implemented in Alter visitor
resumable_option:RESUMABLE EQ (ON | OFF);

max_dop_expression_option : MAXDOP EQ expression;
mx_duration_expr_option :MAX_DURATION EQ expression (MINUTES)?;
online_eq_online_option: ONLINE EQ (ON low_priority_lock_wait_clause?| OFF);

// End of Alter visitor
pad_index_option  : PAD_INDEX EQ (ON | OFF);
filter_factor_option
    : FILTER_FACTOR EQ literal
    ;
drop_existing_option
    : DROP_EXISTING EQ (ON | OFF)
    ;
index_common_option
    : pad_index_option
    | filter_factor_option
    | ignore_dup_key_option
    | allow_row_locks_option
    | allow_page_locks_option
    | drop_existing_option
    | online_eq_online_option
    | max_dop_expression_option
    | resumable_option
    | mx_duration_expr_option
    ;

partition_target
    : IDENTIFIER LPAREN full_column_name RPAREN
    | IDENTIFIER
    | DEFAULT
    ;

default_column_definition
    : COLUMN? full_column_name column_type encrypted_with_clause? column_constraint_list
    ;
encrypted_with_clause
    : ENCRYPTED WITH LPAREN encrypted_option (COMMA encrypted_option)* RPAREN
    ;

encrypted_option
    : column_encryption_key_option
    | encryption_type_option
    | algorithm_option
    ;
column_encryption_key_option
    :COLUMN_ENCRYPTION_KEY EQ full_column_name;

encryption_type_option
    : ENCRYPTION_TYPE EQ (DETERMINISTIC | RANDOMIZED)
    ;

algorithm_option
    : ALGORITHM EQ STRING_LITERAL
    ;

function_body
    : begin_end_function_body
    | return_function_body
    ;
begin_end_function_body: BEGIN statement* RETURN expression? END;
return_function_body: RETURN (select_statement | LPAREN select_statement RPAREN);

function_return_type
    : column_type | TABLE
    | USER_VARIABLE  table_type_definition

    ;