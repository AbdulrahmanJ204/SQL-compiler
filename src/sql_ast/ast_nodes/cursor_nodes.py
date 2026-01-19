from ..ast_nodes.ast_node import  ASTNode

class CursorName(ASTNode):
    def __init__(self, name, is_global=False):
        self.name = name
        self.is_global = is_global

    def print(self, spacer="  ", level=0):
        to_print = self.name
        if self.is_global:
            to_print = "GLOBAL" + self.name
        self.self_print(spacer*level , to_print)