from .ast_node import ASTNode
from .basic_nodes import SingleValueNode, SingleExpressionNode

class CreateTable(ASTNode):
    def __init__(self, full_table_name, create_table_element_list, table_on_clause=None, table_with_clause=None):
        self.full_table_name = full_table_name
        self.create_table_element_list = create_table_element_list
        self.table_on_clause = table_on_clause
        self.table_with_clause = table_with_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}CreateTable")
        self.full_table_name.print(spacer, level + 1)
        self.create_table_element_list.print(spacer, level + 1)
        if self.table_on_clause:
            self.table_on_clause.print(spacer, level + 1)
        if self.table_with_clause:
            self.table_with_clause.print(spacer, level + 1)


class TableOnClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Table On Clause:")
        self.expression.print(spacer, level + 1)


class TableWithClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Table With Clause:")
        self.expression.print(spacer, level + 1)


class TableOptionCreate(ASTNode):
    def __init__(self, option_type, value, partitions_clause=None):
        self.option_type = option_type
        self.value = value
        self.partitions_clause = partitions_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Table Option: {self.option_type}")
        if self.value:
            self.value.print(spacer, level + 1)
        if self.partitions_clause:
            self.partitions_clause.print(spacer, level + 1)


class DataCompressionKind(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Data Compression: {self.value}")


class LockEscalationValue(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Lock Escalation: {self.value}")


class TablePartitionsClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Table Partitions:")
        self.expression.print(spacer, level + 1)


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
        print(f"{spacer * level}CreateIndex")
        print(f"{spacer * (level + 1)}Name: {self.index_name}")
        print(f"{spacer * (level + 1)}Unique: {self.unique}")
        print(f"{spacer * (level + 1)}Clustered: {self.clustered}")
        print(f"{spacer * (level + 1)}Columnstore: {self.columnstore}")
        
        self.full_table_name.print(spacer, level + 1)
        
        if self.index_column_list:
            self.index_column_list.print(spacer, level + 1)
        if self.include_clause:
            self.include_clause.print(spacer, level + 1)
        if self.where_clause:
            self.where_clause.print(spacer, level + 1)
        if self.index_with_clause:
            self.index_with_clause.print(spacer, level + 1)
        if self.index_on_clause:
            self.index_on_clause.print(spacer, level + 1)


class IndexOnClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Index On Clause:")
        self.expression.print(spacer, level + 1)


class IndexWithClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Index With Clause:")
        self.expression.print(spacer, level + 1)


class IndexOption(ASTNode):
    def __init__(self, option_type, value=None):
        self.option_type = option_type
        self.value = value

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Index Option: {self.option_type}")
        if self.value:
            self.value.print(spacer, level + 1)


class IncludeClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Include Clause:")
        self.expression.print(spacer, level + 1)


class CreateView(ASTNode):
    def __init__(self, full_table_name, select_statement, view_column_list=None, view_with_attributes=None, view_check_option=None):
        self.full_table_name = full_table_name
        self.select_statement = select_statement
        self.view_column_list = view_column_list
        self.view_with_attributes = view_with_attributes
        self.view_check_option = view_check_option

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}CreateView")
        self.full_table_name.print(spacer, level + 1)
        if self.view_column_list:
            self.view_column_list.print(spacer, level + 1)
        if self.view_with_attributes:
            self.view_with_attributes.print(spacer, level + 1)
        self.select_statement.print(spacer, level + 1)
        if self.view_check_option:
            self.view_check_option.print(spacer, level + 1)


class ViewColumnList(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}View Column List:")
        self.expression.print(spacer, level + 1)


class ViewWithAttributes(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}View With Attributes:")
        self.expression.print(spacer, level + 1)


class CreateUser(ASTNode):
    def __init__(self, user_name, create_user_core=None):
        self.user_name = user_name
        self.create_user_core = create_user_core

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}CreateUser")
        self.user_name.print(spacer, level + 1)
        if self.create_user_core:
            self.create_user_core.print(spacer, level + 1)


class CreateUserCore(ASTNode):
    def __init__(self, core_type, login_name=None, password=None, options=None):
        self.core_type = core_type
        self.login_name = login_name
        self.password = password
        self.options = options

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Create User Core: {self.core_type}")
        if self.login_name:
            print(f"{spacer * (level + 1)}Login Name:")
            self.login_name.print(spacer, level + 2)
        if self.password:
            print(f"{spacer * (level + 1)}Password:")
            self.password.print(spacer, level + 2)
        if self.options:
            self.options.print(spacer, level + 1)


class FromExternalProviderClause(ASTNode):
    def __init__(self, limited_options=None):
        self.limited_options = limited_options

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}From External Provider")
        if self.limited_options:
            self.limited_options.print(spacer, level + 1)


class WithUserOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}With User Options:")
        self.expression.print(spacer, level + 1)


class WithLimitedUserOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}With Limited User Options:")
        self.expression.print(spacer, level + 1)


