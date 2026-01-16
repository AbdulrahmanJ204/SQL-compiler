from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.statements import *
from ..ast_nodes.expressions import *
from ..ast_nodes.basic import *

class BasicVisitor(SQLParserVisitor):
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

    def visitFull_table_name(self, ctx: SQLParser.Full_table_nameContext):
        parts = [identifier.getText() for identifier in ctx.IDENTIFIER()]
        return TableRef(parts)

    def visitFull_column_name(self, ctx: SQLParser.Full_column_nameContext):
        parts = [ctx.getChild(0).getText()]
        for ident in ctx.IDENTIFIER()[1:]:
            parts.append(ident.getText())
        return ColumnRef(parts)

    def visitDerived_table(self, ctx: SQLParser.Derived_tableContext):
        return self.visit(ctx.select_statement())
