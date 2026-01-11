lexer grammar SQLLexer;
options {
	caseInsensitive = true;
}

tokens {
	IDENTIFIER,
	LITERAL,
	OPERATOR
}

//! ╔══════════════════════════════════╗
//! ║━━━━━━━━━━━━<KEYWORDS>━━━━━━━━━━━━║
//! ╚══════════════════════════════════╝
ADD: 'ADD';
ALL: 'ALL';
ALTER: 'ALTER';
AND: 'AND';
ANY: 'ANY';
AS: 'AS';
ASC: 'ASC';
AUTHORIZATION: 'AUTHORIZATION';
BACKUP: 'BACKUP';
BEGIN: 'BEGIN';
BETWEEN: 'BETWEEN';
BREAK: 'BREAK';
BROWSE: 'BROWSE';
BULK: 'BULK';
BY: 'BY';
OUTPUT  : 'OUTPUT';
DELETED : 'DELETED';
CASCADE: 'CASCADE';
CASE: 'CASE';
CHECK: 'CHECK';
CHECKPOINT: 'CHECKPOINT';
CLOSE: 'CLOSE';
CLUSTERED: 'CLUSTERED';
COALESCE: 'COALESCE';
COLLATE: 'COLLATE';
COLUMN: 'COLUMN';
COMMIT: 'COMMIT';
COMPUTE: 'COMPUTE';
CONSTRAINT: 'CONSTRAINT';
CONTAINS: 'CONTAINS';
CONTAINSTABLE: 'CONTAINSTABLE';
CONTINUE: 'CONTINUE';
CONVERT: 'CONVERT';
CREATE: 'CREATE';
CROSS: 'CROSS';
CURRENT: 'CURRENT';
CURRENT_DATE: 'CURRENT_DATE';
CURRENT_TIME: 'CURRENT_TIME';
CURRENT_TIMESTAMP: 'CURRENT_TIMESTAMP';
CURRENT_USER: 'CURRENT_USER';
CURSOR: 'CURSOR';
DATABASE: 'DATABASE';
DBCC: 'DBCC';
DEALLOCATE: 'DEALLOCATE';
DECLARE: 'DECLARE';
DEFAULT: 'DEFAULT';
DELETE: 'DELETE';
DENY: 'DENY';
DESC: 'DESC';
DISK: 'DISK';
DISTINCT: 'DISTINCT';
DISTRIBUTED: 'DISTRIBUTED';
DOUBLE: 'DOUBLE';
DROP: 'DROP';
DUMP: 'DUMP';
ELSE: 'ELSE';
END: 'END';
ERRLVL: 'ERRLVL';
ESCAPE: 'ESCAPE';
EXCEPT: 'EXCEPT';
EXEC: 'EXEC';
EXECUTE: 'EXECUTE';
EXISTS: 'EXISTS';
EXIT: 'EXIT';
EXTERNAL: 'EXTERNAL';
FETCH: 'FETCH';
FILE: 'FILE';
FILLFACTOR: 'FILLFACTOR';
FOR: 'FOR';
FOREIGN: 'FOREIGN';
FREETEXT: 'FREETEXT';
FREETEXTTABLE: 'FREETEXTTABLE';
FROM: 'FROM';
FULL: 'FULL';
FUNCTION: 'FUNCTION';
GOTO: 'GOTO';
GRANT: 'GRANT';
GROUP: 'GROUP';
HAVING: 'HAVING';
HOLDLOCK: 'HOLDLOCK';
IDENTITY: 'IDENTITY';
IDENTITY_INSERT: 'IDENTITY_INSERT';
IDENTITYCOL: 'IDENTITYCOL';
IF: 'IF';
IN: 'IN';
INDEX: 'INDEX';
INNER: 'INNER';
INSERT: 'INSERT';
INTERSECT: 'INTERSECT';
INTO: 'INTO';
IS: 'IS';
JOIN: 'JOIN';
KEY: 'KEY';
KILL: 'KILL';
LEFT: 'LEFT';
LIKE: 'LIKE';
LINENO: 'LINENO';
LOAD: 'LOAD';
MERGE: 'MERGE';
NATIONAL: 'NATIONAL';
NOCHECK: 'NOCHECK';
NONCLUSTERED: 'NONCLUSTERED';
NOT: 'NOT';
NULL: 'NULL';
NULLIF: 'NULLIF';
OBJECT_SCHEMA_NAME: 'OBJECT_SCHEMA_NAME';
OF: 'OF';
OFF: 'OFF';
OFFSETS: 'OFFSETS';
ON: 'ON';
OPEN: 'OPEN';
OPENDATASOURCE: 'OPENDATASOURCE';
OPENQUERY: 'OPENQUERY';
OPENROWSET: 'OPENROWSET';
OPENXML: 'OPENXML';
OPTION: 'OPTION';
OR: 'OR';
ORDER: 'ORDER';
OUTER: 'OUTER';
OVER: 'OVER';
PERCENT: 'PERCENT';
PIVOT: 'PIVOT';
PLAN: 'PLAN';
PRECISION: 'PRECISION';
PRIMARY: 'PRIMARY';
PRINT: 'PRINT';
PROC: 'PROC';
PROCEDURE: 'PROCEDURE';
PUBLIC: 'PUBLIC';
QUOTENAME: 'QUOTENAME';
RAISERROR: 'RAISERROR';
READ: 'READ';
READTEXT: 'READTEXT';
RECONFIGURE: 'RECONFIGURE';
REFERENCES: 'REFERENCES';
REPLICATION: 'REPLICATION';
RESTORE: 'RESTORE';
RESTRICT: 'RESTRICT';
RETURN: 'RETURN';
REVERT: 'REVERT';
REVOKE: 'REVOKE';
RIGHT: 'RIGHT';
ROLLBACK: 'ROLLBACK';
ROWCOUNT: 'ROWCOUNT';
ROWGUIDCOL: 'ROWGUIDCOL';
RULE: 'RULE';
SAVE: 'SAVE';
SCHEMA: 'SCHEMA';
SELECT: 'SELECT';
SEMANTICKEYPHRASETABLE: 'SEMANTICKEYPHRASETABLE';
SEMANTICSIMILARITYDETAILSTABLE:
	'SEMANTICSIMILARITYDETAILSTABLE';
