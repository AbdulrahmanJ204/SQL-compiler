from .ast_node import ASTNode


class WhileClause(ASTNode):
    def __init__(self, search_condition, statements):
        self.search_condition = search_condition
        self.statements = statements

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}" "WhileClause: {")
        print(f"{spacer * (level + 1)}Search Condition:")
        self.search_condition.print(spacer, level + 2)
        print(f"{spacer * (level + 1)}Statements:")
        self.statements.print(spacer, level + 2)
        print(f"{spacer * level}" "}")


class IfClause(ASTNode):
    def __init__(self, condition, statements, else_clauses=None):
        self.condition = condition
        self.statements = statements
        self.else_clauses = else_clauses

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}""IfClause: {")
        print(f"{spacer * (level + 1)}Condition:")
        self.condition.print(spacer, level + 2)
        print(f"{spacer * (level + 1)}Statements:")
        self.statements.print(spacer, level + 2)
        if self.else_clauses:
            print(f"{spacer * (level + 1)}Else Clauses:")
            self.else_clauses.print(spacer, level + 2)
        print(f"{spacer * level}""         }")

class BreakStatement(ASTNode):
    def __init__(self):
        pass

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}BreakStatement\n")

class ContinueStatement(ASTNode):
    def __init__(self):
        pass

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}ContinueStatement\n")