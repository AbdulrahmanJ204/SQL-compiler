from .ast_node import ASTNode

class DropTable(ASTNode):
    def __init__(self, table_name, exists: bool):
        self.table_name = table_name
        self.exists = exists

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} DropTable")
        self.table_name.print(spacer, level + 1)
        print(f"{spacer * (level + 1)} if exists: {self.exists}")


class DropView(ASTNode):
    def __init__(self, view_name_list, exists: bool):
        self.view_name_list = view_name_list
        self.exists = exists

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} DropView")
        self.view_name_list.print(spacer, level + 1)
        print(f"{spacer * (level + 1)} if exists: {self.exists}")


class DropUser(ASTNode):
    def __init__(self, user_name, exists: bool):
        self.user_name = user_name
        self.exists = exists

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} DropUser")
        self.user_name.print(spacer, level + 1)
        print(f"{spacer * (level + 1)} if exists: {self.exists}")

class DropIndexItem(ASTNode):

    def __init__(self, index_name, full_table_name, exists: bool, drop_index_with_clause=None):
        self.index_name = index_name
        self.full_table_name = full_table_name
        self.exists = exists
        self.drop_index_with_clause = drop_index_with_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} DropIndexItem")

        print(f"{spacer * (level + 1)} Index Name:")
        self.index_name.print(spacer, level + 2)

        print(f"{spacer * (level + 1)} On Table:")
        self.full_table_name.print(spacer, level + 2)

        if self.drop_index_with_clause:
            print(f"{spacer * (level + 1)} With Clause:")
            self.drop_index_with_clause.print(spacer, level + 2)

        print(f"{spacer * (level + 1)} if exists: {self.exists}")

class DropFunction(ASTNode):
    def __init__(self, drop_function_name_list, exists: bool):
        self.drop_function_name_list = drop_function_name_list
        self.exists = exists

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} DropFunction")
        self.drop_function_name_list.print(spacer, level + 1)
        print(f"{spacer * (level + 1)} if exists: {self.exists}")

