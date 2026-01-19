from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
# from ..ast_nodes.basic_nodes import ItemsList
# from ..ast_nodes.truncate_nodes import *
#
#
class AlterVisitor(SQLParserVisitor):
    pass
#
#     def visitAlter_table(self, ctx: SQLParser.Alter_tableContext):
#         table = self.visit(ctx.full_table_name())
#         table_actions = self.visit(ctx.table_action_list())
#         return AlterTableStatement(table, table_actions)
#
#     def visitTable_action_list(self, ctx:SQLParser.Table_action_listContext):
#         return ItemsList([self.visit(action) for action in ctx.table_action()])
#
#
#     def visitTable_alter_column(self, ctx:SQLParser.Table_alter_columnContext):
#         column_name = self.visit(ctx.alter_column_action())
#         column_action = self.visit(ctx.alter_column_action())
#         return TableAlterColumnAction(column_name, column_action)
#
#     def visitAlter_column_action(self, ctx:SQLParser.Alter_column_actionContext):
#     def visitAlter_view(self, ctx: SQLParser.Alter_viewContext):
#         table = self.visit(ctx.full_table_name())
#         columns = self.visit(ctx.column_list()) if ctx.column_list() else None
#         view_attribute = self.visit(ctx.view_attribute()) if ctx.view_attribute() else None
#         select_st = self.visit(ctx.select_statement())
#         view_check_option = self.visit(ctx.view_check_option()) if ctx.view_check_option() else None
#         return AlterViewStatement(table, columns, view_attribute, select_st, view_check_option)
#
#
#
