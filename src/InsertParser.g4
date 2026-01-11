parser grammar InsertParser;

options {
	tokenVocab = SQLLexer;
}
// -- Form 1: INSERT with VALUES
// INSERT INTO table_name (col1, col2) VALUES (val1, val2);

// -- Form 2: INSERT with SELECT
// INSERT INTO table_name (col1, col2) SELECT col1, col2 FROM other_table;

// -- Form 3: INSERT without column list
// INSERT INTO table_name VALUES (val1, val2);
import BasicParser;
import selectParser;
insert_statement:
	INSERT INTO table_source column_list? insert_source SEMI?;


column_list : LPAREN column (COMMA column)* RPAREN;
insert_source : values_source | select_statement;
values_source: VALUES values_list (COMMA values_list)*;
values_list :LPAREN value (COMMA value)* RPAREN ;
value : LITERAL |IDENTIFIER | NULL;