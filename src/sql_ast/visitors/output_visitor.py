from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.basic_nodes import ItemsList, UserVariable
from ..ast_nodes.output_nodes import *

class OutputVisitor(SQLParserVisitor):

    def visitOutput_clause(self, ctx: SQLParser.Output_clauseContext):
        select_list = self.visit(ctx.output_select_list())
        into_clause = self.visit(ctx.output_into_clause()) if ctx.output_into_clause() else None
        return OutputStatement(select_list, into_clause)

    def visitOutput_select_list(self, ctx:SQLParser.Output_select_listContext):
        return ItemsList([self.visit(item_ctx) for item_ctx in ctx.output_select_list_item()])

    def visitId_dot_star_alias(self, ctx:SQLParser.Id_dot_star_aliasContext):
        type = ctx.getChild(0).getText()
        alias = self.visit(ctx.as_alias()) if ctx.as_alias() else None

        return OutputSelectListItem(type, alias)

    def visitOutput_into_clause(self, ctx:SQLParser.Output_into_clauseContext):
        if ctx.USER_VARIABLE():
            return UserVariable(ctx.USER_VARIABLE().getText())

        t_name = self.visit(ctx.full_table_name())
        column_list = self.visit(ctx.column_list()) if ctx.column_list() else None
        return OutputIntoClause(t_name, column_list)
