parser grammar SelectParser;

options {
	tokenVocab = SQLLexer;
}


import BasicParser;



truncate_statement: TRUNCATE TABLE full_table_name (with_partition_number_expression)? SEMI?;

