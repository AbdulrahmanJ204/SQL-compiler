import time

from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.select_nodes import *


class SelectVisitor(SQLParserVisitor):

    def visitSelect_statement(self, ctx: SQLParser.Select_statementContext):
        query_expression = self.visit(ctx.query_expression())
        with_cte = self.visit(ctx.with_cte()) if ctx.with_cte() else None
        order_by = self.visit(ctx.order_by_clause()) if ctx.order_by_clause() else None
        return SelectStatement(query_expression, with_cte, order_by)

    def visitQuery_expression(self, ctx: SQLParser.Query_expressionContext):
        if ctx.LPAREN():
            left = self.visit(ctx.query_expression())
        else:
            left = self.visit(ctx.query_specification())
        operations = self.visit(ctx.set_operators_list()) if ctx.set_operators_list() else None

        return QueryExpression(left, operations)

    def visitSet_operators_list(self, ctx: SQLParser.Set_operators_listContext):
        lst = []
        for i, st_op in enumerate(ctx.set_operators()):
            qu = self.visit(ctx.query_specification(i))
            lst.append(SelectSetOperation(self.visit(st_op), qu))
        return SelectSetOperationsList(lst)

    def visitQuery_specification(self, ctx: SQLParser.Query_specificationContext):
        modifier = self.visit(ctx.select_modifier())
        select_list = self.visit(ctx.select_list())
        into = self.visit(ctx.full_table_name()) if ctx.INTO() else None
        from_table_source = self.visit(ctx.table_source_list()) if ctx.FROM() else None
        where = self.visit(ctx.where_clause()) if ctx.where_clause() else None
        group_by = self.visit(ctx.group_by_clause()) if ctx.group_by_clause() else None
        having_clause = self.visit(ctx.having_clause()) if ctx.having_clause() else None
        return QuerySpecification(modifier, select_list, into, from_table_source, where, group_by, having_clause)

    def visitSelect_modifier(self, ctx: SQLParser.Select_modifierContext):

        top = self.visit(ctx.select_top_clause()) if ctx.select_top_clause() else None

        quantifier = None
        if ctx.DISTINCT():
            quantifier = "DISTINCT"
        elif ctx.ALL():
            quantifier = "ALL"

        return SelectQuantifier(quantifier, top)

    def visitSelect_list(self, ctx: SQLParser.Select_listContext):
        return SelectList([self.visit(item_ctx) for item_ctx in ctx.select_list_item()])



    def visitSelect_list_item(self, ctx:SQLParser.Select_list_itemContext):
        if ctx.DOT():
            return TableStarSelectItem(self.visit(ctx.full_table_name()))
        elif ctx.STAR():
            return Star()
        return self.visit(ctx.select_list_element())


    def visitSelect_list_element(self, ctx: SQLParser.Select_list_elementContext):
        if ctx.expression_alias():
            return self.visit(ctx.expression_alias())

        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return AssignmentSelectItem(left, op, right)

    def visitTop_count(self, ctx: SQLParser.Top_countContext):
        return self.visit(ctx.expression())

    def visitSelect_top_clause(self, ctx: SQLParser.Select_top_clauseContext):
        value = self.visit(ctx.top_count())
        percent = ctx.PERCENT() is not None
        return TopSpec(value, percent)
