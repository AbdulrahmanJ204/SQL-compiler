from .ast_node import ASTNode


class TruncateStatement(ASTNode):
    def __init__(self, table, with_partitions=None):
        self.table = table
        self.with_partitions = with_partitions

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.table.print(spacer, level + 1)
        if self.with_partitions:
            self.with_partitions.print(spacer, level + 1)
