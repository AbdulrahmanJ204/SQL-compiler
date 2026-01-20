from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.alter_nodes import *
from ..ast_nodes.basic_nodes import ItemsList, SingleValueNode, Range, Literal


# from ..ast_nodes.truncate_nodes import *

class AlterVisitor(SQLParserVisitor):

    def visitAlter_table(self, ctx: SQLParser.Alter_tableContext):
        table = self.visit(ctx.full_table_name())
        alter_table = self.visit(ctx.alter_table_with_clause()) if ctx.alter_table_with_clause() else None
        action = self.visit(ctx.table_action())
        return AlterTableStatement(table, action, alter_table)

    def visitAlter_table_with_clause(self, ctx: SQLParser.Alter_table_with_clauseContext):
        return AlterTableWithClause(check=ctx.CHECK() is not None)

    def visitTable_change_tracking(self, ctx: SQLParser.Table_change_trackingContext):
        enabled = ctx.ENABLE() is not None
        change_with = self.visit(ctx.change_tracking_with_clause()) if ctx.change_tracking_with_clause() else None
        return TableChangeTracking(enabled, change_with)

    def visitChange_tracking_with_clause(self, ctx: SQLParser.Change_tracking_with_clauseContext):
        on = ctx.ON() is not None
        return ChangeTrackingWithClause(on)

    def visitTable_set_option(self, ctx: SQLParser.Table_set_optionContext):
        return SetTableOption(self.visit(ctx.table_option_list()))

    def visitTable_option_list(self, ctx: SQLParser.Table_option_listContext):
        return ItemsList([self.visit(option) for option in ctx.table_option()])

    def visitTable_option(self, ctx: SQLParser.Table_optionContext):
        return TableOptionLeaf(ctx.lock_escalation_value().getText())

    def visitTable_alter_column(self, ctx: SQLParser.Table_alter_columnContext):
        col = self.visit(ctx.full_column_name())
        action = self.visit(ctx.alter_column_action())
        return AlterTableColumn(col, action)

    def visitAlter_columnt_type(self, ctx: SQLParser.Alter_columnt_typeContext):
        col_type = self.visit(ctx.cJolumn_type())
        collate = self.visit(ctx.collate_clause()) if ctx.collate_clause() else None
        encrypted_with = self.visit(ctx.encrypted_with_clause()) if ctx.encrypted_with_clause() else None
        nullable = self.visit(ctx.nullability_clause())
        sparse = ctx.SPARSE() is not None
        alter_with_clause = self.visit(ctx.alter_column_with_clause()) if ctx.alter_column_with_clause() else None
        return AlterColumnType(col_type, collate, encrypted_with, nullable, sparse, alter_with_clause)

    def visitAlter_column_with_clause(self, ctx: SQLParser.Alter_column_with_clauseContext):
        return ItemsList([self.visit(option) for option in ctx.alter_column_option()])

    def visitCollate_clause(self, ctx: SQLParser.Collate_clauseContext):
        return CollateClause(self.visit(ctx.full_table_name()))

    def visitAlter_column_option_action(self, ctx: SQLParser.Alter_column_option_actionContext):
        return AlterColumnOptionAction(ctx.getChild(0).getText(),
                                       self.visit(ctx.alter_column_option()))

    def visitAlter_column_option(self, ctx: SQLParser.Alter_column_optionContext):
        if ctx.online_eq_online_option()():
            return self.visit(ctx.online_eq_online_option())
        elif ctx.NOT():
            return AlterColumnOptionLeaf("NOT FOR REPLICATION ")

        return AlterColumnOptionLeaf(ctx.getChild(0).getText())

    ######################################

    def visitTable_add(self, ctx: SQLParser.Table_addContext):
        return TableAddItem(self.visit(ctx.table_add_item_list()))

    def visitTable_add_item_list(self, ctx: SQLParser.Table_add_item_listContext):
        return ItemsList([self.visit(item) for item in ctx.table_add_item()])

    ###############
    def visitTable_rename_column(self, ctx: SQLParser.Table_rename_columnContext):
        old_name = self.visit(ctx.full_column_name())
        new_name = ctx.IDENTIFIER().getText()
        return TableRenameColumn(old_name, new_name)  # TODO :new_name is ID

    def visitTable_check_constraint(self, ctx: SQLParser.Table_check_constraintContext):
        check = ctx.CHECK() is not None
        target = ctx.constraint_target().getText()
        return TableCheckConstraint(target, check)

    ##############################

    def visitTable_drop_constraint_simple(self, ctx: SQLParser.Table_drop_constraint_simpleContext):
        ct_name = ctx.constraint_name().getText()
        drop_with_clause = self.visit(ctx.drop_constraint_with_clause()) if ctx.drop_constraint_with_clause() else None
        return DropTableConstraintWith(ct_name, drop_with_clause)

    def visitDrop_constraint_with_clause(self, ctx: SQLParser.Drop_constraint_with_clauseContext):
        return self.visit(ctx.drop_constraint_option_list())

    def visitDrop_constraint_option_list(self, ctx: SQLParser.Drop_constraint_option_listContext):
        return ItemsList([self.visit(option) for option in ctx.drop_constraint_option()])

    def visitTable_drop(self, ctx: SQLParser.Table_dropContext):
        spec_list = self.visit(ctx.drop_spec_list()) if ctx.drop_spec_list() else None
        return DropTableItems(spec_list)

    def visitDrop_spec_list(self, ctx: SQLParser.Drop_spec_listContext):
        return ItemsList([self.visit(spec) for spec in ctx.drop_spec()])

    def visitDrop_constraint_spec(self, ctx: SQLParser.Drop_constraint_specContext):
        if_exists = ctx.if_exists() is not None
        constraint_list = self.visit(ctx.constraint_name_list())
        drop_with_clause = self.visit(ctx.drop_constraint_with_clause()) if ctx.drop_constraint_with_clause() else None
        return DropConstraintSpec(constraint_list, if_exists, drop_with_clause)

    def visitConstraint_name_list(self, ctx: SQLParser.Constraint_name_listContext):
        return ItemsList([self.visit(name) for name in ctx.constraint_name()])

    def visitDrop_column_spec(self, ctx: SQLParser.Drop_column_specContext):
        if_exists = ctx.if_exists() is not None
        column_list = self.visit(ctx.column_name_list())
        return DropColumnSpec(column_list, if_exists)

    def visitColumn_name_list(self, ctx: SQLParser.Column_name_listContext):
        return ItemsList([self.visit(col) for col in ctx.full_column_name()])

    #################################
    def visitAlter_index(self, ctx: SQLParser.Alter_indexContext):
        index = ctx.getChild(2).getText()
        table = self.visit(ctx.full_table_name())
        action = self.visit(ctx.alter_index_action())
        return AlterIndex(index, table, action)

    def visitSingle_word_indx_action(self, ctx: SQLParser.Single_word_indx_actionContext):
        return SingleWordAlterIndexAction(ctx.getChild(0).getText())

    def visitSet_clause(self, ctx: SQLParser.Set_clauseContext):
        return SetIndexOptionClause(self.visit(ctx.set_index_option_list()))

    def visitSet_index_option_list(self, ctx: SQLParser.Set_index_option_listContext):
        return ItemsList([self.visit(option) for option in ctx.set_index_option()])

    def visitAllow_row_locks_option(self, ctx: SQLParser.Allow_row_locks_optionContext):
        return AllowRowLocks(on=ctx.ON() is not None)

    #
    def visitAllow_page_locks_option(self, ctx: SQLParser.Allow_page_locks_optionContext):
        return AllowPageLocks(on=ctx.ON() is not None)

    #
    def visitOptimize_for_squential_key_option(self, ctx: SQLParser.Optimize_for_squential_key_optionContext):
        return OptimizeForSequentialKey(on=ctx.ON() is not None)

    #
    def visitIgnore_dup_key_option(self, ctx: SQLParser.Ignore_dup_key_optionContext):
        return IgnoreDupKey(on=ctx.ON() is not None)

    #
    def visitStatistics_no_recompute_option(self, ctx: SQLParser.Statistics_no_recompute_optionContext):
        return StatisticsNoRecompute(on=ctx.ON() is not None)

    #
    def visitCompression_delay_option(self, ctx: SQLParser.Compression_delay_optionContext):
        return ComperssionDelayOption(delay_value=self.visit(ctx.compression_delay_value()))

    #
    def visitCompression_delay_value(self, ctx: SQLParser.Compression_delay_valueContext):
        if ctx.NUMBER_LITERAL():
            return Literal(ctx.NUMBER_LITERAL().getText())

        return self.visit(ctx.expression())

    #
    # ################################
    def visitRebuild_clause(self, ctx: SQLParser.Rebuild_clauseContext):
        return RebuildClause(body=self.visit(ctx.rebuild_body()))

    #
    def visitRebuild_body1(self, ctx: SQLParser.Rebuild_body1Context):
        return RebuildBody(self.visit(ctx.par_eq_all()) if ctx.par_eq_all() else None,
                           self.visit(ctx.rebuild_with_options()) if ctx.rebuild_with_options() else None)

    #
    def visitRebuild_body2(self, ctx: SQLParser.Rebuild_body2Context):
        return RebuildBody(self.visit(ctx.par_eq_lit()), self.visit(ctx.single_partition_rebuild_with_options()))

    #
    def visitPar_eq_all(self, ctx: SQLParser.Par_eq_allContext):
        return PartitionEqualAll()

    #
    def visitPar_eq_lit(self, ctx: SQLParser.Par_eq_litContext):
        return PartitionEqualLiteral(ctx.NUMBER_LITERAL().getText())

    #
    def visitRebuild_with_options(self, ctx: SQLParser.Rebuild_with_optionsContext):
        return RebuildWithOptions(ItemsList([self.visit(op) for op in ctx.rebuild_index_option()]))

    def visitSingle_partition_rebuild_with_options(self, ctx: SQLParser.Single_partition_rebuild_with_optionsContext):
        return RebuildWithOptions(
            ItemsList([self.visit(option) for option in ctx.single_partition_rebuild_index_option()]))

    # ######################################
    def visitReorganize_clause(self, ctx: SQLParser.Reorganize_clauseContext):
        return ReorganizeClause(self.visit(ctx.reorganize_body()))

    def visitReorganize_body(self, ctx: SQLParser.Reorganize_bodyContext):
        return ReorganizeBody(self.visit(ctx.par_eq_lit()) if ctx.par_eq_lit() else None,
                              self.visit(ctx.reorganize_with_options()) if ctx.reorganize_with_options() else None
                              )

    #
    def visitReorganize_with_options(self, ctx: SQLParser.Reorganize_with_optionsContext):
        return ReorganizeWithOptions(ItemsList([self.visit(option) for option in ctx.reorganize_option()]))

    #
    def visitResume_clause(self, ctx: SQLParser.Resume_clauseContext):
        return ResumeClause(self.visit(ctx.resume_with_options()) if ctx.resume_with_options() else None)

    #
    def visitResume_with_options(self, ctx: SQLParser.Resume_with_optionsContext):
        return ResumeWithOptions(ItemsList([self.visit(option) for option in ctx.resumable_index_option()]))

    #
    def visitXml_compression_option(self, ctx: SQLParser.Xml_compression_optionContext):
        return XmlCompressionOption(on=ctx.ON() is not None)

    #
    def visitXml_compression_option_with_rebuild(self, ctx: SQLParser.Xml_compression_option_with_rebuildContext):
        return XmlCompressionOptionWithRebuild(self.visit(ctx.xml_compression_option()), self.visit(
            ctx.rebuild_partitions_clause()) if ctx.rebuild_partitions_clause() else None)

    #
    def visitStatistics_incremental_option(self, ctx: SQLParser.Statistics_incremental_optionContext):
        return StatisticsIncrementalOption(on=ctx.ON() is not None)

    #
    def visitSort_in_temp_db_option(self, ctx: SQLParser.Sort_in_temp_db_optionContext):
        return SortInTempDBOption(on=ctx.ON() is not None)

    #
    def visitResumable_option(self, ctx: SQLParser.Resumable_optionContext):
        return ResumableOption(on=ctx.ON() is not None)

    #
    def visitMax_dop_expression_option(self, ctx: SQLParser.Max_dop_expression_optionContext):
        return MaxDopExpressionOption(self.visit(ctx.expression()))

    #
    def visitRebuild_compression_kind(self, ctx: SQLParser.Rebuild_compression_kindContext):
        return RebuildCompressionKind(ctx.getText())

    def visitRebuild_partitions_clause(self, ctx: SQLParser.Rebuild_partitions_clauseContext):
        return OnPartitionsClause(ItemsList([self.visit(rng) for rng in ctx.partition_range()]))

    #
    def visitPartition_range(self, ctx: SQLParser.Partition_rangeContext):
        if ctx.TO():
            return Range(ctx.NUMBER_LITERAL(0).getText(), ctx.NUMBER_LITERAL(1).getText())
        return Range(0, ctx.NUMBER_LITERAL(0).getText())  # TODO : check if from is 0 or 1

    #
    def visitLob_compaction_option(self, ctx: SQLParser.Lob_compaction_optionContext):
        return LobCompactionOption(on=ctx.ON() is not None)

    def visitCompress_all_row_groups_option(self, ctx: SQLParser.Compress_all_row_groups_optionContext):
        return CompressAllRowGroupsOption(on=ctx.ON() is not None)

    #
    # #######################################
    # # This defined in Basic parser
    def visitOnline_eq_online_option(self, ctx: SQLParser.Online_eq_online_optionContext):
        return OnlineOption(ctx.ON() is not None, self.visit(
            ctx.low_priority_lock_wait_clause()) if ctx.low_priority_lock_wait_clause() else None)
    #
    def visitLow_priority_lock_wait_clause(self, ctx: SQLParser.Low_priority_lock_wait_clauseContext):
        return self.visit(ctx.low_priority_lock_wait())
    #
    def visitLow_priority_lock_wait(self, ctx:SQLParser.Low_priority_lock_waitContext):
        mx_dur_mins = self.visit(ctx.mx_duration_expr_option())
        abort_after_wait = ctx.getChild(6).getText()
        return LowPriorityLockWait(mx_dur_mins, abort_after_wait)
    #
    # ###################################
    def visitAlter_view(self, ctx:SQLParser.Alter_viewContext):
        table = self.visit(ctx.full_table_name())
        col_list = self.visit(ctx.column_list()) if ctx.column_list() else None
        attribute_clause = self.visit(ctx.view_attribute_clause()) if ctx.view_attribute_clause() else None
        select_st = self.visit(ctx.select_statement())
        check_option = self.visit(ctx.view_check_option()) if ctx.view_check_option() else None
        return AlterViewStatement(table , select_st,col_list , attribute_clause  , check_option)
    #
    def visitView_attribute_clause(self, ctx:SQLParser.View_attribute_clauseContext):
        return WithViewAttributes(ItemsList([self.visit(attr) for attr in ctx.view_attribute()]))
    #
    #
    def visitAlter_user(self, ctx:SQLParser.Alter_userContext):
        return AlterUserStatement(self.visit(ctx.user_name()), self.visit(ctx.user_option_list()))
    #
    def visitUser_name(self, ctx:SQLParser.User_nameContext):
        return UserNameNode(ctx.getText())

    def visitUser_option_list(self, ctx:SQLParser.User_option_listContext):
        return WithUserOptions(ItemsList([self.visit(option) for option in ctx.user_option()]))
    #
    def visitId_eq_id_user_option(self, ctx:SQLParser.Id_eq_id_user_optionContext):
        return IdentifierEqualIdentifierOption(ctx.IDENTIFIER(0).getText() , ctx.IDENTIFIER(1).getText())
    #
    def visitDefault_schema_eq_user_option(self, ctx:SQLParser.Default_schema_eq_user_optionContext):
        return DefaultSchemaEqualOption(ctx.getChild(2).getText())
    #
    #
    def visitLogin_eq_id_user_option(self, ctx:SQLParser.Login_eq_id_user_optionContext):
        return LoginOption(ctx.getChild(2).getText())
    #
    def visitPassword_eq_user_option(self, ctx:SQLParser.Password_eq_user_optionContext):
        return PasswordAndOldPasswordOption(self.visit(ctx.literal(0)) , self.visit(ctx.literal(1)) if len(ctx.literal(0).getText()) > 0 else None)
    #
    def visitDefault_language_eq_user_option(self, ctx:SQLParser.Default_language_eq_user_optionContext):
        return DefaultLanguageOption(ctx.default_language_value().getText())

    def visitAllow_encrypted_value_modifications_user_option(self, ctx:SQLParser.Allow_encrypted_value_modifications_user_optionContext):
        return AllowEncryptedValueModification(ctx.ON() is not None)
