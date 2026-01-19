
from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.basic_nodes import Variable, Literal
from ..ast_nodes.expression_nodes import *

class ExpressionVisitor(SQLParserVisitor):
    def visitOr_expression(self, ctx: SQLParser.Or_expressionContext):
        expr = self.visit(ctx.and_expression(0))
        for i in range(1, len(ctx.and_expression())):
            right_side = self.visit(ctx.and_expression(i))
            expr = OrExpression(expr, right_side)
        return expr

    def visitAnd_expression(self, ctx: SQLParser.And_expressionContext):
        expr = self.visit(ctx.not_expression(0))
        for i in range(1, len(ctx.not_expression())):
            right_side = self.visit(ctx.not_expression(i))
            expr = AndExpression(expr, right_side)
        return expr

    def visitNot_expression(self, ctx: SQLParser.Not_expressionContext):
        if ctx.NOT():
            expr = self.visit(ctx.not_expression())
            return NotExpression(expr)

        return self.visit(ctx.predicate_expression())

    def visitPredicate_expression(self, ctx: SQLParser.Predicate_expressionContext):
        if ctx.search_condition():
            return self.visit(ctx.search_condition())
        return self.visit(ctx.predicate())

    # no override for predicate

    def visitPredicate(self, ctx: SQLParser.PredicateContext):
        return self.visit(ctx.getChild(0))

    def visitComparison_predicate(self, ctx: SQLParser.Comparison_predicateContext):

        expr = self.visit(ctx.expression(0))

        operators = self.visit(ctx.operators())  # TODO : Could be only getText()
        if ctx.expression(1):
            right = self.visit(ctx.expression(1))
        else:
            right = self.visit(ctx.quantified_subquery())

        return ComparisonExpression(expr, operators, right)

    def visitQuantified_subquery(self, ctx: SQLParser.Quantified_subqueryContext):
        select_st = self.visit(ctx.select_statement())
        quantifier = ctx.getChild(0).getText()

        return QuantifiedSubquery(quantifier, select_st)


    def visitIn_predicate(self, ctx: SQLParser.In_predicateContext):
        expr = self.visit(ctx.expression())
        negated = ctx.NOT() is not None
        if ctx.in_list():
            items = self.visit(ctx.in_list())
        else:
            items = self.visit(ctx.select_statement())

        return InExpression(expr, items, negated)

    def visitIn_list(self, ctx: SQLParser.In_listContext):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitBetween_predicate(self, ctx: SQLParser.Between_predicateContext):
        expr = self.visit(ctx.expression(0))
        negated = ctx.NOT() is not None
        expr1 = self.visit(ctx.expression(1))
        expr2 = self.visit(ctx.expression(2))
        return BetweenExpression(expr, expr1, expr2, negated)

    def visitLike_predicate(self, ctx: SQLParser.Like_predicateContext):
        value = self.visit(ctx.expression(0))
        negated = ctx.NOT() is not None
        pattern = self.visit(ctx.expression(1))
        return LikeExpression(value, pattern, negated)

    def visitNull_predicate(self, ctx: SQLParser.Null_predicateContext):
        expr = self.visit(ctx.expression())
        negated = ctx.NOT() is not None
        return NullCheck(expr, negated)

    def visitExists_predicate(self, ctx: SQLParser.Exists_predicateContext):
        negated = ctx.NOT() is not None
        subquery = self.visit(ctx.derived_table())
        return ExistsExpression(subquery, negated)


    # no override for expression

    def visitOr_bitwise_expression(self, ctx: SQLParser.Or_bitwise_expressionContext):
        expr = self.visit(ctx.xor_bitwise_expression(0))
        for i in range(1, len(ctx.xor_bitwise_expression())):
            right_side = self.visit(ctx.xor_bitwise_expression(i))
            expr = OrBitwiseExpression(expr, right_side)
        return expr

    def visitXor_bitwise_expression(self, ctx: SQLParser.Xor_bitwise_expressionContext):
        expr = self.visit(ctx.and_bitwise_expression(0))
        for i in range(1, len(ctx.and_bitwise_expression())):
            right_side = self.visit(ctx.and_bitwise_expression(i))
            expr = XorBitwiseExpression(expr, right_side)

        return expr

    def visitAnd_bitwise_expression(self, ctx: SQLParser.And_bitwise_expressionContext):
        expr = self.visit(ctx.add_sub_expression(0))
        for i in range(1, len(ctx.add_sub_expression())):
            right_side = self.visit(ctx.add_sub_expression(i))
            expr = AndBitwiseExpression(expr, right_side)

        return expr

    def visitAdd_sub_expression(self, ctx: SQLParser.Add_sub_expressionContext):
        expr = self.visit(ctx.mul_div_expression(0))
        for i in range(1, len(ctx.mul_div_expression())):
            op = ctx.children[2 * i - 1].getText()
            right_side = self.visit(ctx.mul_div_expression(i))
            if op == "+":
                expr = AddExpression(expr, right_side)
            elif op == "-":
                expr = SubExpression(expr, right_side)

        return expr

    def visitMul_div_expression(self, ctx: SQLParser.Mul_div_expressionContext):
        expr = self.visit(ctx.unary_expression(0))
        for i in range(1, len(ctx.unary_expression())):
            right_side = self.visit(ctx.unary_expression(i))
            operator = ctx.children[2 * i - 1].getText()
            if operator == "%":
                expr = ModExpression(expr, right_side)
            elif operator == "*":
                expr = MulExpression(expr, right_side)
            elif operator == "/":
                expr = DivExpression(expr, right_side)

        return expr

    def visitUnary_expression(self, ctx: SQLParser.Unary_expressionContext):
        expr = self.visit(ctx.primary_expression())
        for i in range(len(ctx.children) - 2, -1, -1):
            op = ctx.children[i].getText()
            expr = UnaryExpression(op, expr)

        return expr

    def visitPrimary_expression(self, ctx: SQLParser.Primary_expressionContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.full_column_name():
            return self.visit(ctx.full_column_name())
        elif ctx.USER_VARIABLE():
            return Variable(ctx.USER_VARIABLE().getText())
        elif ctx.SYSTEM_VARIABLE():
            return Variable(ctx.SYSTEM_VARIABLE().getText())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.NULL():
            return Literal(ctx.NULL().getText())
        elif ctx.derived_table():
            return self.visit(ctx.derived_table())
        elif ctx.datatype():
            return self.visit(ctx.datatype())
        else:
            raise NotImplementedError(
                f"Unsupported primary_expression: {ctx.getText()}"
            )
