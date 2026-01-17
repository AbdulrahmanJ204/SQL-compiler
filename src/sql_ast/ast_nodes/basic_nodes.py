from .ast_node import ASTNode

class ExpressionAlaisNode(ASTNode):
    def __init__(self, expression, alias=None):
        self.expression = expression
        self.alias = alias

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.expression.print(spacer, level + 1)
        if self.alias:
            print(spacer * (level + 1), "Alias:")
            self.alias.print(spacer, level + 2)


class TableRef(ASTNode): # full_table_name
    def __init__(self, parts):
        self.parts = parts

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, ".".join(self.parts))


class ColumnRef(ASTNode):
    def __init__(self, parts):
        self.parts = parts

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, ".".join(self.parts))


class FunctionCall(ASTNode):
    def __init__(self, name, args=None, schema=None):
        self.schema = schema  # str | None
        self.name = name  # str
        self.args = args or []  # list[FunctionArg] | ["*"]

    def print(self, spacer="  ", level=0):
        full_name = f"{self.schema}.{self.name}" if self.schema else self.name
        self.self_print(spacer * level, full_name)

        if self.args == ["*"]:
            print(spacer * (level + 1) + " -- *")
        else:
            for arg in self.args:
                arg.print(spacer, level + 1)


class FunctionArg(ExpressionAlaisNode):
    pass


class JoinType(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.name)


class Join(ASTNode):
    def __init__(self, join_type, table, join_condition):
        self.join_type = join_type
        self.table = table
        self.join_condition = join_condition

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.table.print(spacer, level + 1)
        self.join_type.print(spacer, level + 1)
        self.join_condition.print(spacer, level + 1)
