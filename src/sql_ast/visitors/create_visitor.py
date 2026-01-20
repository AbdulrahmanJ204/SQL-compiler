from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.basic_nodes import ItemsList
from sql_ast.ast_nodes.create_nodes import *


class CreateVisitor(SQLParserVisitor):

    def visitCreate_table(self, ctx: SQLParser.Create_tableContext):
        full_table_name = self.visit(ctx.full_table_name())
        create_table_element_list = self.visit(ctx.create_table_body())
        table_on_clause = self.visit(ctx.table_on_clause()) if ctx.table_on_clause() else None
        table_with_clause = self.visit(ctx.table_with_clause()) if ctx.table_with_clause() else None

        return CreateTable(full_table_name, create_table_element_list, table_on_clause, table_with_clause)

    def visitTable_on_clause(self, ctx: SQLParser.Table_on_clauseContext):
        partition_target = self.visit(ctx.partition_target())
        return TableOnClause(partition_target)

    def visitCreate_table_body(self, ctx: SQLParser.Create_table_bodyContext):
        return self.visit(ctx.create_table_element_list())

    def visitCreate_table_element_list(self, ctx: SQLParser.Create_table_element_listContext):
        return ItemsList([self.visit(child) for child in ctx.create_table_element()])

    def visitColumn_set_definition(self, ctx: SQLParser.Column_set_definitionContext):
        return SingleValueNode(ctx.getText())

    def visitTable_index(self, ctx: SQLParser.Table_indexContext):
        index_name = ctx.index_name().getText()
        body = self.visit(ctx.table_index_body())
        return TableIndex(index_name, body)

    def visitTable_index_rowstore(self, ctx: SQLParser.Table_index_rowstoreContext):
        unique_clustered = self.visit(ctx.unique_clustered_clause()) if ctx.unique_clustered_clause() else None
        index_column_list = self.visit(ctx.index_colomn_list()) if ctx.index_colomn_list() else None
        include_clause = self.visit(ctx.include_clause()) if ctx.include_clause() else None
        where_clause = self.visit(ctx.where_clause_for_index()) if ctx.where_clause_for_index() else None
        index_with_clause = self.visit(ctx.index_with_clause()) if ctx.index_with_clause() else None
        index_on_clause = self.visit(ctx.index_on_clause()) if ctx.index_on_clause() else None

        return TableIndexRowstore(unique_clustered, index_column_list, include_clause, where_clause,
                                   index_with_clause, index_on_clause)

    def visitTable_index_columnstore(self, ctx: SQLParser.Table_index_columnstoreContext):
        clustered_columnstore = self.visit(ctx.clustered_columnstroe_clause()) if ctx.clustered_columnstroe_clause() else None
        index_column_list = self.visit(ctx.index_colomn_list()) if ctx.index_colomn_list() else None
        include_clause = self.visit(ctx.include_clause()) if ctx.include_clause() else None
        where_clause = self.visit(ctx.where_clause_for_index()) if ctx.where_clause_for_index() else None
        index_with_clause = self.visit(ctx.index_with_clause()) if ctx.index_with_clause() else None
        index_on_clause = self.visit(ctx.index_on_clause()) if ctx.index_on_clause() else None

        return TableIndexColumnstore(clustered_columnstore, index_column_list, include_clause, where_clause,
                                      index_with_clause, index_on_clause)

    def visitUnique_clustered_clause(self, ctx: SQLParser.Unique_clustered_clauseContext):
        return UniqueClusteredClause(ctx.getText())

    def visitClustered_columnstroe_clause(self, ctx: SQLParser.Clustered_columnstroe_clauseContext):
        return ClusteredColumnstoreClause(ctx.getText())

    def visitIndex_colomn_list(self, ctx: SQLParser.Index_colomn_listContext):
        return ItemsList([self.visit(child) for child in ctx.index_column()])

    def visitIndex_column(self, ctx: SQLParser.Index_columnContext):
        name = self.visit(ctx.full_column_name())
        order = "DESC" if ctx.DESC() else "ASC"
        return IndexColumn(name, order)

    def visitInclude_clause(self, ctx: SQLParser.Include_clauseContext):
        columns = ItemsList([self.visit(child) for child in ctx.full_column_name()])
        return IncludeClause(columns)

    def visitWhere_clause_for_index(self, ctx: SQLParser.Where_clause_for_indexContext):
        return self.visit(ctx.search_condition())

    def visitCreate_index(self, ctx: SQLParser.Create_indexContext):
        index_name = ctx.index_name().getText()
        full_table_name = self.visit(ctx.full_table_name())
        unique = ctx.UNIQUE() is not None
        columnstore = ctx.COLUMNSTORE() is not None
        
        clustered = False
        if ctx.index_clustering():
            clustering_text = ctx.index_clustering().getText()
            clustered = clustering_text == "CLUSTERED"
        
        index_column_list = self.visit(ctx.index_column_list()) if ctx.index_column_list() else None
        include_clause = self.visit(ctx.include_clause()) if ctx.include_clause() else None
        where_clause = self.visit(ctx.where_clause_for_index()) if ctx.where_clause_for_index() else None
        index_with_clause = self.visit(ctx.index_with_clause()) if ctx.index_with_clause() else None
        index_on_clause = self.visit(ctx.index_on_clause()) if ctx.index_on_clause() else None

        return CreateIndex(index_name, full_table_name, index_column_list, unique, clustered, columnstore,
                           include_clause, where_clause, index_with_clause, index_on_clause)

    def visitIndex_on_clause(self, ctx: SQLParser.Index_on_clauseContext):
        partition_target = self.visit(ctx.partition_target())
        return IndexOnClause(partition_target)

    def visitIndex_column_list(self, ctx: SQLParser.Index_column_listContext):
        return ItemsList([self.visit(c) for c in ctx.index_column()])

    def visitIndex_with_clause(self, ctx: SQLParser.Index_with_clauseContext):
        options = ItemsList([self.visit(option) for option in ctx.index_option()])
        return IndexWithClause(options)

    def visitIndex_option(self, ctx: SQLParser.Index_optionContext):
        if ctx.index_common_option():
            return self.visit(ctx.index_common_option())
        elif ctx.DATA_COMPRESSION():
            compression_kind = ctx.getChild(2).getText()  # NONE, ROW, PAGE
            return IndexOption("DATA_COMPRESSION", SingleValueNode(compression_kind))
        elif ctx.xml_compression_option():
            return self.visit(ctx.xml_compression_option())

    def visitCreate_view(self, ctx: SQLParser.Create_viewContext):
        name = self.visit(ctx.full_table_name())
        select = self.visit(ctx.select_statement())
        
        view_column_list = None
        if ctx.view_column_list():
            columns = [id.getText() for id in ctx.view_column_list().IDENTIFIER()]
            view_column_list = ViewColumnList(ItemsList([SingleValueNode(col) for col in columns]))
        
        view_with_attributes = None
        if ctx.view_with_attributes():
            attributes = ItemsList([self.visit(attr) for attr in ctx.view_with_attributes().view_attribute()])
            view_with_attributes = ViewWithAttributes(attributes)
        
        view_check_option = self.visit(ctx.view_check_option()) if ctx.view_check_option() else None
        
        return CreateView(name, select, view_column_list, view_with_attributes, view_check_option)

    def visitCreate_user(self, ctx: SQLParser.Create_userContext):
        name = self.visit(ctx.user_name())
        core = self.visit(ctx.create_user_core()) if ctx.create_user_core() else None
        return CreateUser(name, core)

    def visitCreate_user_core(self, ctx: SQLParser.Create_user_coreContext):
        if ctx.LOGIN():
            login_name = self.visit(ctx.login_name())
            options = self.visit(ctx.with_user_options()) if ctx.with_user_options() else None
            return CreateUserCore("FOR_LOGIN", login_name=login_name, options=options)
        elif ctx.PASSWORD():
            password = self.visit(ctx.literal())
            options_list = [self.visit(opt) for opt in ctx.create_user_option()] if ctx.create_user_option() else []
            options = WithUserOptions(ItemsList(options_list)) if options_list else None
            return CreateUserCore("WITH_PASSWORD", password=password, options=options)
        elif ctx.WITHOUT():
            options = self.visit(ctx.with_user_options()) if ctx.with_user_options() else None
            return CreateUserCore("WITHOUT_LOGIN", options=options)
        elif ctx.from_external_provider_clause():
            external_provider = self.visit(ctx.from_external_provider_clause())
            return CreateUserCore("EXTERNAL_PROVIDER", options=external_provider)
        elif ctx.with_limited_user_options():
            options = self.visit(ctx.with_limited_user_options())
            return CreateUserCore("LIMITED_OPTIONS", options=options)

    def visitFrom_external_provider_clause(self, ctx: SQLParser.From_external_provider_clauseContext):
        limited_options = self.visit(ctx.with_limited_user_options()) if ctx.with_limited_user_options() else None
        return FromExternalProviderClause(limited_options)

    def visitWith_user_options(self, ctx: SQLParser.With_user_optionsContext):
        options = ItemsList([self.visit(opt) for opt in ctx.create_user_option()])
        return WithUserOptions(options)

    def visitWith_limited_user_options(self, ctx: SQLParser.With_limited_user_optionsContext):
        options = ItemsList([self.visit(opt) for opt in ctx.limited_user_option()])
        return WithLimitedUserOptions(options)

    def visitCreate_user_option(self, ctx: SQLParser.Create_user_optionContext):
        if ctx.DEFAULT_SCHEMA():
            schema = self.visit(ctx.full_table_name())
            return CreateUserOption("DEFAULT_SCHEMA", schema)
        elif ctx.default_language_eq_user_option():
            return self.visit(ctx.default_language_eq_user_option())
        elif ctx.SID():
            sid = self.visit(ctx.sid_value())
            return CreateUserOption("SID", sid)

    def visitLimited_user_option(self, ctx: SQLParser.Limited_user_optionContext):
        if ctx.DEFAULT_SCHEMA():
            schema = self.visit(ctx.full_table_name())
            return LimitedUserOption("DEFAULT_SCHEMA", schema)
        elif ctx.allow_encrypted_value_modifications_user_option():
            return self.visit(ctx.allow_encrypted_value_modifications_user_option())

    def visitSid_value(self, ctx: SQLParser.Sid_valueContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return SingleValueNode(ctx.IDENTIFIER().getText())

    def visitCreate_login(self, ctx: SQLParser.Create_loginContext):
        name = SingleValueNode(ctx.login_name().getText())
        core = self.visit(ctx.create_login_core())
        return CreateLogin(name, core)

    def visitCreate_login_core(self, ctx: SQLParser.Create_login_coreContext):
        password = self.visit(ctx.literal())
        options_list = [self.visit(opt) for opt in ctx.create_login_option()] if ctx.create_login_option() else []
        options = ItemsList(options_list) if options_list else None
        return CreateLoginCore(password, options)

    def visitCreate_login_option(self, ctx: SQLParser.Create_login_optionContext):
        if ctx.DEFAULT_DATABASE():
            database = self.visit(ctx.full_table_name())
            return CreateLoginOption("DEFAULT_DATABASE", database)
        elif ctx.default_language_eq_user_option():
            return self.visit(ctx.default_language_eq_user_option())
        elif ctx.CHECK_POLICY():
            value = SingleValueNode("ON" if ctx.ON() else "OFF")
            return CreateLoginOption("CHECK_POLICY", value)
        elif ctx.CHECK_EXPIRATION():
            value = SingleValueNode("ON" if ctx.ON() else "OFF")
            return CreateLoginOption("CHECK_EXPIRATION", value)
        elif ctx.SID():
            sid = self.visit(ctx.sid_value())
            return CreateLoginOption("SID", sid)

    def visitGrant_statement(self, ctx: SQLParser.Grant_statementContext):
        target = self.visit(ctx.grant_target())
        grantee = self.visit(ctx.full_table_name())
        return GrantStatement("IMPERSONATE", target, grantee)

    def visitGrant_target(self, ctx: SQLParser.Grant_targetContext):
        user_name = self.visit(ctx.user_name())
        return GrantTarget(user_name)

    def visitTable_with_clause(self, ctx: SQLParser.Table_with_clauseContext):
        options = ItemsList([self.visit(opt) for opt in ctx.table_option_create()])
        return TableWithClause(options)

    def visitTable_option_create(self, ctx: SQLParser.Table_option_createContext):
        if ctx.DATA_COMPRESSION():
            compression_kind = self.visit(ctx.data_compression_kind())
            partitions = self.visit(ctx.table_partitions_clause()) if ctx.table_partitions_clause() else None
            return TableOptionCreate("DATA_COMPRESSION", compression_kind, partitions)
        elif ctx.LOCK_ESCALATION():
            lock_value = SingleValueNode(ctx.lock_escalation_value().getText())
            return TableOptionCreate("LOCK_ESCALATION", lock_value)
        elif ctx.xml_compression_option():
            xml_option = self.visit(ctx.xml_compression_option())
            return TableOptionCreate("XML_COMPRESSION", xml_option)

    def visitData_compression_kind(self, ctx: SQLParser.Data_compression_kindContext):
        return DataCompressionKind(ctx.getText())

    def visitTable_partitions_clause(self, ctx: SQLParser.Table_partitions_clauseContext):
        expressions = ItemsList([self.visit(expr) for expr in ctx.partition_number_expression()])
        return TablePartitionsClause(expressions)

    def visitCreate_function(self, ctx: SQLParser.Create_functionContext):
        name = self.visit(ctx.function_name())
        or_alter = ctx.ALTER() is not None
        
        parameters = self.visit(ctx.function_parameters()) if ctx.function_parameters() else None
        return_type = self.visit(ctx.function_return_type())
        
        options = None
        if ctx.function_options():
            opts = ItemsList([self.visit(opt) for opt in ctx.function_options().function_option()])
            options = FunctionOptions(opts)
        
        body = self.visit(ctx.function_body())
        
        return CreateFunction(name, parameters, return_type, body, or_alter=or_alter, options=options)

    def visitFunction_options(self, ctx: SQLParser.Function_optionsContext):
        return ItemsList([self.visit(opt) for opt in ctx.function_option()])

    def visitFunction_option(self, ctx: SQLParser.Function_optionContext):
        if ctx.ENCRYPTION():
            return FunctionOption("ENCRYPTION")
        elif ctx.SCHEMABINDING():
            return FunctionOption("SCHEMABINDING")
        elif ctx.RETURNS() and ctx.NULL():
            if ctx.ON():
                return FunctionOption("RETURNS NULL ON NULL INPUT")
            else:
                return FunctionOption("CALLED ON NULL INPUT")
        elif ctx.execute_as_clause():
            return self.visit(ctx.execute_as_clause())
        elif ctx.INLINE():
            value = "ON" if ctx.ON() else "OFF"
            return FunctionOption(f"INLINE = {value}")

    def visitExecute_as_clause(self, ctx: SQLParser.Execute_as_clauseContext):
        if ctx.CALLER():
            return ExecuteAsClause("CALLER")
        elif ctx.SELF():
            return ExecuteAsClause("SELF")
        elif ctx.OWNER():
            return ExecuteAsClause("OWNER")
        elif ctx.literal():
            literal_value = self.visit(ctx.literal())
            return ExecuteAsClause(f"'{literal_value}'")
