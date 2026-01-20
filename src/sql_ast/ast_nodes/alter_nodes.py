from symtable import Class

from .ast_node import ASTNode
from .basic_nodes import SingleValueNode, SingleExpressionNode


class AlterTableStatement(ASTNode):
    def __init__(self, table, actions, alter_table=None):
        self.table = table
        self.action = actions
        self.alter_table = alter_table

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter Table Statement:")
        self.table.print(spacer, level + 1)
        if self.alter_table:
            self.alter_table.print(spacer, level + 1)
        print(spacer * level + "Actions : ")
        self.action.print(spacer, level + 1)


class AlterTableWithClause(ASTNode):
    def __init__(self, check=False):
        self.check = check

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter Table With Clause:")
        print(spacer * (level + 1) + f"Check: {self.check}")


class TableChangeTracking(ASTNode):
    def __init__(self, enabled, change_with=None):
        self.enabled = enabled
        self.change_with = change_with

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Change Tracking:")
        print(spacer * (level + 1) + f"Enabled: {self.enabled}")
        if self.change_with:
            print(spacer * (level + 1) + "Change With:")
            self.change_with.print(spacer, level + 2)




class SetTableOption(ASTNode):
    def __init__(self, options_list):
        self.options_list = options_list

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Set Table Options:")
        self.options_list.print(spacer, level + 1)


