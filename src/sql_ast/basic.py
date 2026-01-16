from .ast_node import ASTNode


class Table(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.name)


class TableRef(ASTNode):
    def __init__(self, parts):
        self.parts = parts

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, ".".join(self.parts))

class ColumnRef(ASTNode):
    def __init__(self, parts):
        self.parts = parts

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, ".".join(self.parts))
