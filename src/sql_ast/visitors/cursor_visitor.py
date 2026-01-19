from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.statements import *
from ..ast_nodes.expression_nodes import *
from ..ast_nodes.basic_nodes import *
from ..ast_nodes.cursor_nodes import CursorName


class CursorVisitor(SQLParserVisitor):

    def visitCursor_name(self, ctx: SQLParser.Cursor_nameContext):
        if ctx.USER_VARIABLE():
            return CursorName(name=ctx.USER_VARIABLE().getText())

        return CursorName(
            name=ctx.IDENTIFIER().getText(),
            is_global=ctx.GLOBAL() is not None
        )
