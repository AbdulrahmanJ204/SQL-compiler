from sql_ast.ast_nodes.ast_node import ASTNode
from typing import Optional

class DeleteStatementNode(ASTNode):
    def __init__(self, with_cte : Optional, top_clause: Optional, table_source, output_clause: Optional, table_source_list: Optional, delete_and_update_where_clause: Optional):
        self.with_cte = with_cte
        self.top_clause = top_clause
        self.table_source = table_source
        self.output_clause = output_clause
        self.table_source_list = table_source_list
        self.delete_and_update_where_clause = delete_and_update_where_clause

    def print(self, spacer="  ", level=0):
        print(spacer*level + "Delete Statement:")
        if self.with_cte:
            self.with_cte.print(spacer,level+1)

        if self.top_clause:
            self.top_clause.print(spacer,level+1)

        # print(spacer*(level+1)+" DELETED", end="")
        self.table_source.print(spacer , level+1)

        if self.output_clause:
            self.output_clause.print(spacer,level+1)

        if self.table_source_list:
            print(spacer * (level + 1) + " FROM")
            self.table_source_list.print(spacer,level+2)

        if self.delete_and_update_where_clause:
            self.delete_and_update_where_clause.print(spacer,level+1)