parser grammar AlterParser;

options { tokenVocab = SQLLexer; }

import BasicParser, CreateParser;
alter_statement
    : alter_table
    | alter_index
    | alter_view
    | alter_user
    // | alter_function
    ;

alter_table
    : ALTER TABLE full_table_name alter_table_with_clause? table_action (COMMA table_action)* SEMI?
    ;

alter_table_with_clause
    : WITH (CHECK | NOCHECK);

table_action
    : table_alter_column
    | table_add
    | table_rename_column
    | table_check_constraint
    | table_drop_constraint_simple
    | table_drop
    | alter_table_set_option
    | table_change_tracking
    ;
table_change_tracking
    : (ENABLE | DISABLE) CHANGE_TRACKING change_tracking_with_clause?;

change_tracking_with_clause
    : WITH LPAREN TRACK_COLUMNS_UPDATED EQ (ON | OFF) RPAREN;

alter_table_set_option
    : SET alter_table_option_list;
alter_table_option_list: LPAREN alter_table_option (COMMA alter_table_option)* RPAREN;

alter_table_option
    : LOCK_ESCALATION EQ lock_escalation_value;
lock_escalation_value
    : AUTO
    | TABLE
    | DISABLE
    ;



table_alter_column
    : ALTER COLUMN full_column_name alter_column_action;

alter_column_action
    : alter_columnt_type
    | alter_column_option_action
    ;

alter_columnt_type:
        column_type
      collate_clause?
      encrypted_with_clause?
      nullability_clause
      SPARSE?
      alter_column_with_clause?;

alter_column_with_clause
    : WITH LPAREN alter_column_option (COMMA alter_column_option)* RPAREN;


collate_clause
    : COLLATE full_table_name  ;

alter_column_option_action
    : ADD  alter_column_option
    | DROP alter_column_option
    ;

alter_column_option
    : SPARSE
    | ROWGUIDCOL
    | PERSISTED
    | NOT FOR REPLICATION
    | online_eq_online_option ;


table_add
    : ADD table_add_item_list ;

table_add_item_list: table_add_item (COMMA table_add_item)*;

table_add_item
    : column_definition
    | table_constraint
    ;

table_rename_column
    : RENAME COLUMN full_column_name TO IDENTIFIER;

table_check_constraint
    : (CHECK| NOCHECK) CONSTRAINT constraint_target
    ;
constraint_target: IDENTIFIER | ALL;




table_drop_constraint_simple
    : DROP CONSTRAINT constraint_name drop_constraint_with_clause?;

constraint_name: IDENTIFIER;

drop_constraint_with_clause
    : WITH LPAREN drop_constraint_option_list RPAREN;
drop_constraint_option_list: drop_constraint_option (COMMA drop_constraint_option)*;
drop_constraint_option : online_eq_online_option;

table_drop : DROP drop_spec_list? ;

drop_spec_list: drop_spec (COMMA drop_spec)* ;
drop_spec
    : drop_constraint_spec
    | drop_column_spec
    ;

drop_constraint_spec
    : (CONSTRAINT)? if_exists? constraint_name_list drop_constraint_with_clause? ;

constraint_name_list
    : constraint_name (COMMA constraint_name)*;

if_exists: IF EXISTS;

drop_column_spec
    : COLUMN if_exists? column_name_list;

column_name_list
    : full_column_name (COMMA full_column_name)*;








alter_index
    : ALTER INDEX (index_name | ALL) ON full_table_name alter_index_action SEMI?;

alter_index_action
    : rebuild_clause
    | single_word_indx_action
    | reorganize_clause
    | set_clause
    | resume_clause
    ;
single_word_indx_action: DISABLE
    | PAUSE
    | ABORT;

set_clause
    : SET LPAREN set_index_option_list  RPAREN;
set_index_option_list: set_index_option (COMMA set_index_option)*;
set_index_option
    : allow_row_locks_option
    | allow_page_locks_option
    | optimize_for_squential_key_option
    | ignore_dup_key_option
    | statistics_no_recompute_option
    | compression_delay_option

    ;

allow_row_locks_option: ALLOW_ROW_LOCKS EQ (ON | OFF) ;
allow_page_locks_option: ALLOW_PAGE_LOCKS EQ (ON | OFF) ;
optimize_for_squential_key_option: OPTIMIZE_FOR_SEQUENTIAL_KEY EQ (ON | OFF) ;
ignore_dup_key_option:IGNORE_DUP_KEY EQ (ON | OFF);
statistics_no_recompute_option : STATISTICS_NORECOMPUTE EQ (ON | OFF);
compression_delay_option:COMPRESSION_DELAY EQ compression_delay_value (MINUTES)?;
compression_delay_value: NUMBER_LITERAL | expression;
fill_factor_option : FILLFACTOR EQ literal;

