parser grammar SQLParser;

options {
	tokenVocab = SQLLexer;
}

import SelectParser , InsertParser ,DeleteParser,UpdateParser,AlterParser, OutputParser,CteParser, CreateParser;

tsql_file: statement* EOF;

ddl_statement:alter_statement | create_statement;
dml_statement:with_cte? (select_statement | insert_statement | delete_statement | update_statement);

statement: dml_statement | ddl_statement;

//! ╔══════════════════════════════════════════╗
//! ║━━━━━━━━━━━━<SELECT STATEMENT>━━━━━━━━━━━━║
//! ╚══════════════════════════════════════════╝
