from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.basic_nodes import UserVariable, DefaultValue, ArgumentList, AssignmentList
from sql_ast.ast_nodes.insert_nodes import InsertedUpdatedValue
from sql_ast.ast_nodes.update_nodes import UpdateStatementNode, UpdateNormalAssignment, UpdateUdtMethodAssignment, \
    UpdateWriteAssignment


class UpdateVisitor(SQLParserVisitor):
    def visitUpdate_statement(self, ctx:SQLParser.Update_statementContext):
        with_cte = self.visit(ctx.with_cte()) if ctx.with_cte() else None
        top_clause = self.visit(ctx.top_clause()) if ctx.top_clause() else None
        table_or_variable = self.visit(ctx.full_table_name()) if ctx.full_table_name() else UserVariable(ctx.USER_VARIABLE().getText())
        assignment_list = self.visit(ctx.assignment_list())
        output_clause = self.visit(ctx.output_clause()) if ctx.output_clause() else None
        table_source_list = self.visit(ctx.table_source_list()) if ctx.table_source_list() else None
        delete_and_update_where_clause = self.visit(ctx.delete_and_update_where_clause()) if ctx.delete_and_update_where_clause() else None

        return UpdateStatementNode(with_cte, top_clause, table_or_variable, assignment_list, output_clause, table_source_list, delete_and_update_where_clause)


    def visitAssignment_list(self, ctx:SQLParser.Assignment_listContext):
        return AssignmentList([self.visit(assignment) for assignment in ctx.assignment()])

    def visitNormal_assignment(self, ctx:SQLParser.Normal_assignmentContext):
        target = self.visit(ctx.target())
        assignment_operator = ctx.assignment_operator().getText()
        source = self.visit(ctx.source())
        return UpdateNormalAssignment(target, assignment_operator, source)

    def visitSource(self, ctx:SQLParser.SourceContext):
        return DefaultValue(ctx.DEFAULT()) if ctx.DEFAULT() else  InsertedUpdatedValue(self.visit(ctx.expression()))

    def visitTarget(self, ctx:SQLParser.TargetContext):
        column_or_variable = self.visit(ctx.full_column_name()) if ctx.full_column_name() else UserVariable(ctx.USER_VARIABLE().getText())
        return column_or_variable

    def visitWrite_assignment(self, ctx:SQLParser.Write_assignmentContext):
        column = self.visit(ctx.full_column_name())
        expression1 = self.visit(ctx.expression(0))
        expression2 = self.visit(ctx.expression(1))
        expression3 = self.visit(ctx.expression(2))
        return UpdateWriteAssignment(column, expression1,expression2,expression3)

    def visitUdt_method_assignment(self, ctx:SQLParser.Udt_method_assignmentContext):
        column = self.visit(ctx.full_column_name())
        identifier = ctx.IDENTIFIER().getText()
        argument_list = self.visit(ctx.argument_list()) if ctx.argument_list() else None
        return UpdateUdtMethodAssignment(column, identifier, argument_list)

    def visitArgument_list(self, ctx:SQLParser.Argument_listContext):
        return ArgumentList([self.visit(argument) for argument in ctx.expression()])