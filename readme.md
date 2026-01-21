# T-SQL Parser

A comprehensive T-SQL (Transact-SQL) parser built with ANTLR4 and Python that generates Abstract Syntax Trees (ASTs) for SQL Server statements.

## Overview

This project provides a complete parser for T-SQL syntax, supporting a wide range of SQL Server statements including DDL, DML, control flow, transactions, cursors, and more. The parser processes SQL files and generates detailed AST representations that can be used for code analysis, transformation, or documentation.

## Features

### Supported SQL Statements

**Data Definition Language (DDL):**
- `CREATE` - Tables, indexes, views, users, logins, functions
- `ALTER` - Tables, indexes, views, users
- `DROP` - Tables, views, users, indexes, functions
- `TRUNCATE` - Tables with partition support

**Data Manipulation Language (DML):**
- `SELECT` - Full query support including CTEs, joins, subqueries, set operations
- `INSERT` - Single/multiple rows, from SELECT statements
- `UPDATE` - Standard updates, joins, OUTPUT clause
- `DELETE` - With joins and OUTPUT clause

**Control Flow:**
- `IF`/`ELSE` statements
- `WHILE` loops
- `BEGIN`/`END` blocks
- `BREAK`/`CONTINUE` statements

**Transactions:**
- `BEGIN TRANSACTION` / `BEGIN DISTRIBUTED TRANSACTION`
- `COMMIT TRANSACTION` / `COMMIT WORK`
- `ROLLBACK TRANSACTION` / `ROLLBACK WORK`
- `SAVE TRANSACTION`

**Cursors:**
- `DECLARE CURSOR` - All cursor types and options
- `OPEN` / `CLOSE` / `DEALLOCATE`
- `FETCH` - All fetch directions

**Variables:**
- `DECLARE` - Scalar, table, and cursor variables
- `SET` - Variable assignments

**Additional Features:**
- Common Table Expressions (CTEs)
- Window functions
- OUTPUT clause
- Identity insert
- Session settings (`SET` statements)
- Function declarations
- Index management
- User and login management

## Project Structure

```
src/
├── parser/                    # ANTLR4 grammar files
│   ├── SQLLexer.g4           # Lexical analyzer
│   ├── SQLParser.g4          # Main parser grammar
│   ├── BasicParser.g4        # Basic SQL constructs
│   ├── SelectParser.g4       # SELECT statements
│   ├── InsertParser.g4       # INSERT statements
│   ├── UpdateParser.g4       # UPDATE statements
│   ├── DeleteParser.g4       # DELETE statements
│   ├── CreateParser.g4       # CREATE statements
│   ├── AlterParser.g4        # ALTER statements
│   ├── DropParser.g4         # DROP statements
│   ├── TruncateParser.g4     # TRUNCATE statements
│   ├── TransactParser.g4     # Transaction control
│   ├── CursorParser.g4       # Cursor operations
│   ├── ControlFlowParser.g4  # Control flow statements
│   ├── VariableParser.g4     # Variable declarations
│   ├── ExpressionParser.g4   # Expression parsing
│   ├── OutputParser.g4       # OUTPUT clause
│   └── CteParser.g4          # Common Table Expressions
│
├── sql_ast/                   # AST implementation
│   ├── ast_nodes/            # AST node definitions
│   │   ├── __init__.py
│   │   ├── ast_node.py       # Base AST node class
│   │   ├── basic_nodes.py    # Common AST nodes
│   │   ├── select_nodes.py   # SELECT AST nodes
│   │   ├── insert_nodes.py   # INSERT AST nodes
│   │   ├── update_nodes.py   # UPDATE AST nodes
│   │   ├── delete_nodes.py   # DELETE AST nodes
│   │   ├── create_nodes.py   # CREATE AST nodes
│   │   ├── alter_nodes.py    # ALTER AST nodes
│   │   ├── drop_nodes.py     # DROP AST nodes
│   │   ├── truncate_nodes.py # TRUNCATE AST nodes
│   │   ├── transact_nodes.py # Transaction AST nodes
│   │   ├── cursor_nodes.py   # Cursor AST nodes
│   │   ├── control_flow_nodes.py # Control flow AST nodes
│   │   ├── variable_nodes.py # Variable AST nodes
│   │   ├── expression_nodes.py # Expression AST nodes
│   │   ├── output_nodes.py   # OUTPUT clause AST nodes
│   │   ├── cte_nodes.py      # CTE AST nodes
│   │   ├── statements.py     # Statement nodes
│   │   └── program.py        # Program root node
│   │
│   ├── visitors/             # Visitor pattern implementations
│   │   ├── __init__.py
│   │   ├── basic_visitor.py
│   │   ├── select_visitor.py
│   │   ├── insert_visitor.py
│   │   ├── update_visitor.py
│   │   ├── delete_visitor.py
│   │   ├── create_visitor.py
│   │   ├── alter_visitor.py
│   │   ├── drop_visitor.py
│   │   ├── truncate_visitor.py
│   │   ├── transact_visitor.py
│   │   ├── cursor_visitor.py
│   │   ├── control_flow_visitor.py
│   │   ├── variable_visitor.py
│   │   ├── expression_visitor.py
│   │   ├── output_visitor.py
│   │   └── cte_visitor.py
│   │
│   ├── __init__.py
│   └── ast_builder_visitor.py # Main AST builder
│
├── __init__.py
├── errors_listner.py          # Custom error listener
└── main.py                    # Entry point
```

