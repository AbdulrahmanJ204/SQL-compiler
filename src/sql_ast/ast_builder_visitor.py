from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.program import Program
from sql_ast.ast_nodes.statements import  SetStatement, SetOption

from sql_ast.ast_nodes.basic_nodes import Table, ColumnOrTable, ItemsList, SingleValueNode
from sql_ast.visitors.alter_visitor import AlterVisitor
from sql_ast.visitors.basic_visitor import BasicVisitor
from sql_ast.visitors.control_flow_visitor import ControlFlowVisitor
from sql_ast.visitors.create_visitor import CreateVisitor
from sql_ast.visitors.cursor_visitor import CursorVisitor
from sql_ast.visitors.delete_visitor import DeleteVisitor
from sql_ast.visitors.drop_visitor import DropVisitor
from sql_ast.visitors.expression_visitor import ExpressionVisitor
from sql_ast.visitors.insert_visitor import InsertVisitor
from sql_ast.visitors.output_visitor import OutputVisitor
from sql_ast.visitors.select_visitor import SelectVisitor
from sql_ast.visitors.transact_visitor import TransactVisitor
from sql_ast.visitors.truncate_visitor import TruncateVisitor
from sql_ast.visitors.update_visitor import UpdateVisitor
from sql_ast.visitors.variable_visitor import VariableVisitor


class ASTBuilderVisitor(ExpressionVisitor, BasicVisitor, SelectVisitor, CursorVisitor, TruncateVisitor, AlterVisitor,
                        VariableVisitor, InsertVisitor, UpdateVisitor, TransactVisitor, ControlFlowVisitor, OutputVisitor, DeleteVisitor,
                        DropVisitor, CreateVisitor):    ###################################################################
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
        return self.visit(ctx.set_options())

    def visitIdentity_insert(self, ctx: SQLParser.Identity_insertContext):
        on = ctx.ON() is not None
        table = self.visit(ctx.full_table_name())
        return SetStatement(table, on, True)

    def visitSet_options_list(self, ctx: SQLParser.Set_options_listContext):

        on = ctx.ON() is not None
        lst = self.visit(ctx.set_option_name_list())
        return SetStatement(lst, on)

    def visitSet_option_name_list(self, ctx: SQLParser.Set_option_name_listContext):
        return ItemsList([self.visit(child) for child in ctx.set_option_name()])

    def visitSet_option_name(self, ctx: SQLParser.Set_option_nameContext):
        return SetOption(ctx.getText())