class CreateUserOption(ASTNode):
    def __init__(self, option_type, value):
        self.option_type = option_type
        self.value = value

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}User Option: {self.option_type}")
        self.value.print(spacer, level + 1)


class LimitedUserOption(ASTNode):
    def __init__(self, option_type, value):
        self.option_type = option_type
        self.value = value

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Limited User Option: {self.option_type}")
        self.value.print(spacer, level + 1)


class CreateLogin(ASTNode):
    def __init__(self, login_name, create_login_core):
        self.login_name = login_name
        self.create_login_core = create_login_core

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}CreateLogin")
        self.login_name.print(spacer, level + 1)
        self.create_login_core.print(spacer, level + 1)


class CreateLoginCore(ASTNode):
    def __init__(self, password, options=None):
        self.password = password
        self.options = options

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Create Login Core:")
        print(f"{spacer * (level + 1)}Password:")
        self.password.print(spacer, level + 2)
        if self.options:
            self.options.print(spacer, level + 1)


class CreateLoginOption(ASTNode):
    def __init__(self, option_type, value):
        self.option_type = option_type
        self.value = value

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Login Option: {self.option_type}")
        if self.value:
            self.value.print(spacer, level + 1)


class GrantStatement(ASTNode):
    def __init__(self, permission_name, grant_target, grantee):
        self.permission_name = permission_name
        self.grant_target = grant_target
        self.grantee = grantee

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}GrantStatement: {self.permission_name}")
        self.grant_target.print(spacer, level + 1)
        self.grantee.print(spacer, level + 1)


class GrantTarget(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Grant Target:")
        self.expression.print(spacer, level + 1)


class CreateFunction(ASTNode):
    def __init__(self, function_name, parameters, return_type, body, or_alter=False, options=None):
        self.function_name = function_name
        self.parameters = parameters
        self.return_type = return_type
        self.body = body
        self.or_alter = or_alter
        self.options = options

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}CreateFunction (Or Alter: {self.or_alter})")
        self.function_name.print(spacer, level + 1)
        if self.parameters:
            self.parameters.print(spacer, level + 1)
        
        print(f"{spacer * (level + 1)}Returns:")
        self.return_type.print(spacer, level + 2)
        
        if self.options:
            self.options.print(spacer, level + 1)

        print(f"{spacer * (level + 1)}Body:")
        self.body.print(spacer, level + 2)


class FunctionOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Function Options:")
        self.expression.print(spacer, level + 1)


class FunctionOption(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Function Option: {self.value}")


class ExecuteAsClause(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Execute As: {self.value}")


class TableIndex(ASTNode):
    def __init__(self, index_name, body):
        self.index_name = index_name
        self.body = body

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}TableIndex: {self.index_name}")
        self.body.print(spacer, level + 1)


class TableIndexRowstore(ASTNode):
    def __init__(self, unique_clustered=None, index_column_list=None, include_clause=None, where_clause=None, index_with_clause=None, index_on_clause=None):
        self.unique_clustered = unique_clustered
        self.index_column_list = index_column_list
        self.include_clause = include_clause
        self.where_clause = where_clause
        self.index_with_clause = index_with_clause
        self.index_on_clause = index_on_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Table Index Rowstore:")
        if self.unique_clustered:
            self.unique_clustered.print(spacer, level + 1)
        if self.index_column_list:
            self.index_column_list.print(spacer, level + 1)
        if self.include_clause:
            self.include_clause.print(spacer, level + 1)
        if self.where_clause:
            self.where_clause.print(spacer, level + 1)
        if self.index_with_clause:
            self.index_with_clause.print(spacer, level + 1)
        if self.index_on_clause:
            self.index_on_clause.print(spacer, level + 1)


class TableIndexColumnstore(ASTNode):
    def __init__(self, clustered_columnstore=None, index_column_list=None, include_clause=None, where_clause=None, index_with_clause=None, index_on_clause=None):
        self.clustered_columnstore = clustered_columnstore
        self.index_column_list = index_column_list
        self.include_clause = include_clause
        self.where_clause = where_clause
        self.index_with_clause = index_with_clause
        self.index_on_clause = index_on_clause

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Table Index Columnstore:")
        if self.clustered_columnstore:
            self.clustered_columnstore.print(spacer, level + 1)
        if self.index_column_list:
            self.index_column_list.print(spacer, level + 1)
        if self.include_clause:
            self.include_clause.print(spacer, level + 1)
        if self.where_clause:
            self.where_clause.print(spacer, level + 1)
        if self.index_with_clause:
            self.index_with_clause.print(spacer, level + 1)
        if self.index_on_clause:
            self.index_on_clause.print(spacer, level + 1)


class UniqueClusteredClause(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Unique Clustered: {self.value}")


class ClusteredColumnstoreClause(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Clustered Columnstore: {self.value}")


class IndexColumn(ASTNode):
    def __init__(self, full_column_name, order="ASC"):
        self.full_column_name = full_column_name
        self.order = order

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}IndexColumn ({self.order})")
        self.full_column_name.print(spacer, level + 1)

