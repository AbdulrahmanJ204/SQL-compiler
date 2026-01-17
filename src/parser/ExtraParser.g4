parser grammar ExtraParser;
options {
	tokenVocab = SQLLexer;
}

user_variable : USER_VARIABLE;
system_variable: SYSTEM_VARIABLE;
