from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.basic_nodes import ItemsList, SingleValueNode
from sql_ast.ast_nodes.create_nodes import *

class CreateVisitor(SQLParserVisitor):

    def visitCreate_table(self, ctx:SQLParser.Create_tableContext):
        full_table_name = self.visit(ctx.full_table_name())
        create_table_element_list = self.visit(ctx.create_table_body())
        table_on_clause = self.visit(ctx.table_on_clause()) if ctx.table_on_clause() else None
        table_with_clause = self.visit(ctx.table_with_clause()) if ctx.table_with_clause() else None

        return CreateTable(full_table_name, create_table_element_list, table_on_clause, table_with_clause)

    def visitCreate_table_body(self, ctx:SQLParser.Create_table_bodyContext):
        return self.visit(ctx.create_table_element_list())

    def visitCreate_table_element_list(self, ctx:SQLParser.Create_table_element_listContext):
        return ItemsList([self.visit(child) for child in ctx.create_table_element()])

    def visitColumn_set_definition(self, ctx:SQLParser.Column_set_definitionContext):
        return SingleValueNode(ctx.getText())

    def visitTable_index(self, ctx:SQLParser.Table_indexContext):
        index_name = ctx.index_name().getText()
        body = self.visit(ctx.table_index_body())
        return TableIndex(index_name, body)

    def visitTable_index_rowstore(self, ctx:SQLParser.Table_index_rowstoreContext):
        unique = ctx.UNIQUE() is not None
        clustered = ctx.CLUSTERED() is not None
        cols = ItemsList([self.visit(c) for c in ctx.index_column()])
        include_clause = self.visit(ctx.include_clause()) if ctx.include_clause() else None
        where_clause_for_index = self.visit(ctx.where_clause_for_index()) if ctx.where_clause_for_index() else None
        index_with_clause = self.visit(ctx.index_with_clause()) if ctx.index_with_clause() else None
        index_on_clause = self.visit(ctx.index_on_clause()) if ctx.index_on_clause() else None
        return TableIndexRowstore(unique, clustered, cols, include_clause, where_clause_for_index, index_with_clause, index_on_clause)

    def visitTable_index_columnstore(self, ctx:SQLParser.Table_index_columnstoreContext):
        column_store = ctx.COLUMNSTORE() is not None
        clustered = ctx.CLUSTERED() is not None
        cols = ItemsList([self.visit(c) for c in ctx.index_column()])
        include_clause = self.visit(ctx.include_clause()) if ctx.include_clause() else None
        where_clause_for_index = self.visit(ctx.where_clause_for_index()) if ctx.where_clause_for_index() else None
        index_with_clause = self.visit(ctx.index_with_clause()) if ctx.index_with_clause() else None
        index_on_clause = self.visit(ctx.index_on_clause()) if ctx.index_on_clause() else None
        return TableIndexRowstore(column_store, clustered, cols, include_clause, where_clause_for_index, index_with_clause, index_on_clause)

    def visitIndex_column(self, ctx:SQLParser.Index_columnContext):
        name = self.visit(ctx.full_column_name())
        order = "DESC" if ctx.DESC() else "ASC"
        return IndexColumn(name, order)

    def visitCreate_index(self, ctx:SQLParser.Create_indexContext):
        index_clustering = self.visit(ctx.index_clustering()) if ctx.index_clustering() else None
        index_name = ctx.index_name().getText()
        full_table_name = self.visit(ctx.full_table_name())
        unique = ctx.UNIQUE() is not None
        columnstore = ctx.COLUMNSTORE() is not None
        clustered = ctx.index_clustering() and ctx.index_clustering().CLUSTERED() is not None
        
        cols = self.visit(ctx.index_column_list()) if ctx.index_column_list() else None
        
        return CreateIndex(index_name, full_table_name, cols, unique=unique, clustered=clustered, columnstore=columnstore)

    def visitIndex_column_list(self, ctx:SQLParser.Index_column_listContext):
        return ItemsList([self.visit(c) for c in ctx.index_column()])

    def visitCreate_view(self, ctx:SQLParser.Create_viewContext):
        name = self.visit(ctx.full_table_name())
        select = self.visit(ctx.select_statement())
        return CreateView(name, select)

    def visitCreate_user(self, ctx:SQLParser.Create_userContext):
        name = self.visit(ctx.user_name())
        return CreateUser(name)

    def visitCreate_login(self, ctx:SQLParser.Create_loginContext):
        name = SingleValueNode(ctx.login_name().getText())
        return CreateLogin(name, SingleValueNode("login_core"))

    def visitGrant_statement(self, ctx:SQLParser.Grant_statementContext):
        target = self.visit(ctx.grant_target())
        grantee = self.visit(ctx.full_table_name())
        return GrantStatement("IMPERSONATE", target, grantee)

    def visitGrant_target(self, ctx:SQLParser.Grant_targetContext):
        return SingleValueNode(ctx.getText())

    def visitCreate_function(self, ctx:SQLParser.Create_functionContext):
        name = SingleValueNode(ctx.function_name().getText())
        or_alter = ctx.ALTER() is not None
        return CreateFunction(name, None, SingleValueNode("type"), SingleValueNode("body"), or_alter=or_alter)
