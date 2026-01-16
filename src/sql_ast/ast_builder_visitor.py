from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.program import Program
from sql_ast.ast_nodes.statements import DeleteStatement, WhereClause, SetStatement, StatementBlock
from sql_ast.ast_nodes.expressions import Literal
from sql_ast.ast_nodes.basic import Table, TableRef, ColumnRef
from sql_ast.visitors.basic_visitor import BasicVisitor
from sql_ast.visitors.expression_visitor import ExpressionVisitor


class ASTBuilderVisitor(ExpressionVisitor , BasicVisitor):
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

