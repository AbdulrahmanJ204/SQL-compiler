parser grammar SQLParser;

options {
	tokenVocab = SQLLexer;
}

import SelectParser , InsertParser ,DeleteParser,UpdateParser,AlterParser, OutputParser,CteParser, CreateParser, CursorParser, VariableParser, ControlFlowParser,DropParser, TruncateParser, TransactParser;



program: statement* EOF;



ddl_statement:alter_statement | create_statement | drop_statement | truncate_statement;
dml_statement: select_statement | insert_statement | delete_statement | update_statement;
variable_statement: declare_var | set_variable;
cursor_statement: declare_cursor | close_cursor | open_cursor | fetch_row | deallocate_cursor;






statement:transaction_statement|  dml_statement | ddl_statement | variable_statement | cursor_statement | control_flow_statement | go_statement| print_clause|function_call|set_statement;



set_statement
    :SET set_options  SEMI?
    ;


set_options: set_options_list|identity_insert;

set_options_list:set_option_name_list (ON | OFF);
identity_insert:  IDENTITY_INSERT full_table_name (ON | OFF);

set_option_name_list
    : set_option_name (COMMA set_option_name)*;

set_option_name
    : ANSI_PADDING|NUMERIC_ROUNDABORT| NOCOUNT| ANSI_WARNINGS | CONCAT_NULL_YIELDS_NULL | ARITHABORT | QUOTED_IDENTIFIER | ANSI_NULLS ;


