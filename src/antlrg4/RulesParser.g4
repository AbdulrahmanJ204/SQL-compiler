parser grammar RulesParser;
options {
	tokenVocab = SQLLexer;
}

// ============================================ CATEGORY 1: DDL, DML & Query Structure (Person 1 &
// Person 2) ============================================

tsql_file:;
batch:;
sql_statement:;

// DDL
ddl_statement:;
create_statement:;
create_table:;
create_database:;
create_index:;
create_view:;
create_procedure:;
create_function:;
create_trigger:;
create_schema:;
alter_statement:;
alter_table:;
alter_database:;
alter_procedure:;
alter_function:;
drop_statement:;
drop_table:;
drop_database:;
drop_index:;
drop_view:;
drop_procedure:;
drop_function:;
drop_trigger:;
truncate_statement:;

// DML
dml_statement:;
select_statement:;
query_expression:;
query_specification:;
insert_statement:;
insert_with_cte:;
insert_source:;
values_clause:;
row_value_list:;
row_value:;
update_statement:;
update_with_cte:;
assignment_list:;
assignment:;
delete_statement:;
delete_with_cte:;
merge_statement:;

// Query Clauses
select_list:;
select_list_element:;
from_clause:;
table_source_list:;
table_source:;
table_source_item:;
subquery:;
join_clause:;
join_type:;
join_condition:;
where_clause:;
group_by_clause:;
group_by_list:;
group_by_item:;
having_clause:;
order_by_clause:;
order_by_list:;
order_by_item:;
top_clause:;
limit_clause:;
offset_clause:;
set_operator:;

// ============================================ CATEGORY 2: CTE, Cursor, Expressions & Control Flow
// (Person 3 & Person 4) ============================================

// CTE
with_clause:;
cte_list:;
common_table_expression:;
cte_name:;

// Cursor
cursor_statement:;
cursor_declare:;
cursor_open:;
cursor_fetch:;
cursor_close:;
cursor_deallocate:;
cursor_name:;
cursor_options:;
fetch_options:;

// Transactions & Control Flow
transaction_statement:;
begin_transaction:;
commit_transaction:;
rollback_transaction:;
save_transaction:;
transaction_name:;
other_statement:;
declare_statement:;
variable_declaration_list:;
variable_declaration:;
set_statement:;
execute_statement:;
print_statement:;
if_statement:;
while_statement:;
statement_block:;

// Expressions & Conditions
search_condition:;
search_condition_or:;
search_condition_and:;
search_condition_not:;
predicate:;
comparison_operator:;
expression:;
arithmetic_operator:;
primary_expression:;
function_call:;
argument_list:;
case_expression:;
when_clause:;
else_clause:;
cast_expression:;

// Basic Elements
table_name:;
column_name:;
table_alias:;
column_alias:;
procedure_name:;
function_name:;
variable_name:;
variable_list:;
parameter_list:;
parameter:;
column_name_list:;
expression_list:;
data_type:;
type_name:;
precision:;
scale:;
literal:;
identifier:;
table_function:;