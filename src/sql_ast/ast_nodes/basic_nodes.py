from .ast_node import ASTNode


class SingleValueNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.value)


class Variable(SingleValueNode):
    pass


class Literal(SingleValueNode):
    pass


class GroupBy(ASTNode):
    def __init__(self, items, with_):
        self.items = items
        self.with_ = with_

    def print(self, spacer="  ", level=0):
        to_print = ""
        if self.with_:
            to_print = "WITH " + self.with_

        self.self_print(spacer * level, to_print)
        for item in self.items:
            item.print(spacer, level + 1)


class OrderByItem(ASTNode):
    def __init__(self, expression, asc=True):
        self.expression = expression
        self.asc = asc

    def print(self, spacer="  ", level=0):
        print(spacer * level + "ASC" if self.asc else "DESC")
        self.expression.print(spacer, level + 1)


class OrderByOffset(ASTNode):
    def __init__(self, offset, fetch_next_rows_only=None):
        self.offset = offset
        self.fetch_next_rows_only = fetch_next_rows_only

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        print(spacer * (level + 1) + "OFFSET : ")
        self.offset.print(spacer, level + 2)
        if self.fetch_next_rows_only:
            print(spacer * (level + 1), "ONLY NEXT ROWS :")
            self.fetch_next_rows_only.print(spacer, level + 2)


class OrderBy(ASTNode):
    def __init__(self, order_by_list, offset=None):
        self.order_by_list = order_by_list
        self.offset = offset

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        for item in self.order_by_list:
            item.print(spacer, level + 1)

        if self.offset:
            self.offset.print(spacer, level + 1)


class SetOperator(ASTNode):
    def __init__(self, operator):
        self.operator = operator

    def print(self, spacer="  ", level=0):
        print(spacer * level, self.operator)

class SingleExpressionNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.expression.print(spacer, level + 1)


class ExpressionAlaisNode(ASTNode):
    def __init__(self, expression, alias=None):
        self.expression = expression
        self.alias = alias

    def print(self, spacer="  ", level=0):
        # self.self_print(spacer * level)
        self.expression.print(spacer, level + 1)
        if self.alias:
            self.alias.print(spacer, level + 2)


class WhereClause(ASTNode):
    def __init__(self, condition, is_cursor=False):
        self.condition = condition
        self.is_cursor = is_cursor

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        if self.is_cursor:
            print(spacer * (level + 2), "CURRENT OF :")
        self.condition.print(spacer, level + 1)


class StatementBlock(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        for statement in self.statements:
            statement.print(spacer, level + 1)


class Alias(SingleExpressionNode):
    pass


class Having(SingleExpressionNode):
    pass


class Table(ASTNode):  # full_table_name
    def __init__(self, parts):
        self.parts = parts

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, ".".join(self.parts))


class ColumnOrTable(ASTNode):
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


class DerivedTable(SingleExpressionNode):
    pass


class TableSourceItem(ExpressionAlaisNode):
    def print(self, spacer="  ", level=0):
        self.expression.print(spacer, level + 1)
        if self.alias:
            self.alias.print(spacer, level + 1)


class TableSourceList(ASTNode):
    def __init__(self, sources):
        self.sources = sources

    def print(self, spacer="  ", level=0):
        # self.self_print(spacer * level)
        for i, src in enumerate(self.sources):
            src.print(spacer, level)


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


class TableSource(ASTNode):
    def __init__(self, table, joins):
        self.table = table
        self.joins = joins

    def print(self, spacer="  ", level=0):
        # self.self_print(spacer * level)
        self.table.print(spacer, level + 1)
        if self.joins:
            for join in self.joins:
                join.print(spacer, level + 2)
