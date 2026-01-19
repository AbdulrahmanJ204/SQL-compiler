parser grammar AlterParser;

options { tokenVocab = SQLLexer; }

import BasicParser;
alter_statement
    : alter_table
    | alter_index
    | alter_view
    | alter_user
    // | alter_function
    ;

alter_table
    : ALTER TABLE full_table_name alter_table_with_clause? table_action SEMI?
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
    | table_set_option
    | table_change_tracking
    ;
table_change_tracking
    : (ENABLE | DISABLE) CHANGE_TRACKING change_tracking_with_clause?;

change_tracking_with_clause
    : WITH LPAREN TRACK_COLUMNS_UPDATED EQ (ON | OFF) RPAREN;

table_set_option
    : SET LPAREN table_option (COMMA table_option)* RPAREN;
table_option
    : LOCK_ESCALATION EQ lock_escalation_value;
lock_escalation_value
    : AUTO
    | TABLE
    | DISABLE
    ;

constraint_target: IDENTIFIER | ALL;


table_alter_column
    : ALTER COLUMN full_column_name alter_column_action;

alter_column_action
    : column_type
      collate_clause?
      encrypted_with_clause?
      nullability_clause? // todo : check if i can remove the ? if it has a defaulf value of null
      SPARSE?
      alter_column_with_clause?
    | alter_column_option_action
    ;

alter_column_with_clause
    : WITH LPAREN alter_column_option (COMMA alter_column_option)* RPAREN;

alter_column_option
    : ONLINE EQ (ON | OFF) ;

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
    ;

table_add
    : ADD table_add_item (COMMA table_add_item)*;

table_add_item
    : column_definition
    | table_constraint
    ;

table_rename_column
    : RENAME COLUMN full_column_name TO IDENTIFIER;

table_check_constraint
    : CHECK   CONSTRAINT constraint_target
    | NOCHECK CONSTRAINT constraint_target
    ;

table_drop_constraint_simple
    : DROP CONSTRAINT constraint_name drop_constraint_with_clause?;

constraint_name: IDENTIFIER;

drop_constraint_with_clause
    : WITH LPAREN drop_constraint_option (COMMA drop_constraint_option)* RPAREN;

drop_constraint_option : ONLINE EQ (ON | OFF)  ;

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
    | DISABLE
    | reorganize_clause
    | set_clause
    | resume_clause
    | PAUSE
    | ABORT
    ;

set_clause
    : SET LPAREN set_index_option (COMMA set_index_option)* RPAREN;

set_index_option
    : ALLOW_ROW_LOCKS EQ (ON | OFF)
    | ALLOW_PAGE_LOCKS EQ (ON | OFF)
    | OPTIMIZE_FOR_SEQUENTIAL_KEY EQ (ON | OFF)
    | IGNORE_DUP_KEY EQ (ON | OFF)
    | STATISTICS_NORECOMPUTE EQ (ON | OFF)
    | COMPRESSION_DELAY EQ (NUMBER_LITERAL | expression) (MINUTES)?
    ;
rebuild_clause : REBUILD rebuild_body ;

rebuild_body
    : rebuild_with_options?
    | partition_spec rebuild_with_options?
    ;

partition_spec
    : PARTITION EQ ALL
    | PARTITION EQ NUMBER_LITERAL ;

rebuild_with_options
    : WITH LPAREN rebuild_index_option (COMMA rebuild_index_option)* RPAREN;

single_partition_rebuild_with_options
    : WITH LPAREN single_partition_rebuild_index_option
           (COMMA single_partition_rebuild_index_option)* RPAREN;

reorganize_clause: REORGANIZE reorganize_body;

reorganize_body
    : (PARTITION EQ NUMBER_LITERAL)? reorganize_with_options?;

reorganize_with_options
    : WITH LPAREN reorganize_option (COMMA reorganize_option)* RPAREN;

resume_clause
    : RESUME resume_with_options?;

resume_with_options
    : WITH LPAREN resumable_index_option (COMMA resumable_index_option)* RPAREN;

rebuild_index_option
    : index_common_option
    | STATISTICS_NORECOMPUTE EQ (ON | OFF)
    | STATISTICS_INCREMENTAL EQ (ON | OFF)
    | SORT_IN_TEMPDB EQ (ON | OFF)
    | DATA_COMPRESSION EQ rebuild_compression_kind rebuild_partitions_clause?
    | XML_COMPRESSION EQ (ON | OFF) rebuild_partitions_clause?
    ;

single_partition_rebuild_index_option
    : SORT_IN_TEMPDB EQ (ON | OFF)
    | MAXDOP EQ expression
    | RESUMABLE EQ (ON | OFF)
    | MAX_DURATION EQ expression (MINUTES)?
    | DATA_COMPRESSION EQ rebuild_compression_kind
    | XML_COMPRESSION EQ (ON | OFF)
    | ONLINE EQ online_option
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
    : LOB_COMPACTION EQ (ON | OFF)
    | COMPRESS_ALL_ROW_GROUPS EQ (ON | OFF)
    ;
resumable_index_option
    : MAXDOP EQ expression
    | MAX_DURATION EQ expression (MINUTES)?
    | low_priority_lock_wait
    ;
online_option
    : ON low_priority_lock_wait_clause?
    | OFF;

low_priority_lock_wait_clause
    : LPAREN low_priority_lock_wait RPAREN;

low_priority_lock_wait
    : WAIT_AT_LOW_PRIORITY LPAREN
        MAX_DURATION EQ expression (MINUTES)?
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

view_attribute_clause: WITH view_attribute_list;

view_attribute_list
    : view_attribute (COMMA view_attribute)* ;

alter_user
    : ALTER USER user_name WITH user_option (COMMA user_option)* SEMI?;

user_option
    : IDENTIFIER EQ IDENTIFIER
    | DEFAULT_SCHEMA EQ (IDENTIFIER | NULL)
    | LOGIN EQ IDENTIFIER
    | PASSWORD EQ literal (OLD_PASSWORD EQ literal)?
    | DEFAULT_LANGUAGE EQ (NONE | literal | IDENTIFIER)
    | ALLOW_ENCRYPTED_VALUE_MODIFICATIONS EQ (ON | OFF);

/*alter_function
    : ALTER FUNCTION function_name function_parameters? returns_clause AS? function_body SEMI?;

returns_clause
    : RETURNS function_return_type SEMI;*/

