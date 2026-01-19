from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.ast_node import ASTNode
from sql_ast.ast_nodes.basic_nodes import UserVariable, InsertRecordsList, InsertRecordValuesList, SingleValueNode, \
    DefaultValue
from sql_ast.ast_nodes.insert_nodes import InsertStatementNode, InsertedUpdatedValue


class InsertVisitor(SQLParserVisitor):

    def visitInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        with_cte = self.visit(ctx.with_cte()) if ctx.with_cte() else None
        top_clause = self.visit(ctx.top_clause()) if ctx.top_clause() else None
        table_or_variable = self.visit(ctx.full_table_name()) if ctx.full_table_name() else UserVariable(ctx.USER_VARIABLE().getText())
        column_list = self.visit(ctx.column_list()) if ctx.column_list() else None
        output_clause = self.visit(ctx.output_clause()) if ctx.output_clause() else None
        insert_source = self.visit(ctx.insert_source())

        return InsertStatementNode(with_cte, top_clause, table_or_variable, column_list, output_clause, insert_source)

    def visitValues_source(self, ctx:SQLParser.Values_sourceContext):
        return InsertRecordsList([self.visit(values_list) for values_list in ctx.values_list()])

    def visitValues_list(self, ctx:SQLParser.Values_listContext):
        return InsertRecordValuesList([self.visit(value) for value in ctx.value()])

    def visitValue(self, ctx:SQLParser.ValueContext):
        return DefaultValue(ctx.DEFAULT()) if ctx.DEFAULT() else  InsertedUpdatedValue(self.visit(ctx.expression()))

    def visitDefault_values(self, ctx:SQLParser.Default_valuesContext):
        return DefaultValue(ctx.getText())
