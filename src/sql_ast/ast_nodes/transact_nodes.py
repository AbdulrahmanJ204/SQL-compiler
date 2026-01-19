from .ast_node import ASTNode


class BeginDistributedTransactionNode(ASTNode):
    def __init__(self, name=None):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Begin Distributed Transaction:")
        if self.name:
            self.name.print(spacer, level + 1)


class BeginTransactionNode(ASTNode):
    def __init__(self, name=None):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Begin Transaction")
        if self.name:
            self.name.print(spacer, level + 1)


class TransactionNameWithMarkClauseNode(ASTNode):
    def __init__(self, name, mark_clause=None):
        self.name = name
        self.mark_clause = mark_clause

    def print(self, spacer="  ", level=0):
        self.name.print(spacer, level + 1)
        if self.mark_clause:
            self.mark_clause.print(spacer, level + 1)


class WithMarkClauseNode(ASTNode):
    def __init__(self, literal=None):
        self.literal = literal

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}With Mark " f": {self.literal}" if self.literal else "")


class CommitTransactionNode(ASTNode):
    def __init__(self, name=None, with_delay_durability=None):
        self.name = name
        self.with_delay_durability = with_delay_durability

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}CommitTransaction :")
        if self.name:
            self.name.print(spacer, level + 1)
        if self.with_delay_durability:
            self.with_delay_durability.print(spacer, 1)


class WithDelayDurabilityClauseNode(ASTNode):
    def __init__(self, on):
        self.on = on

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}WithDelayDurabilityClause : {'ON' if self.on else 'OFF'}")


class CommitWorkNode(ASTNode):

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} Commit Work")


class SaveTransactionNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Save Transaction",   end="")
        self.name.print(" ", 1)


class RollbackTransactionNode(ASTNode):
    def __init__(self, name=None):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} Rollback Transaction :", end="")
        if self.name:
            self.name.print(" ", 1)


class RollbackWorkNode(ASTNode):

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} Rollback Work")