SEMANTICSIMILARITYTABLE: 'SEMANTICSIMILARITYTABLE';
SESSION_USER: 'SESSION_USER';
SET: 'SET';
SETUSER: 'SETUSER';
SHUTDOWN: 'SHUTDOWN';
SOME: 'SOME';
STATISTICS: 'STATISTICS';
SYSTEM_USER: 'SYSTEM_USER';
TABLE: 'TABLE';
TABLESAMPLE: 'TABLESAMPLE';
TEXTSIZE: 'TEXTSIZE';
THEN: 'THEN';
TO: 'TO';
TOP: 'TOP';
TRAN: 'TRAN';
TRANSACTION: 'TRANSACTION';
TRIGGER: 'TRIGGER';
TRUNCATE: 'TRUNCATE';
TRY_CONVERT: 'TRY_CONVERT';
TSEQUAL: 'TSEQUAL';
UNION: 'UNION';
UNIQUE: 'UNIQUE';
UNPIVOT: 'UNPIVOT';
UPDATE: 'UPDATE';
UPDATETEXT: 'UPDATETEXT';
USE: 'USE';
USER: 'USER';
VALUES: 'VALUES';
VARYING: 'VARYING';
VIEW: 'VIEW';
WAITFOR: 'WAITFOR';
WHEN: 'WHEN';
WHERE: 'WHERE';
WHILE: 'WHILE';
WITH: 'WITH';
WITHIN_GROUP: 'WITHIN_GROUP';
WRITETEXT: 'WRITETEXT';
CAST: 'CAST';
COUNT: 'COUNT';
CUBE: 'CUBE';
CURRENT_SCHEMA: 'CURRENT_SCHEMA';
DATETIME: 'DATETIME';
DAY: 'DAY';
HOUR: 'HOUR';
MINUTE: 'MINUTE';
MONTH: 'MONTH';
SECOND: 'SECOND';
YEAR: 'YEAR';
EXPLAIN: 'EXPLAIN';
FILTER: 'FILTER';
GROUPING: 'GROUPING';
INTERVAL: 'INTERVAL';
LIMIT: 'LIMIT';
OFFSET: 'OFFSET';
ONLY: 'ONLY';
PARTITION: 'PARTITION';
RECURSIVE: 'RECURSIVE';
ROLLUP: 'ROLLUP';
ROW: 'ROW';
ROWS: 'ROWS';
WINDOW: 'WINDOW';
BIGINT: 'BIGINT';
BINARY: 'BINARY';
BIT: 'BIT';
CHAR: 'CHAR';
DATE: 'DATE';
DECIMAL_TYPE: 'DECIMAL_TYPE';
FLOAT_TYPE: 'FLOAT_TYPE';
INT_TYPE: 'INT_TYPE';
MONEY: 'MONEY';
NCHAR: 'NCHAR';
NUMERIC: 'NUMERIC';
NVARCHAR: 'NVARCHAR';
REAL: 'REAL';
SMALLINT: 'SMALLINT';
TEXT: 'TEXT';
TIME: 'TIME';
TIMESTAMP: 'TIMESTAMP';
TINYINT: 'TINYINT';
UNIQUEIDENTIFIER: 'UNIQUEIDENTIFIER';
VARBINARY: 'VARBINARY';
VARCHAR: 'VARCHAR';
XML: 'XML';

//! ╔══════════════════════════════════╗
//! ║━━━━━━━━━━━━<LITERALs>━━━━━━━━━━━━║
//! ╚══════════════════════════════════╝
NUMBER_LITERAL:
	(DIGIT+ ( '.' DIGIT*)? | '.' DIGIT+) ('E' [+\-]? DIGIT+)? -> type(LITERAL);

