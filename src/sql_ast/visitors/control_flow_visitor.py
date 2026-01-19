from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.basic_nodes import ItemsList
from ..ast_nodes.control_flow_nodes import *


class ControlFlowVisitor(SQLParserVisitor):
    def visitWhile_clause(self, ctx: SQLParser.While_clauseContext):
        search_condition = self.visit(ctx.search_condition())
        statements = ItemsList([self.visit(stmt) for stmt in ctx.statement()])
        return WhileClause(search_condition, statements)


    def visitIf_clause(self, ctx:SQLParser.If_clauseContext):
        condition = self.visit(ctx.search_condition())
        statements = ItemsList([self.visit(stmt) for stmt in ctx.statement()])
        else_clauses = self.visit(ctx.else_clause()) if ctx.else_clause() else None
        return IfClause(condition, statements, else_clauses)


    def visitElse_clause(self, ctx:SQLParser.Else_clauseContext):
        return ItemsList([self.visit(stmt) for stmt in ctx.statement()])

    def visitBreak_statement(self, ctx:SQLParser.Break_statementContext):
        return BreakStatement()

    def visitContinue_statement(self, ctx:SQLParser.Continue_statementContext):
        return ContinueStatement()
