from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from .program import Program
from .statements import PrintStatement, DeleteStatement, WhereClause, SetStatement, StatementBlock
from .expressions import Literal, Variable, UnaryExpression, ComparisonExpression, QuantifiedSubquery, \
    BetweenExpression, LikeExpression, NullCheck, ExistsExpression, InExpression, NotExpression, OrExpression, \
    AndExpression, OrBitwiseExpression, XorBitwiseExpression, AndBitwiseExpression, AddExpression, SubExpression, \
    MulExpression, DivExpression, ModExpression
from .basic import Table, TableRef, ColumnRef


class ASTBuilderVisitor(SQLParserVisitor):
    ###################################################################
    #             SQLParser Visit.
    ###################################################################

    def visitProgram(self, ctx: SQLParser.ProgramContext):
        statements = []
        for statement_ctx in ctx.statement():
            statement = self.visit(statement_ctx)
            if statement is not None:
                statements.append(statement)

        return Program(statements)

    # no override for ddl
    # no override for dml
    # no override for variable_statement
    # no override for cursor_statement
    # no override for statement

    def visitSet_statement(self, ctx: SQLParser.Set_statementContext):
        on = True if ctx.ON() else False
        table = self.visit(ctx.full_table_name())
        return SetStatement(table, on)

    ###################################################################
    #             ! END OF SQLParser Visit.
    ###################################################################

    def visitDelete_statement(self, ctx: SQLParser.Delete_statementContext):
        # TODO : reconstruct this.
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
    #             BasicParser Visitor.
    ###################################################################
    def visitStatement_block(self, ctx: SQLParser.Statement_blockContext):
        statements = [self.visit(statement) for statement in ctx.statement()]
        return StatementBlock(statements)

    def visitWhere_clause(self, ctx):
        condition = self.visit(ctx.search_condition())
        return WhereClause(condition)

    def visitDelete_and_update_where_clause(self, ctx: SQLParser.Delete_and_update_where_clauseContext):
        if ctx.where_clause():
            return self.visit(ctx.where_clause())
        cursor = ctx.cursor_name().getText()
        # TODO : Check Cursor Name
        return WhereClause(
            Literal(f"CURRENT OF {cursor}")
        )

    def visitJoin_clause(self, ctx: SQLParser.Join_clauseContext):
        join_type = ctx.join_type().getText()
        table = self.visit(ctx.table_source_item())
        join_condition = self.visit(ctx.join_condition())
        # TODO : Should Return Join Node
        return ""

    def visitHaving_clause(self, ctx: SQLParser.Having_clauseContext):
        condition = self.visit(ctx.search_condition())
        # TODO : Should Return Having Node
        return "Having Node"

    def visitLiteral(self, ctx: SQLParser.LiteralContext):
        return Literal(ctx.getText())

    ###################################################################
    #             BasicParser Visit.
    ###################################################################

    def visitFull_table_name(self, ctx: SQLParser.Full_table_nameContext):
        parts = [identifier.getText() for identifier in ctx.IDENTIFIER()]
        return TableRef(parts)

    def visitFull_column_name(self, ctx: SQLParser.Full_column_nameContext):
        parts = [ctx.getChild(0).getText()]
        for ident in ctx.IDENTIFIER()[1:]:
            parts.append(ident.getText())
        return ColumnRef(parts)

    def visitDerived_table(self, ctx:SQLParser.Derived_tableContext):
        return self.visit(ctx.select_statement())
    ###################################################################
    #             ExpressionParser Visit.
    ###################################################################

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
    def visitPredicate(self, ctx:SQLParser.PredicateContext):
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

    def visitOperators(self, ctx: SQLParser.OperatorsContext):
        return ctx.getText()

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
        else:
            raise NotImplementedError(
                f"Unsupported primary_expression: {ctx.getText()}"
            )


    # ! END OF ExpressionParser
