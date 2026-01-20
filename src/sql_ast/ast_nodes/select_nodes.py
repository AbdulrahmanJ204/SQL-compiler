from .ast_node import ASTNode
from .expression_nodes import BinaryExpression
from .basic_nodes import ExpressionAlaisNode


class SelectStatement(ASTNode):
    def __init__(self, query, cte=None, order_by=None):
        self.query = query
        self.cte = cte
        self.order_by = order_by

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Select Statement:")
        if self.cte:
            self.cte.print(spacer, level + 1)
        self.query.print(spacer, level + 1)
        if self.order_by:
            self.order_by.print(spacer, level + 1)


class SelectSetOperationsList(ASTNode):
    def __init__(self, lst):
        self.lst = lst

    def print(self, spacer="  ", level=0):
        if len(self.lst) >0:
            print(spacer * level + "Set Operations")
        for item in self.lst:
            item.print(spacer, level + 1)


class SelectSetOperation(ASTNode):
    def __init__(self, set_op, query_spec):
        self.set_op = set_op
        self.query_spec = query_spec

    def print(self, spacer="  ", level=0):
        self.set_op.print(spacer, level + 1)
        self.query_spec.print(spacer, level + 1)


class QueryExpression(ASTNode):
    def __init__(self, left, operations=None):
        self.left = left
        self.operations = operations

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Query Expression:")
        self.left.print(spacer, level+1)
        if self.operations:
            self.operations.print(spacer, level+1)


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
        print(spacer * level + "Query Specification:")
        self.modifier.print(spacer, level + 1)
        self.select_list.print(spacer, level + 1)

        if self.from_:
            print(spacer * (level + 1)+ "From:")
            self.from_.print(spacer, level+2)
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
        if self.quantifier:
            print(spacer * level + self.quantifier)
        if self.top:
            self.top.print(spacer, level + 1)


class TopSpec(ASTNode):
    def __init__(self, value, percent=False):
        self.value = value
        self.percent = percent

    def print(self, spacer="  ", level=0):
        to_print = "Top Percent" if self.percent else "Top :"
        print(spacer * level + to_print)
        self.value.print(spacer, level + 1)


class Star(ASTNode):

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Star (*)")


class TableStarSelectItem(ASTNode):
    def __init__(self, table):
        self.table = table

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table.*")
        self.table.print(spacer, level + 1)


class ExpressionSelectItem(ExpressionAlaisNode):
    pass


class AssignmentSelectItem(BinaryExpression):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Assignment : " + self.operator)
        self.left.print(spacer, level + 1)
        self.right.print(spacer, level + 1)


class SelectList(ASTNode):
    def __init__(self, items):
        self.items = items

    def print(self, spacer="  ", level=0):

        print(spacer * level+ "Columns:")
        for item in self.items:
            item.print(spacer, level+1)
