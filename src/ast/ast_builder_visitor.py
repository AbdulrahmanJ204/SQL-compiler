from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from .program import Program
from .statements import PrintStatement, DeleteStatement, WhereClause
from .expressions import Literal, Variable, BinaryExpression, UnaryExpression, ComparisonExpression, QuantifiedSubquery, \
    BetweenExpression, LikeExpression, NullCheck, ExistsExpression, InExpression
from .table import Table


class ASTBuilderVisitor(SQLParserVisitor):
    def visitProgram(self, ctx: SQLParser.ProgramContext):
        statements = []
        for statement_ctx in ctx.statement():
            statement = self.visit(statement_ctx)
            if statement is not None:
                statements.append(statement)

        return Program(statements)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitPrint_clause(self, ctx: SQLParser.Print_clauseContext):
        value = None
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.USER_VARIABLE():
            value = Variable(ctx.USER_VARIABLE().getText())

        return PrintStatement(value)

    def visitDelete_statement(self, ctx: SQLParser.Delete_statementContext):
        table_ctx = ctx.table_source()
        table_name = table_ctx.getText()
        table = Table(table_name)

        where = None
        if ctx.delete_and_update_where_clause():
            where = self.visit(ctx.delete_and_update_where_clause())

        top = None
        if ctx.top_clause():
            top = self.visit(ctx.top_clause())

        return DeleteStatement(table, where, top)


    ###################################################################
    #             ExpressionParser Visit.
    ###################################################################

    def visitSearch_condition(self, ctx: SQLParser.Search_conditionContext):
        return self.visit(ctx.or_expression())

    def visitOr_expression(self, ctx: SQLParser.Or_expressionContext):
        expr = self.visit(ctx.and_expression(0))
        for i in range(1, len(ctx.and_expression())):
            right_side = self.visit(ctx.and_expression(i))
            expr = BinaryExpression(expr, "OR", right_side)
        return expr

    def visitAnd_expression(self, ctx: SQLParser.And_expressionContext):
        expr = self.visit(ctx.not_expression(0))
        for i in range(1, len(ctx.not_expression())):
            right_side = self.visit(ctx.not_expression(i))
            expr = BinaryExpression(expr, "AND", right_side)

        return expr

    def visitNot_expression(self, ctx: SQLParser.Not_expressionContext):
        if ctx.NOT():
            operand = self.visit(ctx.not_expression())
            return UnaryExpression("NOT", operand)

        return self.visit(ctx.predicate_expression())

    def visitPredicate_expression(self, ctx: SQLParser.Predicate_expressionContext):
        if ctx.search_condition():
            return self.visit(ctx.search_condition())
        return self.visit(ctx.predicate())

    def visitPredicate(self, ctx: SQLParser.PredicateContext):
        if ctx.comparison_predicate():
            return self.visit(ctx.comparison_predicate())
        elif ctx.in_predicate():
            return self.visit(ctx.in_predicate())
        elif ctx.between_predicate():
            return self.visit(ctx.between_predicate())
        elif ctx.like_predicate():
            return self.visit(ctx.like_predicate())
        elif ctx.null_predicate():
            return self.visit(ctx.null_predicate())

        return self.visit(ctx.exists_predicate())

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

    def visitOperators(self, ctx: SQLParser.OperatorsContext):
        return ctx.getChild(0).getText()

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
        expr = self.visit(ctx.expression())
        negated = ctx.NOT() is not None
        expr1 = self.visit(ctx.expression(1))
        expr2 = self.visit(ctx.expression(2))
        return BetweenExpression(expr, expr1, expr2, negated)

    def visitLike_predicate(self, ctx: SQLParser.Like_predicateContext):
        value = self.visit(ctx.expression(0))
        negated = ctx.NOT() is not None
        pattern = self.visit(ctx.expression(1))
        return LikeExpression(value, pattern, negated)


    def visitNull_predicate(self, ctx:SQLParser.Null_predicateContext):
        expr= self.visit(ctx.expression())
        negated = ctx.NOT() is not None
        return NullCheck(expr, negated)


    def visitExists_predicate(self, ctx:SQLParser.Exists_predicateContext):
        negated = ctx.NOT() is not None
        subquery = self.visit(ctx.derived_table())
        return ExistsExpression(subquery, negated)

    # Expression
    def visitExpression(self, ctx: SQLParser.ExpressionContext):
        return self.visit(ctx.or_bitwise_expression())

    def visitOr_bitwise_expression(self, ctx: SQLParser.Or_bitwise_expressionContext):
        expr = self.visit(ctx.xor_bitwise_expression(0))
        for i in range(1, len(ctx.xor_bitwise_expression())):
            right_side = self.visit(ctx.xor_bitwise_expression(i))
            expr = BinaryExpression(expr, "|", right_side)
        return expr

    def visitXor_bitwise_expression(self, ctx: SQLParser.Xor_bitwise_expressionContext):
        expr = self.visit(ctx.and_bitwise_expression(0))
        for i in range(1, len(ctx.and_bitwise_expression())):
            right_side = self.visit(ctx.and_bitwise_expression(i))
            expr = BinaryExpression(expr, "^", right_side)

        return expr

    def visitAnd_bitwise_expression(self, ctx: SQLParser.And_bitwise_expressionContext):
        expr = self.visit(ctx.add_sub_expression(0))
        for i in range(1, len(ctx.add_sub_expression())):
            right_side = self.visit(ctx.add_sub_expression(i))
            expr = BinaryExpression(expr, "&", right_side)

        return expr

    def visitAdd_sub_expression(self, ctx: SQLParser.Add_sub_expressionContext):
        expr = self.visit(ctx.mul_div_expression(0))
        for i in range(1, len(ctx.mul_div_expression())):
            op = ctx.children[2 * i - 1].getText()
            right_side = self.visit(ctx.mul_div_expression(i))
            expr = BinaryExpression(expr, op, right_side)

        return expr

    def visitMul_div_expression(self, ctx: SQLParser.Mul_div_expressionContext):
        expr = self.visit(ctx.unary_expression(0))
        for i in range(1, len(ctx.unary_expression())):
            right_side = self.visit(ctx.unary_expression(i))
            operator = ctx.children[2 * i - 1].getText()

            expr = BinaryExpression(expr, operator, right_side)

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
            return self.visit(ctx.full_column_name())  # TODO : Could be node , check this
        elif ctx.USER_VARIABLE():
            return Variable(ctx.USER_VARIABLE().getText())
        elif ctx.SYSTEM_VARIABLE():
            return Variable(ctx.SYSTEM_VARIABLE().getText())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.NULL():
            return Literal("NULL")  # TODO : Check this
        elif ctx.derived_table():
            return self.visit(ctx.derived_table())
        else:
            raise NotImplementedError(
                f"Unsupported primary_expression: {ctx.getText()}"
            )
    # ! END OF ExpressionParser
