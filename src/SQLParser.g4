parser grammar SQLParser;

options {
	tokenVocab = SQLLexer;
}

import SelectParser , InsertParser ,DeleteParser,UpdateParser  ;

tsql_file: statement* EOF;

statement: select_statement | insert_statement | delete_statement | update_statement;

//! ╔══════════════════════════════════════════╗
//! ║━━━━━━━━━━━━<SELECT STATEMENT>━━━━━━━━━━━━║
//! ╚══════════════════════════════════════════╝
