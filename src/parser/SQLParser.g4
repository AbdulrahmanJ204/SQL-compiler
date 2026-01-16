parser grammar SQLParser;

options {
	tokenVocab = SQLLexer;
}


import SelectParser , InsertParser ,DeleteParser,UpdateParser,AlterParser, OutputParser,CteParser, CreateParser, CursorParser, VariableParser, ControlFlowParser,DropParser;

program: statement* EOF;


ddl_statement:alter_statement | create_statement | drop_statement;
dml_statement: select_statement | insert_statement | delete_statement | update_statement;
variable_statement: declare_var | set_variable;
cursor_statement: declare_cursor | close_cursor | open_cursor | fetch_row | deallocate_cursor;



statement: search_condition| dml_statement | ddl_statement | variable_statement | cursor_statement | control_flow_statement | go_statement| print_clause|function_call|set_statement;
set_statement
    : SET IDENTITY_INSERT full_table_name (ON | OFF) SEMI? ;




