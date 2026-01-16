from antlr4 import *
from generated.SQLLexer import SQLLexer
from generated.SQLParser import SQLParser
from sql_ast.ast_builder_visitor import ASTBuilderVisitor


def main():
    input_stream = FileStream("tests/test.sql", encoding='utf-8')

    lexer = SQLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SQLParser(tokens)

    parse_tree = parser.program()
    visitor = ASTBuilderVisitor()
    ast = visitor.visit(parse_tree)

    print("\nAST:")
    ast.print()


if __name__ == "__main__":
    main()
