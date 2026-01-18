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
        self.schema = schema
        self.name = name
        self.args = args

    def print(self, spacer="  ", level=0):
        full_name = f"{self.schema}.{self.name}" if self.schema else self.name
        self.self_print(spacer * level, full_name)

        if self.args:
            self.args.print(spacer, level + 1)


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


class ItemsList(ASTNode):
    def __init__(self, items):
        self.items = items

    def print(self, spacer="  ", level=0):
        for item in self.items:
            item.print(spacer, level + 1)


class ColumnList(ItemsList):
    pass


class UserVariableList(ItemsList):
    pass


class NullClause(ASTNode):
    def __init__(self, nullable: bool):
        self.nullable = nullable

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Nullability: {'NULL' if self.nullable else 'NOT NULL'}")


class ColumnType(ASTNode):
    def __init__(self, data_type, sparse=False, nullable=None):
        self.data_type = data_type
        self.sparse = sparse
        self.nullable = nullable

    def print(self, spacer="  ", level=0):
        print(spacer * level, "Column Type")
        self.data_type.print(spacer, level + 1)
        if self.sparse:
            print(spacer * level, "Sparse")
        if self.nullable:
            self.nullable.print(spacer, level + 1)


class DataType(ASTNode):
    def __init__(self, name, params=None):
        self.name = name
        self.params = params

    def print(self, spacer="  ", level=0):
        print(spacer * level, f"DataType:  {self.name}")
        if self.params:
            self.params.print(spacer, level + 1)


class ParenLiteralMax(ASTNode):
    def __init__(self, value, is_max=False):
        self.value = value
        self.is_max = is_max

    def print(self, spacer="  ", level=0):
        if self.is_max:
            print(spacer * level, "MAX")
        else:
            self.value.print(spacer, level + 1)
