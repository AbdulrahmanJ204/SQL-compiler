from sql_ast.ast_nodes.ast_node import ASTNode
from typing import Optional

class InsertStatementNode(ASTNode):
    def __init__(self, with_cte : Optional, top_clause: Optional, table_or_variable, column_list: Optional, output_clause: Optional, insert_source):
        self.with_cte = with_cte
        self.top_clause = top_clause
        self.table_or_variable = table_or_variable
        self.column_list = column_list
        self.output_clause = output_clause
        self.insert_source = insert_source

    def print(self, spacer="  ", level=0):
        print(spacer*level + "INSERT")
        if self.with_cte:
            self.with_cte.print(spacer,level+1)

        if self.top_clause:
            self.top_clause.print(spacer,level+1)

        print(spacer*(level+1)+" INTO", end="")
        self.table_or_variable.print("", 0)

        if self.column_list:
            print(spacer*(level+1)+" FROM")
            self.column_list.print(spacer,level+2)
        if self.output_clause:
            self.output_clause.print(spacer,level+1)

        self.insert_source.print(spacer,level+1)

class InsertedUpdatedValue(ASTNode):
    def __init__(self, value):
        self.value = value

    def print(self, spacer="  ", level=0):
        self.value.print(spacer,level)