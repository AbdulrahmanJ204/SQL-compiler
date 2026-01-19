
from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.truncate_nodes import *
class TruncateVisitor(SQLParserVisitor):
    def visitTruncate_statement(self, ctx:SQLParser.Truncate_statementContext):
        table = self.visit(ctx.full_table_name())
        with_partitions = self.visit(ctx.with_partition_number_expression()) if ctx.with_partition_number_expression() else None

        return TruncateStatement(table=table, with_partitions=with_partitions)