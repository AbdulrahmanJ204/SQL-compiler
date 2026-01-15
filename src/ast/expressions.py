from .ast_node import ASTNode


class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.value)


class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.name)


class BinaryExpression(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.operator)
        self.left.print(spacer , level + 1)
        self.right.print(spacer , level + 1)


class UnaryExpression(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.operator)
        self.operand.print(spacer, level + 1)


class ComparisonExpression(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.operator)
        self.left.print(spacer , level + 1)
        self.right.print(spacer , level + 1)


class QuantifiedSubquery(ASTNode):

    def __init__(self, quantifier, subquery):
        self.quantifier = quantifier
        self.subquery = subquery

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, self.quantifier)
        self.subquery.print(spacer , level + 1)


class InExpression(ASTNode):
    def __init__(self, value, items, negated=False):
        self.value = value
        self.items = items
        self.negated = negated

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level, " NOT IN " if self.negated else " IN ")
        self.value.print(spacer , level + 1)
        if isinstance(self.items, list):
            print(spacer * (level + 1) + " -- List")
            for item in self.items:
                item.print(spacer, level + 2)
        else:
            self.items.print(spacer , level + 1)


class BetweenExpression(ASTNode):
    def __init__(self, value , low , high , negated=False):
        self.value = value
        self.low = low
        self.high = high
        self.negated = negated

    def print(self, spacer="  ", level=0):
        to_print = " NOT BETWEEN " if self.negated else " BETWEEN "
        self.self_print(spacer * level, to_print)
        self.value.print(spacer, level + 1)
        self.low.print(spacer , level + 1)
        self.high.print(spacer ,level + 1)


class LikeExpression(ASTNode):
    def __init__(self, value, pattern, negated=False):
        self.value = value
        self.pattern = pattern
        self.negated = negated

    def print(self,spacer = "  ", level=0):
        to_print = " NOT Like " if self.negated else " LIKE "
        self.self_print(spacer * level, to_print)
        self.value.print(spacer , level + 1)
        self.pattern.print(spacer , level + 1)



class NullCheck(ASTNode):
    def __init__(self, value, negated=False):
        self.value = value
        self.negated = negated

    def print(self, spacer="  ", level=0):
        to_print = "NOT Null " if self.negated else " NOT "
        self.self_print(spacer * level, to_print)
        self.value.print(spacer , level + 1)


class ExistsExpression(ASTNode):

    def __init__(self, subquery, negated=False):
        self.subquery = subquery
        self.negated = negated

    def print(self, spacer="  ", level=0):
        to_print = "NOT EXISTS " if self.negated else " EXISTS "
        self.self_print(spacer * level, to_print)
        self.subquery.print(spacer , level + 1)
