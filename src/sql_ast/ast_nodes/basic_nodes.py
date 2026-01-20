from .ast_node import ASTNode


class SingleValueNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level + self.value)


class UserVariable(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level +  "User Variable : " + self.value)


class Variable(SingleValueNode):
    pass


class Literal(ASTNode):
    def __init__(self, value, type_=None):
        self.value = value
        self.type_ = type_

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Literal: ")
        print(spacer * (level + 1) + f" Value: {self.value}")

        if self.type_:
            print(spacer * (level + 1) + f" Type: {self.type_}")


class GroupBy(ASTNode):
    def __init__(self, items, with_):
        self.items = items
        self.with_ = with_

    def print(self, spacer="  ", level=0):
        to_print = ""
        if self.with_:
            to_print = "WITH " + self.with_

        self.self_print(spacer * level, to_print)
        for item in self.items:
            item.print(spacer, level + 1)


class OrderByItem(ASTNode):
    def __init__(self, expression, asc=True):
        self.expression = expression
        self.asc = asc

    def print(self, spacer="  ", level=0):

        print(spacer * level + ("Ascending" if self.asc else "Descending") + " :")
        self.expression.print(spacer, level + 1)


class OrderByOffset(ASTNode):
    def __init__(self, offset, fetch_next_rows_only=None):
        self.offset = offset
        self.fetch_next_rows_only = fetch_next_rows_only

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        print(spacer * (level + 1) + "OFFSET : ")
        self.offset.print(spacer, level + 2)
        if self.fetch_next_rows_only:
            print(spacer * (level + 1)+ "ONLY NEXT ROWS :")
            self.fetch_next_rows_only.print(spacer, level + 2)


class OrderBy(ASTNode):
    def __init__(self, order_by_list, offset=None):
        self.order_by_list = order_by_list
        self.offset = offset

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Order By:")
        for item in self.order_by_list:
            item.print(spacer, level + 1)

        if self.offset:
            self.offset.print(spacer, level + 1)


class SetOperator(ASTNode):
    def __init__(self, operator):
        self.operator = operator

    def print(self, spacer="  ", level=0):
        print(spacer * level, self.operator)


class SingleExpressionNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.expression.print(spacer, level + 1)


class ExpressionAlaisNode(ASTNode):
    def __init__(self, expression, alias=None):
        self.expression = expression
        self.alias = alias

    def print(self, spacer="  ", level=0):
        # self.self_print(spacer * level)
        self.expression.print(spacer, level + 1)
        if self.alias:
            self.alias.print(spacer, level + 2)


class WhereClause(ASTNode):
    def __init__(self, condition, is_cursor=False):
        self.condition = condition
        self.is_cursor = is_cursor

    def print(self, spacer="  ", level=0):
        print(spacer*level + "Where " , end= '')
        if self.is_cursor:
            print( "CURRENT OF " , end="")
        print(":")
        self.condition.print(spacer, level + 1)


