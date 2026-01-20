from .ast_node import ASTNode

class CreateTable(ASTNode):
    def __init__(self, full_table_name, create_table_element_list, table_on_clause=None, table_with_clause=None):
        self.full_table_name = full_table_name
        self.create_table_element_list = create_table_element_list
        self.table_on_clause = table_on_clause
        self.table_with_clause = table_with_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} CreateTable")
        self.full_table_name.print(spacer, level + 1)
        self.create_table_element_list.print(spacer, level + 1)
        if self.table_on_clause:
            self.table_on_clause.print(spacer, level + 1)
        if self.table_with_clause:
            self.table_with_clause.print(spacer, level + 1)


class CreateIndex(ASTNode):
    def __init__(self, index_name, full_table_name, index_column_list=None, unique=False, clustered=False, columnstore=False, include_clause=None, where_clause=None, index_with_clause=None, index_on_clause=None):
        self.index_name = index_name
        self.full_table_name = full_table_name
        self.index_column_list = index_column_list
        self.unique = unique
        self.clustered = clustered
        self.columnstore = columnstore
        self.include_clause = include_clause
        self.where_clause = where_clause
        self.index_with_clause = index_with_clause
        self.index_on_clause = index_on_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} CreateIndex")
        print(f"{spacer * (level + 1)} Name: {self.index_name}")
        print(f"{spacer * (level + 1)} Unique: {self.unique}")
        print(f"{spacer * (level + 1)} Clustered: {self.clustered}")
        print(f"{spacer * (level + 1)} Columnstore: {self.columnstore}")
        
        self.full_table_name.print(spacer, level + 1)
        
        if self.index_column_list:
            self.index_column_list.print(spacer, level + 1)
        if self.include_clause:
            self.include_clause.print(spacer, level + 1)
        if self.where_clause:
            self.where_clause.print(spacer, level + 1)


class CreateView(ASTNode):
    def __init__(self, full_table_name, select_statement, view_column_list=None, view_with_attributes=None, view_check_option=None):
        self.full_table_name = full_table_name
        self.select_statement = select_statement
        self.view_column_list = view_column_list
        self.view_with_attributes = view_with_attributes
        self.view_check_option = view_check_option

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} CreateView")
        self.full_table_name.print(spacer, level + 1)
        if self.view_column_list:
            self.view_column_list.print(spacer, level + 1)
        if self.view_with_attributes:
            self.view_with_attributes.print(spacer, level + 1)
        self.select_statement.print(spacer, level + 1)


class CreateUser(ASTNode):
    def __init__(self, user_name, create_user_core=None):
        self.user_name = user_name
        self.create_user_core = create_user_core

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} CreateUser")
        self.user_name.print(spacer, level + 1)
        if self.create_user_core:
            self.create_user_core.print(spacer, level + 1)


class CreateLogin(ASTNode):
    def __init__(self, login_name, create_login_core):
        self.login_name = login_name
        self.create_login_core = create_login_core

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} CreateLogin")
        self.login_name.print(spacer, level + 1)
        self.create_login_core.print(spacer, level + 1)


class GrantStatement(ASTNode):
    def __init__(self, permission_name, grant_target, grantee):
        self.permission_name = permission_name
        self.grant_target = grant_target
        self.grantee = grantee

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} GrantStatement: {self.permission_name}")
        self.grant_target.print(spacer, level + 1)
        self.grantee.print(spacer, level + 1)


class CreateFunction(ASTNode):
    def __init__(self, function_name, parameters, return_type, body, or_alter=False, options=None):
        self.function_name = function_name
        self.parameters = parameters
        self.return_type = return_type
        self.body = body
        self.or_alter = or_alter
        self.options = options

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} CreateFunction (Or Alter: {self.or_alter})")
        self.function_name.print(spacer, level + 1)
        if self.parameters:
            self.parameters.print(spacer, level + 1)
        
        print(f"{spacer * (level + 1)} Returns:")
        self.return_type.print(spacer, level + 2)
        
        if self.options:
            self.options.print(spacer, level + 1)

        print(f"{spacer * (level + 1)} Body:")
        self.body.print(spacer, level + 2)

class TableIndex(ASTNode):
    def __init__(self, index_name, body):
        self.index_name = index_name
        self.body = body

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} TableIndex: {self.index_name}")
        self.body.print(spacer, level + 1)

class IndexColumn(ASTNode):
    def __init__(self, full_column_name, order="ASC"):
        self.full_column_name = full_column_name
        self.order = order

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level} IndexColumn ({self.order})")
        self.full_column_name.print(spacer, level + 1)

