from .ast_node import ASTNode


class OutputStatement(ASTNode):
    def __init__(self, select_list, into_clause):
        self.select_list = select_list
        self.into_clause = into_clause

    def print(self, spacer="  ", level=0):
        print(spacer * level, "Select List")
        self.select_list.print(spacer, level + 1)

        if self.into_clause:
            print(spacer * level, "Into Clause")
            self.into_clause.print(spacer, level + 1)

class OutputSelectListItem(ASTNode):
    def __init__(self, type, alias = None):
        self.type = type
        self.alias = alias

    def print(self, spacer="  ", level=0):
        print(spacer * level ,self.type)
        if self.alias:
            self.alias.print(spacer, level + 1)
class OutputIntoClause(ASTNode):
    def __init__(self, t_name, column_list = None):
        self.t_name = t_name
        self.column_list = column_list

    def print(self, spacer="  ", level=0):
        print(self.t_name, " ")
        if self.column_list:
            self.column_list.print(spacer, level + 1)