class AlterTableOptionLeaf(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Lock Escalation : {self.value}")


class AlterTableColumn(ASTNode):
    def __init__(self, column, action):
        self.column = column
        self.action = action

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter Table Column:", end="")
        self.column.print("", 0)
        print()
        self.action.print(spacer, level + 1)


class AlterColumnType(ASTNode):
    def __init__(self, col_type, collate, encrypted_with, nullable, sparse, alter_with_clause):
        self.col_type = col_type
        self.collate = collate
        self.encrypted_with = encrypted_with
        self.nullable = nullable
        self.sparse = sparse
        self.alter_with_clause = alter_with_clause

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter :")
        self.col_type.print(spacer, level + 2)
        if self.collate:
            print(spacer * (level + 1) + "Collate:")
            self.collate.print(spacer, level + 2)
        if self.encrypted_with:
            print(spacer * (level + 1) + "Encrypted With:")
            self.encrypted_with.print(spacer, level + 2)
        self.nullable.print(spacer, level + 1)
        print(spacer * (level + 1) + f"Sparse: {self.sparse}")
        if self.alter_with_clause:
            print(spacer * (level + 1) + "Alter With Clause:")
            self.alter_with_clause.print(spacer, level + 2)


class CollateClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Collate :")
        self.expression.print("", 0)
        print()


class AlterColumnOptionAction(ASTNode):
    def __init__(self, add_or_drop, option):
        self.option = option
        self.add_or_drop = add_or_drop

    def print(self, spacer="  ", level=0):
        print(spacer * level + self.add_or_drop + " Option: ")
        self.option.print(spacer, level + 1)


class AlterColumnOptionLeaf(SingleValueNode):
    pass


class TableAddItem(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Add To Table:")
        self.expression.print(spacer, level + 1)


class TableRenameColumn(ASTNode):
    def __init__(self, old_column_name, new_column_name):
        self.old_column_name = old_column_name
        self.new_column_name = new_column_name

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Rename Column:")
        print(spacer * (level + 1) + f"Old Column Name:")
        self.old_column_name.print(spacer, level + 1)
        print(spacer * (level + 1) + f"New Column Name: {self.new_column_name}")


class TableCheckConstraint(ASTNode):
    def __init__(self, constraint_target, check=True, ):
        self.constraint_target = constraint_target
        self.check = check

    def print(self, spacer="  ", level=0):
        print(spacer * level + ("Check:" if self.check else "No Check:") + f" {self.constraint_target}")


class DropTableConstraintWith(ASTNode):
    def __init__(self, constraint_name, drop_with=None):
        self.constraint_name = constraint_name
        self.drop_with = drop_with

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Drop From Table:")
        print(spacer * (level + 1) + f"Constraint Name: {self.constraint_name}")
        if self.drop_with:
            print(spacer * (level + 1) + "Drop With:")
            self.drop_with.print(spacer, level + 2)


class DropTableItems(ASTNode):
    def __init__(self, items=None):
        self.items = items

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Drop ")
        if self.items:
            self.items.print(spacer, level + 1)


class DropConstraintSpec(ASTNode):
    def __init__(self, constraint_list, if_exists, drop_with_clause):
        self.constraint_list = constraint_list
        self.if_exists = if_exists
        self.drop_with_clause = drop_with_clause

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Drop Constraints{" If Exists" if self.if_exists else ""}:")
        self.constraint_list.print(spacer, level + 1)
        if self.drop_with_clause:
            print(spacer * (level + 1) + "Drop With:")
            self.drop_with_clause.print(spacer, level + 2)


class DropColumnSpec(ASTNode):
    def __init__(self, column_list, if_exists):
        self.column_list = column_list
        self.if_exists = if_exists

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Drop Columns{" If Exists" if self.if_exists else ""}:")
        self.column_list.print(spacer, level + 1)


class AlterIndex(ASTNode):
    def __init__(self, index, table, action):
        self.index = index
        self.table = table
        self.action = action

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Alter Index: {self.index}")
        self.table.print(spacer, level + 1)
        self.action.print(spacer, level + 1)


class SingleWordAlterIndexAction(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Action : " + self.value)


class SetIndexOptionClause(ASTNode):
    def __init__(self, index_option_list):
        self.index_option_list = index_option_list

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Set Index Options:")
        self.index_option_list.print(spacer, level + 1)




class ComperssionDelayOption(ASTNode):
    def __init__(self, delay_value):
        self.delay_value = delay_value

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Compression Delay :  ")
        self.delay_value.print(spacer, level + 1)


class RebuildClause(ASTNode):
    def __init__(self, body = None):
        self.body = body

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Rebuild Clause  ")
        if self.body:
            self.body.print(spacer, level + 1)


class RebuildBody(ASTNode):
    def __init__(self, par_eq, rebuild_options):
        self.par_eq = par_eq
        self.rebuild_options = rebuild_options

    def print(self, spacer="  ", level=0):
        if self.par_eq or self.rebuild_options:
            print(spacer * level + "Rebuild Body:")
        if self.par_eq:
            self.par_eq.print(spacer, level + 1)
        if self.rebuild_options:
            self.rebuild_options.print(spacer, level + 1)


class PartitionEqualAll(ASTNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Partition Equal All ")


class PartitionEqualLiteral(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Partition Equal : {self.value} ")


class RebuildWithOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Rebuild With Options: ")
        self.expression.print(spacer, level + 1)


class ReorganizeClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Reorganize Clause: ")
        self.expression.print(spacer, level + 1)


class ReorganizeBody(ASTNode):
    def __init__(self, par_eq, reorganize_options):
        self.par_eq = par_eq
        self.reorganize_options = reorganize_options

    def print(self, spacer="  ", level=0):
        if self.par_eq or self.reorganize_options:
            print(spacer * level + "Reorganize Body: ", end="")
        if self.par_eq:
            self.par_eq.print("", 0)
        if self.reorganize_options:
            print()
            self.reorganize_options.print(spacer, level + 1)


class ReorganizeWithOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Reorganize With Options: ")
        self.expression.print(spacer, level + 1)


class ResumeClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Resume Clause ")
        if self.expression:
            self.expression.print(spacer, level + 1)


class ResumeWithOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Resume With Options: ")
        self.expression.print(spacer, level + 1)



class XmlCompressionOptionWithRebuild(ASTNode):
    def __init__(self, xml_compression_option, rebuild_clause):
        self.xml_compression_option = xml_compression_option
        self.rebuild_clause = rebuild_clause

    def print(self, spacer="  ", level=0):
        print(spacer * level + "XML Compression Option: ")
        self.xml_compression_option.print(spacer, level + 1)
        if self.rebuild_clause:
            self.rebuild_clause.print(spacer, level + 1)



class MaxDopExpressionOption(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "MaxDop Expression Option: ")
        self.expression.print(spacer, level + 1)


class RebuildCompressionKind(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Rebuild Compression Kind : {self.value} ")


class OnPartitionsClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "On Partitions: ")
        self.expression.print(spacer, level + 1)


class OnlineOption(ASTNode):
    def __init__(self, on, expression=None):
        self.on = on
        self.expression = expression

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Online Option: {'ON' if self.on else 'OFF'}")
        if self.expression:
            self.expression.print(spacer, level + 2)


class LowPriorityLockWait(ASTNode):
    def __init__(self, mx_dur_mins, abort_after_wait):
        self.mx_dur_mins = mx_dur_mins
        self.abort_after_wait = abort_after_wait

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Low Priority Lock Wait: ")
        self.mx_dur_mins.print(spacer, level + 1)
        print(spacer * (level + 1) + f"Abort After Wait: {self.abort_after_wait}")


class AlterViewStatement(ASTNode):
    def __init__(self, table, select_st, col_list=None, attribute_clause=None, check_option=None):
        self.table = table
        self.col_list = col_list
        self.attribute_clause = attribute_clause
        self.select_st = select_st
        self.check_option = check_option

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter View Statement: ")
        self.table.print(spacer, level + 1)
        if self.col_list:
            print(spacer * (level + 1) + "Column List: ")
            self.col_list.print(spacer, level + 2)
        if self.attribute_clause:
            self.attribute_clause.print(spacer, level + 2)
        print(spacer * (level + 1) + "As : ")
        self.select_st.print(spacer, level + 2)
        if self.check_option:
            print(spacer * (level + 1) + "Check Option: ")
            self.check_option.print(spacer, level + 2)


class WithViewAttributes(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "With View Attributes: ")
        self.expression.print(spacer, level + 1)


class AlterUserStatement(ASTNode):
    def __init__(self, user_name, with_option):
        self.user_name = user_name
        self.with_option = with_option

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter User Statement: ")
        self.user_name.print(spacer, level + 1)
        self.with_option.print(spacer, level + 1)


class UserNameNode(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"User Name: {self.value}")


class WithUserOptions(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "With User Options: ")
        self.expression.print(spacer, level + 1)


class IdentifierEqualIdentifierOption(ASTNode):
    def __init__(self, identifier, identifier_2):
        self.identifier = identifier
        self.identifier_2 = identifier_2

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"{self.identifier} = {self.identifier_2} ")

class DefaultSchemaEqualOption(ASTNode):
    def __init__(self, default_schema):
        self.default_schema = default_schema

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"DEFAULT_SCHEMA = {self.default_schema} ")

class LoginOption(ASTNode):
    def __init__(self, login_name):
        self.login_name = login_name

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"LOGIN = {self.login_name} ")

class PasswordAndOldPasswordOption(ASTNode):
    def __init__(self, password, old_password = None):
        self.password = password
        self.old_password = old_password

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"PASSWORD = {self.password} ")
        if self.old_password:
            print(spacer * level  + f"OLD_PASSWORD = {self.old_password} ")


class DefaultLanguageOption(ASTNode):
    def __init__(self, language):
        self.language = language

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"DEFAULT_LANGUAGE = {self.language} ")