rebuild_clause : REBUILD rebuild_body ;

rebuild_body
    :  rebuild_body1|rebuild_body2

    ;
rebuild_body1:par_eq_all ? rebuild_with_options?;
rebuild_body2:par_eq_lit single_partition_rebuild_with_options;

par_eq_all: PARTITION EQ ALL;
par_eq_lit: PARTITION EQ NUMBER_LITERAL;

rebuild_with_options
    : WITH LPAREN rebuild_index_option (COMMA rebuild_index_option)* RPAREN;

single_partition_rebuild_with_options
    : WITH LPAREN single_partition_rebuild_index_option
           (COMMA single_partition_rebuild_index_option)* RPAREN;

reorganize_clause: REORGANIZE reorganize_body;

reorganize_body
    : par_eq_lit? reorganize_with_options?;

reorganize_with_options
    : WITH LPAREN reorganize_option (COMMA reorganize_option)* RPAREN;

resume_clause
    : RESUME resume_with_options?;

resume_with_options
    : WITH LPAREN resumable_index_option (COMMA resumable_index_option)* RPAREN;

rebuild_index_option
    : index_common_option
    | statistics_no_recompute_option
    | statistics_incremental_option
    | sort_in_temp_db_option
    |data_compression_option_with_rebuild_partitions
    | xml_compression_option_with_rebuild
    |fill_factor_option
    ;

xml_compression_option:
     XML_COMPRESSION EQ (ON | OFF)
    ;

xml_compression_option_with_rebuild:
            xml_compression_option rebuild_partitions_clause?;

data_compression_option
    : DATA_COMPRESSION EQ rebuild_compression_kind ;
data_compression_option_with_rebuild_partitions
    : data_compression_option rebuild_partitions_clause?
    ;
statistics_incremental_option
    : STATISTICS_INCREMENTAL EQ (ON | OFF)
    ;
sort_in_temp_db_option
    : SORT_IN_TEMPDB EQ (ON | OFF)
    ;
single_partition_rebuild_index_option
    : sort_in_temp_db_option
    | max_dop_expression_option
    | resumable_option
    | mx_duration_expr_option
    | data_compression_option
    | xml_compression_option
    | online_eq_online_option
    ;


rebuild_compression_kind
    : NONE
    | ROW
    | PAGE
    | COLUMNSTORE
    | COLUMNSTORE_ARCHIVE
    ;

rebuild_partitions_clause
    : ON PARTITIONS LPAREN partition_range (COMMA partition_range)* RPAREN;

partition_range
    : NUMBER_LITERAL
    | NUMBER_LITERAL TO NUMBER_LITERAL
    ;

reorganize_option
    : lob_compaction_option
    | compress_all_row_groups_option
    ;

lob_compaction_option : LOB_COMPACTION EQ (ON | OFF)    ;
compress_all_row_groups_option : COMPRESS_ALL_ROW_GROUPS EQ (ON | OFF)    ;
resumable_index_option
    : max_dop_expression_option
    | mx_duration_expr_option
    | low_priority_lock_wait
    ;


low_priority_lock_wait_clause
    : LPAREN low_priority_lock_wait RPAREN;

low_priority_lock_wait
    : WAIT_AT_LOW_PRIORITY LPAREN
        mx_duration_expr_option
        COMMA
        ABORT_AFTER_WAIT EQ (NONE | SELF | BLOCKERS)
      RPAREN
    ;

alter_view
    : ALTER VIEW full_table_name
      column_list?
      view_attribute_clause?
      AS select_statement
      view_check_option?
      SEMI?
    ;

view_attribute_clause: WITH view_attribute (COMMA view_attribute)*;


alter_user
    : ALTER USER user_name WITH user_option_list SEMI?;
user_option_list:
 user_option (COMMA user_option)*;
user_option
    : id_eq_id_user_option
    |default_schema_eq_user_option
    |login_eq_id_user_option
    |password_eq_user_option
    |default_language_eq_user_option
    |allow_encrypted_value_modifications_user_option ;

id_eq_id_user_option:IDENTIFIER EQ IDENTIFIER ;
default_schema_eq_user_option:DEFAULT_SCHEMA EQ (IDENTIFIER | NULL);
login_eq_id_user_option:LOGIN EQ IDENTIFIER;
password_eq_user_option:PASSWORD EQ literal (OLD_PASSWORD EQ literal)?;
default_language_eq_user_option:DEFAULT_LANGUAGE EQ default_language_value;
allow_encrypted_value_modifications_user_option:ALLOW_ENCRYPTED_VALUE_MODIFICATIONS EQ (ON | OFF);


