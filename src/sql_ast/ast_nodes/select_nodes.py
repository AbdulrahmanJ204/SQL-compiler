from .ast_node import ASTNode
from .expressions import BinaryExpression
from .basic_nodes import ExpressionAlaisNode


class SelectStatement(ASTNode):
    def __init__(self, query, cte=None, order_by=None):
        self.query = query
        self.cte = cte
        self.order_by = order_by

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        if self.cte:
            self.cte.print(spacer, level + 1)
        self.query.print(spacer, level + 1)
        if self.order_by:
            self.order_by.print(spacer, level + 1)


class QueryExpression(ASTNode):
    def __init__(self, left, operations=None):
        self.left = left  # QuerySpecification or QueryExpression
        self.operations = operations or []

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.left.print(spacer, level + 1)
        for op in self.operations:
            op.print(spacer, level + 1)


class QuerySpecification(ASTNode):
    def __init__(self, modifier, select_list, into=None, from_=None,
                 where=None, group_by=None, having=None):
        self.modifier = modifier
        self.select_list = select_list
        self.from_ = from_
        self.where = where
        self.group_by = group_by
        self.having = having
        self.into = into

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.modifier.print(spacer, level + 1)
        print(spacer * (level + 1), "Items :")
        for item in self.select_list:
            item.print(spacer, level + 2)

        if self.from_:
            self.from_.print(spacer, level + 1)
        if self.where:
            self.where.print(spacer, level + 1)
        if self.group_by:
            self.group_by.print(spacer, level + 1)
        if self.having:
            self.having.print(spacer, level + 1)
        if self.into:
            self.into.print(spacer, level + 1)


class SelectQuantifier(ASTNode):
    def __init__(self, quantifier=None, top=None):
        self.quantifier = quantifier  # ALL | DISTINCT | None
        self.top = top  # TopSpec | None

    def print(self, spacer="  ", level=0):
        to_print = self.quantifier if self.quantifier is not None else ""
        self.self_print(spacer * level, to_print)
        if self.top:
            self.top.print(spacer, level + 1)


class TopSpec(ASTNode):
    def __init__(self, value, percent=False):
        self.value = value
        self.percent = percent

    def print(self, spacer="  ", level=0):
        to_print = "PERCENT" if self.percent else ""
        self.self_print(spacer * level, to_print)
        self.value.print(spacer, level + 1)


class StarSelectItem(ASTNode):

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)


class TableStarSelectItem(ASTNode):
    def __init__(self, table):
        self.table = table

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.table.print(spacer, level + 1)


class ExpressionSelectItem(ExpressionAlaisNode):
    pass


class AssignmentSelectItem(BinaryExpression):
    pass
