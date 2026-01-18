from PIL.DdsImagePlugin import item1

from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor

# from ..ast_nodes.expression_nodes import *
from ..ast_nodes.basic_nodes import *
from ..ast_nodes.select_nodes import TopSpec, Star


class BasicVisitor(SQLParserVisitor):
    # Statement Block
    def visitStatement_block(self, ctx: SQLParser.Statement_blockContext):
        statements = [self.visit(statement) for statement in ctx.statement()]
        return StatementBlock(statements)

    # Where
    def visitWhere_clause(self, ctx):
        condition = self.visit(ctx.search_condition())
        return WhereClause(condition)

    def visitDelete_and_update_where_clause(self, ctx: SQLParser.Delete_and_update_where_clauseContext):
        if ctx.where_clause():
            return self.visit(ctx.where_clause())
        cursor = self.visit(ctx.cursor_name())
        return WhereClause(
            cursor,
            is_cursor=True
        )

    # Having
    def visitHaving_clause(self, ctx: SQLParser.Having_clauseContext):
        return Having(self.visit(ctx.search_condition()))

    # Group By
    def visitGroup_by_clause(self, ctx: SQLParser.Group_by_clauseContext):
        with_ = None
        if ctx.WITH():
            with_ = ctx.getChild(-1).getText()

        items = self.visit(ctx.group_by_item_list())
        return GroupBy(items, with_)

    def visitGroup_by_item_list(self, ctx: SQLParser.Group_by_item_listContext):
        return [self.visit(expr) for expr in ctx.expression()]

    # Order By
    def visitOrder_by_clause(self, ctx: SQLParser.Order_by_clauseContext):
        order_by_list = self.visit(ctx.order_by_list())
        order_by_offset = self.visit(ctx.order_by_offset()) if ctx.order_by_offset() else None
        return OrderBy(order_by_list, order_by_offset)

    def visitOrder_by_offset(self, ctx: SQLParser.Order_by_offsetContext):
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1)) if ctx.FETCH() else None
        return OrderByOffset(expr1, expr2)

    def visitOrder_by_list(self, ctx: SQLParser.Order_by_listContext):
        return [self.visit(item) for item in ctx.order_by_item()]

    def visitOrder_by_item(self, ctx: SQLParser.Order_by_itemContext):
        asc = ctx.DESC() is None
        expr = self.visit(ctx.expression())
        return OrderByItem(expr, asc)

    # JOIN
    def visitJoin_clause(self, ctx: SQLParser.Join_clauseContext):
        join_type = self.visit(ctx.join_type())
        table = self.visit(ctx.table_source_item())
        join_condition = self.visit(ctx.join_condition())
        return Join(join_type, table, join_condition)

    def visitJoin_condition(self, ctx: SQLParser.Join_conditionContext):
        return self.visit(ctx.search_condition())

    def visitJoin_type(self, ctx: SQLParser.Join_typeContext):
        if ctx.CROSS():
            return JoinType("CROSS")
        if ctx.FULL():
            return JoinType("FULL")
        if ctx.LEFT():
            return JoinType("LEFT")
        if ctx.RIGHT():
            return JoinType("RIGHT")

        return JoinType("INNER")

    # Table Source

    def visitTable_source_list(self, ctx: SQLParser.Table_source_listContext):
        return TableSourceList([self.visit(source) for source in ctx.table_source()])

    def visitTable_source(self, ctx: SQLParser.Table_sourceContext):
        src_item = self.visit(ctx.table_source_item())
        joins = [self.visit(join) for join in ctx.join_clause()]
        return TableSource(src_item, joins)

    def visitTable_source_item(self, ctx: SQLParser.Table_source_itemContext):

        if ctx.full_table_name():
            src = self.visit(ctx.full_table_name())
        elif ctx.derived_table():
            src = self.visit(ctx.derived_table())
        else:
            src = Variable(ctx.USER_VARIABLE().getText())

        as_alias = self.visit(ctx.as_alias()) if ctx.as_alias() else None
        return TableSourceItem(src, as_alias)

    def visitDerived_table(self, ctx: SQLParser.Derived_tableContext):
        return DerivedTable(self.visit(ctx.select_statement()))

    def visitAs_alias(self, ctx: SQLParser.As_aliasContext):
        return Alias(self.visit(ctx.expression()))

    def visitFull_table_name(self, ctx: SQLParser.Full_table_nameContext):
        parts = [identifier.getText() for identifier in ctx.IDENTIFIER()]
        return Table(parts)

    def visitTop_clause(self, ctx: SQLParser.Top_clauseContext):
        return TopSpec(self.visit(ctx.expression()), ctx.PERCENT() is not None)

    def visitSet_operators(self, ctx):

        if ctx.UNION():
            return SetOperator("UNION ALL" if ctx.ALL() else "UNION")
        return SetOperator(ctx.getText())

    def visitFull_column_name(self, ctx: SQLParser.Full_column_nameContext):
        parts = [ctx.getChild(0).getText()]
        for ident in ctx.IDENTIFIER()[1:]:
            parts.append(ident.getText())
        return ColumnOrTable(parts)

    def visitColumn_list(self, ctx: SQLParser.Column_listContext):
        return ColumnList([self.visit(col) for col in ctx.full_column_name()])

    def visitUser_variable_list(self, ctx: SQLParser.User_variable_listContext):
        return UserVariableList([Variable(var.getText()) for var in ctx.USER_VARIABLE()])

    def visitOperators(self, ctx: SQLParser.OperatorsContext):
        return ctx.getText()

        # Literal

    def visitColumn_type(self, ctx: SQLParser.Column_typeContext):
        data_type = self.visit(ctx.datatype())
        sparse = ctx.SPARSE() is not None
        null_clause = self.visit(ctx.nullability_clause())
        return ColumnType(data_type, sparse, null_clause)

    def visitNullability_clause(self, ctx: SQLParser.Nullability_clauseContext):
        return NullClause(ctx.NOT() is not None)

    # no override for datatype

    def visitSingle_word_data_type(self, ctx: SQLParser.Single_word_data_typeContext):
        return DataType(ctx.getText())

    def visitDecimal_numeric_data_type(self, ctx: SQLParser.Decimal_numeric_data_typeContext):
        literal_pair = self.visit(ctx.literal_pair()) if ctx.literal_pair() else None
        name = ctx.getChild(0).getText()
        return DataType(name, literal_pair)

    def visitLiteral_pair(self, ctx: SQLParser.Literal_pairContext):
        return ItemsList([self.visit(lt) for lt in ctx.literal()])

    def visitChar_nchar_binary_data_type(self, ctx: SQLParser.Char_nchar_binary_data_typeContext):
        name = ctx.getChild(0).getText()
        literal = self.visit(ctx.paren_literal()) if ctx.paren_literal() else None
        return DataType(name, literal)

    def visitParen_literal(self, ctx: SQLParser.Paren_literalContext):
        return self.visit(ctx.literal())

    def visitVarchar_nvarchar_varbinary_data_type(self, ctx: SQLParser.Varchar_nvarchar_varbinary_data_typeContext):
        name = ctx.getChild(0).getText()
        literal = self.visit(ctx.paren_literal_max()) if ctx.paren_literal_max() else None
        return DataType(name, literal)

    def visitParen_literal_max(self, ctx: SQLParser.Paren_literal_maxContext):
        if ctx.MAX():
            return ParenLiteralMax(None, is_max=True)
        else:
            return ParenLiteralMax(self.visit(ctx.literal()), is_max=False)

    def visitFunction_call(self, ctx: SQLParser.Function_callContext):
        schema = None
        if ctx.DOT():
            schema = ctx.IDENTIFIER(0)
            name = ctx.IDENTIFIER(1)
        else:
            name = ctx.getChild(0).getText()

        args = []
        if ctx.function_arguments():
            args = self.visit(ctx.function_arguments())

        return FunctionCall(name, args, schema)

    def visitFunction_arguments(self, ctx: SQLParser.Function_argumentsContext):
        if ctx.STAR():
            return Star()

        return self.visit(ctx.expression_alias_list())

    def visitExpression_alias_list(self, ctx: SQLParser.Expression_alias_listContext):
        return ItemsList([self.visit(expr) for expr in ctx.expression_alias()])

    def visitExpression_alias(self, ctx: SQLParser.Expression_aliasContext):
        expr = self.visit(ctx.expression())
        alias = self.visit(ctx.as_alias()) if ctx.as_alias() else None
        return ExpressionAlaisNode(expr, alias)

    def visitLiteral(self, ctx: SQLParser.LiteralContext):
        return Literal(ctx.getText())