TRUE: 'TRUE' -> type(LITERAL);
FALSE: 'FALSE' -> type(LITERAL);

BIT_STRING_LITERAL:
	'B' SINGLE_QUOTE BITFrag+ SINGLE_QUOTE -> type(LITERAL);

fragment BITFrag: [01];

MONEY_LITERAL:
	[$\u00A2\u00A3\u00A4\u00A5] NUMBER_LITERAL -> type(LITERAL);

HEX_LITERAL: ('0' 'X' (( NEW_LINE_STRING | HEX_REP)+ |)) -> type(LITERAL);
// {
//       raw = self.text
//       # Remove \r and \n that come after backslash
//       raw = raw.replace("\\\r\n", "")
//       raw = raw.replace("\\\n", "")
//       raw = raw.replace("\\\r", "")
//       if raw[-1] in ['x', 'X']:
//             raw+="0"
//       self.text = raw
// };

fragment HEX_REP: [0-9A-F];
fragment NEW_LINE_STRING: '\\' '\r'? '\n';

STRING_LITERAL:
	(
		SINGLE_QUOTE (ESCAPED_QUOTE | NEW_LINE_STRING | ~['\r\n])* SINGLE_QUOTE
	)-> type(LITERAL);
// {
//   raw = self.text
//   # Remove the first and last quote
//   raw = raw[1:-1]
//   # Replace doubled single quotes with one single quote
//   raw = raw.replace("''", "'")
//   # Remove \r and \n that come after backslash
//   raw = raw.replace("\\\r\n", "")  # Windows line ending
//   raw = raw.replace("\\\n", "")    # Unix line ending
//   raw = raw.replace("\\\r", "")    # Old Mac line ending
//   self.text = raw
// };

UNICODE_STRING_LITERAL: ('N' STRING_LITERAL)-> type(LITERAL);
//  {
//         raw = self.text
//         # Remove the N , first and last quote
//         raw = raw[2:-1]
//         # Replace doubled single quotes with one single quote
//         raw = raw.replace("''", "'")
//         # Remove \r and \n that come after backslash
//         raw = raw.replace("\\\r\n", "")  # Windows line ending
//         raw = raw.replace("\\\n", "")    # Unix line ending
//         raw = raw.replace("\\\r", "")    # Old Mac line ending
//         self.text = raw
//       };

fragment SINGLE_QUOTE: '\'';
fragment ESCAPED_QUOTE: '\'\'';

//! ╔═════════════════════════════════╗
//! ║━━━━━━━━━━<IDENTIFIERs>━━━━━━━━━━║
//! ╚═════════════════════════════════╝
UNQUOTED_IDENTIFIER:
	IDENTIFIER_START IDENTIFIER_REST* -> type(IDENTIFIER);
BRACKET_IDENTIFIER:
	'[' (~[\]\r\n] | ']]')* ']' -> type(IDENTIFIER);
DOUBLE_QUOTED_IDENTIFIER:
	'"' ('""' | ~["\r\n])* '"' -> type(IDENTIFIER);

//! ╔═════════════════════════════════╗
//! ║━━━━━━━━━━━<VARIABLEs>━━━━━━━━━━━║
//! ╚═════════════════════════════════╝
USER_VARIABLE: '@' IDENTIFIER_START IDENTIFIER_REST*;
SYSTEM_VARIABLE: '@@' IDENTIFIER_START IDENTIFIER_REST*;
fragment IDENTIFIER_START: [a-z_#];
fragment IDENTIFIER_REST: [a-z0-9_#@$];

//! ╔══════════════════════════════════════════════════╗
//! ║━━━━━━━━━━━<OPERATORs AND PUNCTUATIONs>━━━━━━━━━━━║
//! ╚══════════════════════════════════════════════════╝
SEMI: ';';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';

EQ: '=' -> type(OPERATOR);
NEQ: ('!=' | '<>') -> type(OPERATOR);
LTE: '<=' -> type(OPERATOR);
GTE: '>=' -> type(OPERATOR);
LT: '<' -> type(OPERATOR);
GT: '>' -> type(OPERATOR);

MINUS: '-';
STAR: '*';
SLASH: '/';
PLUS: '+';
PERCENT_OP: '%';

PLUS_EQ: '+=';
MINUS_EQ: '-=';
STAR_EQ: '*=';
SLASH_EQ: '/=';
PERCENT_EQ: '%=';

AMPERSAND: '&';
PIPE: '|';
CARET: '^';

//! ╔═══════════════════════════════════════════════╗
//! ║━━━━━━━━━━━<COMMENTs AND WHITESPACE>━━━━━━━━━━━║
//! ╚═══════════════════════════════════════════════╝
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '--' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;


fragment DIGIT: [0-9];
