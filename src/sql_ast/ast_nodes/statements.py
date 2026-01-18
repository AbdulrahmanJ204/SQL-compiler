from .ast_node import ASTNode
from .basic_nodes import SingleValueNode


class PrintStatement(ASTNode):
    def __init__(self, value):
        self.value = value

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.value.print(spacer, level + 1)


class DeleteStatement(ASTNode):
    def __init__(self,table , where = None ,  top = None, output = None):
        self.table = table
        self.where = where
        self.top = top
        self.output = output

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.table.print(spacer, level + 1)
        if self.top:
            self.top.print(spacer, level + 1)
        if self.where:
            self.where.print(spacer, level + 1)
        if self.output:
            self.output.print(spacer, level + 1)


class SetStatement(ASTNode):
    def __init__(self, table, on = False , is_identity_insert = False):
        self.table = table
        self.on = on
        self.is_identity_insert = is_identity_insert

    def print(self,spacer = "  ", level=0):
        self.self_print(spacer * level , " ON "if self.on else " OFF " )
        if self.is_identity_insert:
            print(spacer * level , "IDENTITY_INSERT")
        self.table.print(spacer, level + 1)

class SetOption(SingleValueNode):
    pass