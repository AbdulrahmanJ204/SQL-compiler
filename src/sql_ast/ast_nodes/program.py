from .ast_node import ASTNode


class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def print(self, spacer="  ", level=1):
        print(spacer * level + "Program ")
        for statement in self.statements:
            statement.print(spacer, level + 1)
