
from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.basic_nodes import ItemsList
from sql_ast.ast_nodes.drop_nodes import *

class DropVisitor(SQLParserVisitor):

    def visitDrop_statement(self, ctx:SQLParser.Drop_statementContext):
        return self.visit(ctx.drop_object())

    def visitDrop_table(self, ctx:SQLParser.Drop_tableContext):
        name = self.visit(ctx.full_table_name())
        exists =  ctx.if_exists() is not None
        return DropTable(name, exists)

    def visitDrop_view(self, ctx:SQLParser.Drop_viewContext):
        view_name_list = self.visit(ctx.view_name_list())
        exists =  ctx.if_exists() is not None
        return DropView(view_name_list, exists)

    def visitView_name_list(self, ctx:SQLParser.View_name_listContext):
        return ItemsList([self.visit(item_ctx) for item_ctx in ctx.full_table_name()])

    def visitDrop_user(self, ctx:SQLParser.Drop_userContext):
        user_name = self.visit(ctx.user_name())
        exists =  ctx.if_exists() is not None
        return DropUser(user_name, exists)

    def visitDrop_index(self, ctx:SQLParser.Drop_indexContext):
        return ItemsList([self.visit(item_ctx) for item_ctx in ctx.drop_index_item()])

    def visitDrop_index_item(self, ctx:SQLParser.Drop_index_itemContext):
        exists =  ctx.if_exists() is not None
        index_name = self.visit(ctx.index_name())
        full_table_name = self.visit(ctx.full_table_name())
        drop_index_with_clause = self.visit(ctx.drop_index_with_clause()) if ctx.drop_index_with_clause() else None

        return DropIndexItem(index_name, full_table_name, exists, drop_index_with_clause)

    def visitDrop_index_with_clause(self, ctx:SQLParser.Drop_index_with_clauseContext):
        return ItemsList([self.visit(item_ctx) for item_ctx in ctx.drop_index_option()])

    def visitMove_to_drop_move_target(self, ctx:SQLParser.Move_to_drop_move_targetContext):
        return self.visit(ctx.drop_move_target())

    def visitFilestream_drop_filestream_target(self, ctx:SQLParser.Filestream_drop_filestream_targetContext):
        return self.visit(ctx.drop_filestream_target())

    def visitDrop_function(self, ctx:SQLParser.Drop_functionContext):
        exists =  ctx.if_exists() is not None
        drop_function_name_list = self.visit(ctx.drop_function_name_list())

        return DropFunction(drop_function_name_list, exists)

    def visitDrop_function_name_list(self, ctx:SQLParser.Drop_function_name_listContext):
        return ItemsList([self.visit(item_ctx) for item_ctx in ctx.function_name()])

