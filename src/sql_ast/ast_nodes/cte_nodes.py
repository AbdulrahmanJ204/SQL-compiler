from .ast_node import ASTNode

class CommonTableExpression(ASTNode):
    def __init__(self, name, column_list, query):
        self.name = name
        self.column_list = column_list
        self.query = query

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"CTE: {self.name}")

        if self.column_list:
            print(spacer * (level + 1)+ "columns")
            self.column_list.print(spacer, level + 2)

        print(spacer * (level + 1)+ "Query")
        self.query.print(spacer, level + 2)

class SetSelectStatement(ASTNode):
    def __init__(self, set_operators, select_statement):
        self.set_operators = set_operators
        self.select_statement = select_statement


    def print(self, spacer="  ", level=0):
        print(spacer * level + "Set Operators")
        self.set_operators.print(spacer, level + 1)

        print(spacer * level + "Select Statement")
        self.select_statement.print(spacer, level + 1)

class SetSelectStatementList(ASTNode):
    def __init__(self, items):
        self.items = items

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Set Select Statements")
        for item in self.items:
            item.print(spacer, level + 1)