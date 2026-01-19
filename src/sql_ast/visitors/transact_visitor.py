from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.basic_nodes import ItemsList, SingleValueNode
from ..ast_nodes.control_flow_nodes import *
from ..ast_nodes.transact_nodes import *

class TransactVisitor(SQLParserVisitor):

    def visitBegin_ditributed_transaction(self, ctx: SQLParser.Begin_ditributed_transactionContext):
        name = self.visit(ctx.transaction_name()) if ctx.transaction_name() else None
        return BeginDistributedTransactionNode(name=name)

    def visitBegin_transaction(self, ctx: SQLParser.Begin_transactionContext):
        return BeginTransactionNode(
            self.visit(ctx.transaction_name_with_mark_clause()) if ctx.transaction_name_with_mark_clause() else None)

    def visitTransaction_name_with_mark_clause(self, ctx: SQLParser.Transaction_name_with_mark_clauseContext):
        name = self.visit(ctx.transaction_name())
        mark_clause = self.visit(ctx.with_mark_clause()) if ctx.with_mark_clause() else None
        return TransactionNameWithMarkClauseNode(name=name, mark_clause=mark_clause)

    def visitWith_mark_clause(self, ctx: SQLParser.With_mark_clauseContext):
        literal = ctx.STRING_LITERAL().getText() if ctx.STRING_LITERAL() else None
        if ctx.UNICODE_STRING_LITERAL():
            literal = ctx.UNICODE_STRING_LITERAL().getText()

        return WithMarkClauseNode(literal)

    def visitCommit_transaction(self, ctx:SQLParser.Commit_transactionContext):
        name = self.visit(ctx.transaction_name()) if ctx.transaction_name() else None
        with_delay_durabilty = self.visit(ctx.with_delay_durability_clause()) if ctx.with_delay_durability_clause() else None
        return CommitTransactionNode(name=name, with_delay_durability=with_delay_durabilty)

    def visitWith_delay_durability_clause(self, ctx:SQLParser.With_delay_durability_clauseContext):
        return WithDelayDurabilityClauseNode(ctx.ON() is not None)


    def visitCommit_work(self, ctx:SQLParser.Commit_workContext):
        return CommitWorkNode()

    def visitSave_transaction(self, ctx:SQLParser.Save_transactionContext):
        name = self.visit(ctx.transaction_name())
        return SaveTransactionNode(name=name)


    def visitRollback_transaction(self, ctx:SQLParser.Rollback_transactionContext):
        name = self.visit(ctx.transaction_name()) if ctx.transaction_name() else None
        return RollbackTransactionNode(name=name)

    def visitRollback_work(self, ctx:SQLParser.Rollback_workContext):
        return RollbackWorkNode()

    def visitTransaction_name(self, ctx: SQLParser.Transaction_nameContext):
        return SingleValueNode(value=ctx.getText())