class StatementBlock(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        for statement in self.statements:
            statement.print(spacer, level + 1)


class Alias(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alias :")
        self.expression.print(spacer, level + 1)


class Having(SingleExpressionNode):
    pass


class Table(ASTNode):  # full_table_name
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Name : " + self.name)


class ColumnOrTable(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Column : " + self.name)


class FunctionCall(ASTNode):
    def __init__(self, name, args=None, schema=None):
        self.schema = schema
        self.name = name
        self.args = args

    def print(self, spacer="  ", level=0):
        full_name = f"{self.schema}.{self.name}" if self.schema else self.name
        print(spacer * level + "Function Call : ")
        print(spacer * (level + 1)+ "Name: " + full_name)

        if self.args:
            print(spacer * (level + 1)+ "Arguments:")
            self.args.print(spacer, level + 1)


class DerivedTable(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Derived Table :")
        self.expression.print(spacer, level + 1)


class TableSourceItem(ExpressionAlaisNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Source Details :")
        self.expression.print(spacer, level + 1)
        if self.alias:
            self.alias.print(spacer, level + 1)
        else:
            print(spacer * (level + 1) + "Alias : None")


class TableSourceList(ASTNode):
    def __init__(self, sources):
        self.sources = sources

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Sources:")
        for src in self.sources:
            src.print(spacer, level + 1)


class JoinType(ASTNode):
    def __init__(self, name):
        self.name = name

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Join Type : " + self.name)


class Join(ASTNode):
    def __init__(self, join_type, table, join_condition):
        self.join_type = join_type
        self.table = table
        self.join_condition = join_condition

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Join:")
        self.table.print(spacer, level + 1)
        self.join_type.print(spacer, level + 1)
        if self.join_condition:
            self.join_condition.print(spacer, level + 1)


class TableSource(ASTNode):
    def __init__(self, table, joins):
        self.table = table
        self.joins = joins

    def print(self, spacer="  ", level=0):
        # self.self_print(spacer * level)
        print(spacer * level + "Table Source:")
        self.table.print(spacer, level + 1)
        if self.joins:
            self.joins.print(spacer, level + 1)


class ItemsList(ASTNode):
    def __init__(self, items):
        self.items = items

    def print(self, spacer="  ", level=0):
        for item in self.items:
            if item:
                item.print(spacer, level)
            else:
                print(spacer * level + "Warning : Null Node")


class JoinsList(ItemsList):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Join List: ", end="")
        if len(self.items) == 0:
            print( "No Joins")
            return
        print()
        for join in self.items:
            join.print(spacer, level + 1)


class InsertRecordsList(ItemsList):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Records :")
        for record in self.items:
            record.print(spacer, level + 1)


class InsertRecordValuesList(ItemsList):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Record Values :")
        for value in self.items:
            value.print(spacer, level + 1)


class AssignmentList(ItemsList):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Assignment: ")
        for value in self.items:
            value.print(spacer, level + 1)


class ArgumentList(ItemsList):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Arguments :")
        for value in self.items:
            value.print(spacer, level + 1)


class CursorUpdateColumnsList(ItemsList):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "OF: ")
        for column in self.items:
            column.print(spacer, level + 1)


class FetchIntoClauseList(ItemsList):
    def print(self, spacer="  ", level=0):
        for var in self.items:
            var.print(spacer, level)


class DefaultValue(ASTNode):
    def __init__(self, default_text):
        self.default_text = default_text

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Default Value")


class ColumnList(ItemsList):
    pass


class UserVariableList(ItemsList):
    pass


class NullClause(ASTNode):
    def __init__(self, nullable: bool):
        self.nullable = nullable

    def print(self, spacer="  ", level=0):
        print(f"{spacer * level}Nullability: {'Null' if self.nullable else 'Not Null'}")


class ColumnType(ASTNode):
    def __init__(self, data_type, sparse=False, nullable=None):
        self.data_type = data_type
        self.sparse = sparse
        self.nullable = nullable

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Column Type")
        self.data_type.print(spacer, level + 1)
        if self.sparse:
            print(spacer * level + "Sparse")
        if self.nullable:
            self.nullable.print(spacer, level + 1)


class DataType(ASTNode):
    def __init__(self, name, params=None):
        self.name = name
        self.params = params

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Data Type : {self.name}")
        if self.params:
            self.params.print(spacer, level + 1)


class ParenLiteralMax(ASTNode):
    def __init__(self, value, is_max=False):
        self.value = value
        self.is_max = is_max

    def print(self, spacer="  ", level=0):
        if self.is_max:
            print(spacer * level + "MAX")
        else:
            self.value.print(spacer, level + 1)


class ColumnDefinition(ASTNode):
    def __init__(self, name, column_type, constraints, encrypted_with=None):
        self.name = name
        self.column_type = column_type
        self.constraints = constraints
        self.encrypted_with = encrypted_with

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.name.print(spacer, level + 1)
        self.column_type.print(spacer, level + 1)
        if self.encrypted_with:
            self.encrypted_with.print(spacer, level + 2)
        self.constraints.print(spacer, level + 1)


class ColumnAs(ExpressionAlaisNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Column :")
        self.expression.print(spacer, level + 1)
        if self.alias:
            self.alias.print(spacer, level + 1)


class ComputedColumnDefinition(ASTNode):
    def __init__(self, name, expression, persisted=False):
        self.name = name
        self.expression = expression
        self.persisted = persisted

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.name.print(spacer, level + 1)
        self.expression.print(spacer, level + 1)
        if self.persisted:
            print(spacer * (level + 1)+ "Persisted")


class ColumnConstraint(ASTNode):
    def __init__(self, body, prefix=None):
        self.body = body
        self.prefix = prefix

    def print(self, spacer="  ", level=0):
        if self.prefix:
            print(spacer * level, self.prefix)
        self.body.print(spacer, level + 1)


class IdentityConstraint(ASTNode):
    def __init__(self, seed=1, increment=1):
        self.seed = seed
        self.increment = increment

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        print(spacer * (level + 1)+ f"Seed : {self.seed}")
        print(spacer * (level + 1)+ f"Increment : {self.increment}")


class CheckConstraint(ASTNode):
    def __init__(self, condition):
        self.condition = condition

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.condition.print(spacer, level + 1)


class PrimaryKeyConstraint(ASTNode):
    def __init__(self, clustered=True):
        self.clustered = clustered

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Primary Key: {'Clustered' if self.clustered else 'Non Clustered'}")


class UniqueConstraint(ASTNode):
    def __init__(self, clustered=True):
        self.clustered = clustered

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Unique : {'Clustered' if self.clustered else 'Non Clustered'}")


class ColumnForeignKeyConstraint(ASTNode):
    def __init__(self, referenced_table, referenced_column):
        self.referenced_table = referenced_table
        self.referenced_column = referenced_column

    def print(self, spacer="  ", level=0):
        print(spacer * (level + 1)+ "Foreign Key References :")
        self.referenced_table.print(spacer, level + 2)
        self.referenced_column.print(spacer, level + 2)


class DefaultConstraint(ASTNode):
    def __init__(self, default_value, with_values):
        self.default_value = default_value
        self.with_values = with_values

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Default Constraint"" With Values" if self.with_values else "")
        self.default_value.print(spacer, level + 1)


class TableConstraint(ASTNode):
    def __init__(self, body, prefix=None):
        self.body = body
        self.prefix = prefix

    def print(self, spacer="  ", level=0):
        if self.prefix:
            print(spacer * level, self.prefix)
        self.body.print(spacer, level + 1)


class PrimaryKeyTableConstraint(ASTNode):
    def __init__(self, column_list, pk, with_):
        self.column_list = column_list
        self.pk = pk
        self.with_ = with_

    def print(self, spacer="  ", level=0):
        self.pk.print(spacer, level + 1)
        self.column_list.print(spacer, level + 1)
        if self.with_:
            self.with_.print(spacer, level + 1)


class UniqueTableConstraint(ASTNode):
    def __init__(self, column_list, unique, with_):
        self.column_list = column_list
        self.unique = unique
        self.with_ = with_

    def print(self, spacer="  ", level=0):
        self.unique.print(spacer, level + 1)
        self.column_list.print(spacer, level + 1)
        if self.with_:
            self.with_.print(spacer, level + 1)


class PrimaryKeyColConstraint(ASTNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Primary Key")


class UniqueColConstraint(ASTNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Unique")


class ForeignKeyTableConstraint(ASTNode):
    def __init__(self, column_list, referenced_table, referenced_column):
        self.column_list = column_list
        self.referenced_table = referenced_table
        self.referenced_column = referenced_column

    def print(self, spacer="  ", level=0):
        print(spacer * (level + 1)+ "Foreign Key Columns :")
        self.column_list.print(spacer, level + 2)
        print(spacer * (level + 1)+ "References :")
        self.referenced_table.print(spacer, level + 2)
        self.referenced_column.print(spacer, level + 2)


class DefaultTableConstraint(ASTNode):
    def __init__(self, column, default_value):
        self.column = column
        self.default_value = default_value

    def print(self, spacer="  ", level=0):
        print(spacer * (level + 1)+ "COLUMN :")
        self.column.print(spacer, level + 2)
        print(spacer * (level + 1)+ "Default value :")
        self.default_value.print(spacer, level + 2)


class TableTypeDefinition(ASTNode):
    def __init__(self, lst):
        self.list = lst

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Type Definition :")
        self.list.print(spacer, level + 2)


class GoStatement(ASTNode):
    def __init__(self, id=None):
        self.id = id

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Go Statement :")
        if self.id:
            print(spacer * (level + 1)+ f"Use : {self.id}")


class PrintClause(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level)
        self.expression.print(spacer, level + 1)


class WithPartitionNumberExpression(ASTNode):
    def __init__(self, expressions_list):
        self.expressions_list = expressions_list

    def print(self, spacer="  ", level=0):
        print(spacer * level + "With Partitions :")
        self.expressions_list.print(spacer, level + 2)


class Range(ASTNode):
    def __init__(self, from_, to_):
        self.from_ = from_
        self.to_ = to_

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Range : {self.from_} to {self.to_}")


class FunctionParameters(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        if self.expression:
            print(spacer * level + "Function Parameters :")
            self.expression.print(spacer, level + 1)


class FunctionParameter(ASTNode):
    def __init__(self, name, data_type, null_=None, default_value=None, read_only=None):
        self.name = name
        self.data_type = data_type
        self.default_value = default_value
        self.read_only = read_only
        self.null_ = null_

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Function Parameter :")
        print(spacer * (level + 1) + "Name :")
        self.name.print(spacer, level + 2)
        self.data_type.print(spacer, level + 1)
        if self.null_:
            self.null_.print(spacer, level + 1)
        if self.default_value:
            print(spacer * (level + 1)+ "DEFAULT VALUE :")
            self.default_value.print(spacer, level + 2)
        if self.read_only:
            print(spacer * (level + 1)+ "READ ONLY")


class IndexName(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"INDEX NAME : {self.value}")


class ViewAttribute(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"VIEW ATTRIBUTE : {self.value}")


class ViewCheckOption(ASTNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "With Check Option")


class OptionOnOff(ASTNode):
    def __init__(self, on):
        self.on = on

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Option {"ON" if self.on else "OFF"}")


class ChangeTrackingWithClause(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"With Track Columns Updated : {"ON" if self.on else "OFF"}")


class AllowRowLocks(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Allow Row Locks: " + ("ON" if self.on else "OFF"))


class AllowPageLocks(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Allow Page Locks: " + ("ON" if self.on else "OFF"))


class OptimizeForSequentialKey(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Optimize For Sequential Key: " + ("ON" if self.on else "OFF"))


class IgnoreDupKey(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Ignore Duplicated Key: " + ("ON" if self.on else "OFF"))


class XmlCompressionOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "XML Compression Option: " + ("ON" if self.on else "OFF"))


class StatisticsIncrementalOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Statistics Incremental Option: " + ("ON" if self.on else "OFF"))


class SortInTempDBOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Sort In TempDB Option: " + ("ON" if self.on else "OFF"))


class ResumableOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Resumable Option: " + ("ON" if self.on else "OFF"))


class StatisticsNoRecompute(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Statistics No Recompute : " + ("ON" if self.on else "OFF"))


class PadIndexOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"PAD INDEX : {'ON' if self.on else 'OFF'}")


class DropExistingOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Drop Existing : {'ON' if self.on else 'OFF'}")


class FilterFactorOption(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Filter Factor : {self.value}")

class FillFactorOption(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Fill Factor : {self.value}")

class PartitionTarget(ASTNode):
    def __init__(self, partition_name, column=None):
        self.partition_name = partition_name
        self.column = column

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Partition Target : ")
        print(spacer * (level + 1)+ "Partition Name : " + self.partition_name)
        if self.column:
            self.column.print(spacer, level + 1)


class LobCompactionOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Lob Compaction Option: " + ("ON" if self.on else "OFF"))


class CompressAllRowGroupsOption(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Compress All Row Groups Option: " + ("ON" if self.on else "OFF"))


class EncryptedWithClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "ENCRYPTED WITH :")
        self.expression.print(spacer, level + 1)


class ColumnEncryptionKeyOption(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Column Encryption Key :")
        self.expression.print(spacer, level + 1)


class EncryptionTypeOption(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Encryption Type : {self.value}")


class AlgorithmOption(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Algorithm : {self.value}")


class AllowEncryptedValueModification(OptionOnOff):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Allow Encrypted Value Modification : " + ("ON" if self.on else "OFF"))


class BeginEndFunctionBody(ASTNode):
    def __init__(self, return_val, statements):
        self.return_val = return_val
        self.statements = statements

    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level + "Function Body :")

        if self.statements:
            print(spacer * (level + 1) + "Statments :")
            self.statements.print(spacer, level + 2)

        if self.return_val:
            print(spacer * (level + 1) + "Return Value :")
            self.return_val.print(spacer, level + 2)



class ReturnFuctionBody(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level + "Function Body :")
        print(spacer * (level + 1) + "Return Value :")
        self.expression.print(spacer, level + 2)


class TableReturnType(ASTNode):
    def print(self, spacer="  ", level=0):
        self.self_print(spacer * level + "Table Return Type")


class UserTableReturnType(ASTNode):
    def __init__(self, name, table_type):
        self.name = name
        self.table_type = table_type

    def print(self, spacer="  ", level=0):
        self.name.print(spacer, level + 1)
        self.table_type.print(spacer, level + 1)
