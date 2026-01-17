from .ast_node import ASTNode

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
    def __init__(self, table, on = False):
        self.table = table
        self.on = on

    def print(self,spacer = "  ", level=0):
        self.self_print(spacer * level , " ON "if self.on else " OFF " )
        self.table.print(spacer, level + 1)