## Installation

### Prerequisites

- Python 3.7 or higher
- ANTLR4 (for grammar compilation)
- Java Runtime Environment (required by ANTLR4)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd tsql-parser
   ```

2. **Install ANTLR4 Python runtime:**
   ```bash
   pip install antlr4-python3-runtime
   ```

3. **Install ANTLR4 tool (if not already installed):**
   
   Download from: https://www.antlr.org/download.html
   
   Or use a package manager:
   ```bash
   # macOS
   brew install antlr
   
   # Ubuntu/Debian
   apt-get install antlr4
   ```

4. **Generate parser files from ANTLR4 grammars:**
   ```bash
   antlr4 -o gen/parser -package parser -listener -visitor -lib src/parser src/parser/SQLParser.g4 src/parser/SQLLexer.g4
   ```

## Usage

### Basic Usage

Parse a SQL file and print the AST:

```bash
python src/main.py path/to/your/file.sql
```

### Running Tests

```bash
python src/main.py tests/train.sql
python src/main.py tests/train2-1.sql
```

### Command-Line Options

- `file` - Path to the SQL file to parse (default: `../tests/test.sql`)
- `--tokens` - Print lexer tokens before parsing

Example with token output:
```bash
python src/main.py tests/train.sql --tokens
```

### Programmatic Usage

```python
from antlr4 import FileStream, CommonTokenStream
from generated.SQLLexer import SQLLexer
from generated.SQLParser import SQLParser
from sql_ast.ast_builder_visitor import ASTBuilderVisitor
from errors_listner import SQLErrorListener

# Read SQL file
input_stream = FileStream('example.sql', encoding='utf-8')

# Lexical analysis
lexer = SQLLexer(input_stream)
lexer.removeErrorListeners()
lexer.addErrorListener(SQLErrorListener())
token_stream = CommonTokenStream(lexer)

# Parsing
parser = SQLParser(token_stream)
parser.removeErrorListeners()
parser.addErrorListener(SQLErrorListener())
tree = parser.program()

# Build AST
visitor = ASTBuilderVisitor()
ast = visitor.visit(tree)

# Print AST
ast.print("    ")
```

## AST Structure

The parser generates a hierarchical AST with the following key components:

### Root Node
- `Program` - Contains all top-level statements

### Statement Types
- **DML Statements**: `SelectStatement`, `InsertStatementNode`, `UpdateStatementNode`, `DeleteStatementNode`
- **DDL Statements**: `CreateTable`, `AlterTableStatement`, `DropTable`, etc.
- **Control Flow**: `IfClause`, `WhileClause`, `StatementBlock`
- **Transactions**: `BeginTransactionNode`, `CommitTransactionNode`, `RollbackTransactionNode`
- **Cursors**: `DeclareCursorNode`, `OpenCursor`, `FetchRow`, etc.
- **Variables**: `DeclareVariableNode`, `SetScalarVariableNode`

### Expression Nodes
- Binary expressions: `OrExpression`, `AndExpression`, `ComparisonExpression`, etc.
- Unary expressions: `NotExpression`, `UnaryExpression`
- Special expressions: `CaseExpression`, `InExpression`, `BetweenExpression`, `ExistsExpression`

### Example AST Output

```
Program 
    Select Statement:
        Query Expression:
            Query Specification:
                Quantifier : DISTINCT
                Columns:
                    Column : CustomerID
                    Column : CustomerName
                From:
                    Table Sources:
                        Table Source:
                            Table Source Details :
                                Table Name : Customers
```

## Grammar Organization

The parser uses a modular grammar structure with multiple grammar files:

- **SQLLexer.g4** - Tokenization rules
- **SQLParser.g4** - Main parser entry point
- **BasicParser.g4** - Common constructs (WHERE, JOIN, ORDER BY, etc.)
- **ExpressionParser.g4** - Expression parsing with proper precedence
- Specialized parsers for each statement type

## Error Handling

The parser includes custom error listeners that capture:
- Lexer errors (invalid tokens)
- Parser errors (syntax errors)
- Line and column information for each error

Errors are collected and can be accessed programmatically or printed to the console.

## Development

### Regenerating Parser Files

After modifying grammar files, regenerate the parser:

```bash
antlr4 -o gen/parser -package parser -listener -visitor -lib src/parser src/parser/SQLParser.g4 src/parser/SQLLexer.g4
```

### Adding New Features

1. Update the appropriate grammar file in `src/parser/`
2. Regenerate parser files
3. Create or update AST node classes in `src/sql_ast/ast_nodes/`
4. Implement visitor methods in `src/sql_ast/visitors/`
5. Add tests

## Testing

Place test SQL files in the `tests/` directory and run:

```bash
python src/main.py tests/your_test_file.sql
```

## License

[ِA Students work so feel free to use it]

## Acknowledgments

- Built with [ANTLR4](https://www.antlr.org/)
- Inspired by SQL Server T-SQL syntax

## Contacts

Please email one of us for any Questions :)
- muhammadaydi7@gmail.com
- abdallaalkasm9@gmail.com
- abdalrahmanaljomaat@gmail.com
- Alaaalshahror@gmail.com
- manarkurdy111@gmail.com
