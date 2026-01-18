from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.program import Program
from sql_ast.ast_nodes.statements import DeleteStatement, SetStatement

from sql_ast.ast_nodes.basic_nodes import Table, ColumnOrTable
from sql_ast.visitors.basic_visitor import BasicVisitor
from sql_ast.visitors.cursor_visitor import CursorVisitor
from sql_ast.visitors.expression_visitor import ExpressionVisitor
from sql_ast.visitors.select_visitor import SelectVisitor
from sql_ast.visitors.truncate_visitor import TruncateVisitor


class ASTBuilderVisitor(ExpressionVisitor, BasicVisitor, SelectVisitor, CursorVisitor, TruncateVisitor):
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

    def visitDelete_statement(self, ctx: SQLParser.Delete_statementContext):
        # TODO : reconstruct this.
        table_ctx = ctx.table_source()
        table_name = table_ctx.getText()
        table = Table([table_name])

        where = None
        if ctx.delete_and_update_where_clause():
            where = self.visit(ctx.delete_and_update_where_clause())

        top = None
        if ctx.top_clause():
            top = self.visit(ctx.top_clause())

        return DeleteStatement(table, where, top)
