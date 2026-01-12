import argparse
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener

from generated.SQLLexer import SQLLexer
from generated.SQLParser import SQLParser
from visualizar import visualize_parse_tree



def to_string_tree(root, symbolic_lexer_names, token_delimiter='"', show_token_types=True):
    builder = []
    _to_string_tree_traverse(root, builder, symbolic_lexer_names, token_delimiter, show_token_types)
    return ''.join(builder)


def _to_string_tree_traverse(tree, builder, symbolic_lexer_names, token_delimiter, show_token_types):
    child_list_stack = [[tree]]

    while len(child_list_stack) > 0:
        child_stack = child_list_stack[-1]

        if len(child_stack) == 0:
            child_list_stack.pop()
        else:
            tree = child_stack.pop(0)
            node = str(type(tree).__name__).replace('Context', '')
            node = '{0}{1}'.format(node[0].lower(), node[1:])

            indent = []

            for i in range(0, len(child_list_stack) - 1):
                indent.append('║  ' if len(child_list_stack[i]) > 0 else '   ')

            token_name = ''
            token_type = tree.getPayload().type if node.startswith('terminal') else 0

            if show_token_types and token_type > -1:
                token_name = ' ({0})'.format(symbolic_lexer_names[token_type])

            builder.extend(indent)
            builder.append('╚═ ' if len(child_stack) == 0 else '╠═ ')
            builder.append('{0}{1}{2}{3}'.format(token_delimiter, tree.getText(), token_delimiter, token_name)
                           if node.startswith('terminal') else node)
            builder.append('\n')

            if tree.getChildCount() > 0:
                children = []
                for i in range(0, tree.getChildCount()):
                    children.append(tree.getChild(i))
                child_list_stack.append(children)


DEFAULT_TEST_FILE = "tests/delete_test.sql"

def main():
    parser_cli = argparse.ArgumentParser(description="T-SQL Parser")

    parser_cli.add_argument(
        "file",
        nargs="?",
        default=DEFAULT_TEST_FILE,
        help="SQL file to parse"
    )

    parser_cli.add_argument(
        "--tokens",
        action="store_true",
        help="Print lexer tokens"
    )

    args = parser_cli.parse_args()

    print(f"Parsing file: {args.file}")

    input_stream = FileStream(args.file, encoding='utf-8')

    lexer = SQLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    if args.tokens:
        token_stream.fill()
        for token in token_stream.tokens:
            token_name = lexer.symbolicNames[token.type]
            print(f"{token_name:15} -> {token.text}")
        token_stream.seek(0)

    parser = SQLParser(token_stream)
    
    parser.removeErrorListeners()
    parser.addErrorListener(DiagnosticErrorListener())

    tree = parser.tsql_file()
    # print(tree.toStringTree(recog=parser))
    # Visualize

    print(to_string_tree(tree, lexer.symbolicNames))
    visualize_parse_tree(parser, tree, title="T-SQL Parse Tree")
    


if __name__ == "__main__":
    main()
