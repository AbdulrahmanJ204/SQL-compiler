from sql_ast.ast_nodes.ast_node import ASTNode
from typing import Optional

class UpdateStatementNode(ASTNode):
    def __init__(self, with_cte : Optional, top_clause: Optional, table_or_variable, assignment_list, output_clause: Optional, table_source_list: Optional, delete_and_update_where_clause: Optional):
        self.with_cte = with_cte
        self.top_clause = top_clause
        self.table_or_variable = table_or_variable
        self.assignment_list = assignment_list
        self.output_clause = output_clause
        self.table_source_list = table_source_list
        self.delete_and_update_where_clause = delete_and_update_where_clause

    def print(self, spacer="  ", level=0):
        print(spacer*level, "UPDATE")
        if self.with_cte:
            self.with_cte.print(spacer,level+1)

        if self.top_clause:
            self.top_clause.print(spacer,level+1)

        print(spacer*(level+1)+" Updated", end="")
        self.table_or_variable.print("", 0)

        self.assignment_list.print(spacer,level+1)
        if self.output_clause:
            self.output_clause.print(spacer,level+1)

        if self.table_source_list:
            print(spacer * (level + 1) + " FROM")
            self.table_source_list.print(spacer,level+2)

        if self.delete_and_update_where_clause:
            self.delete_and_update_where_clause.print(spacer,level+1)


class UpdateNormalAssignment(ASTNode):
    # UpdateNormalAssignment(target, assignment_operator, source)
    def __init__(self, target, assignment_operator, source):
        self.target = target
        self.assignment_operator = assignment_operator
        self.source = source

    def print(self, spacer="  ", level=0):
        print(spacer*level,"Normal Assignment")
        self.target.print(spacer,level+1)
        print(spacer*(level+1)+f" OP: {self.assignment_operator}")
        self.source.print(spacer,level+1)

class UpdateWriteAssignment(ASTNode):
    def __init__(self, column, exp1, exp2, exp3):
        self.column = column
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

    def print(self, spacer="  ", level=0):
        print(spacer*level,"Write Assignment")
        self.column.print(spacer,level+1)
        self.exp1.print(spacer,level+1)
        self.exp2.print(spacer,level+1)
        self.exp3.print(spacer,level+1)

class UpdateUdtMethodAssignment(ASTNode):
    def __init__(self, column, identifier, arg_list: Optional):
        self.column = column
        self.identifier = identifier
        self.arg_list = arg_list

    def print(self, spacer="  ", level=0):
        print(spacer*level,"Udt Method Assignment")
        self.column.print(spacer,level+1)
        print(spacer * (level + 1)+f" id: {self.identifier}")
        if self.arg_list:
            self.arg_list.print(spacer,level+1)