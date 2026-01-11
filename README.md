# SQL-Compiler
  use this command to generated the lexer 
  ```shell
  antlr4 src/SQLLexer.g4 -Dlanguage=Python3 -o .\generated\

  python -m src.main inputFile

  python -m src.main .\queries\test1.sql  
  ```



  # Mini T-SQL Parser – Common Grammar Rules Guide

This document lists the most common repeated grammar rules used across
DDL, DML, CTE, and Cursor statements in T-SQL, ordered by **implementation
priority** and **mapped to statement categories**.

---

## 1. Implementation Priority (Top → Bottom)

### Tier 1 – Absolute Core (Implement First)
These rules are required almost everywhere and block progress if missing.

- identifier
- multipart_identifier
- expression
- scalar_expression
- search_condition
- predicate
- boolean_expression
- comparison_expression
- logical_operator
- constant
- parameter

---

### Tier 2 – Query Skeleton (SELECT Backbone)
Needed for SELECT, CTEs, subqueries, and many DML statements.

- select_statement
- query_expression
- query_specification
- from_clause
- where_clause
- join_clause
- join_type
- join_condition
- on_clause
- subquery
- derived_table
- alias
- table_alias
- column_alias

---

### Tier 3 – Query Refinement
Used for grouping, sorting, pagination, and filtering.

- group_by_clause
- having_clause
- order_by_clause
- offset_fetch_clause
- top_clause
- apply_clause
- cross_join

---

### Tier 4 – Expressions & Functions
Shared across SELECT, WHERE, DML assignments, and constraints.

- arithmetic_expression
- case_expression
- function_call
- aggregate_function
- window_function
- between_expression
- in_expression
- like_expression
- exists_expression
- null_predicate
- unary_expression

---

### Tier 5 – DML Core
Core rules for INSERT, UPDATE, DELETE.

- insert_statement
- update_statement
- delete_statement
- set_clause
- assignment
- output_clause

---

### Tier 6 – CTE Support
Used in modern queries and recursive logic.

- with_expression
- common_table_expression
- cte_column_list
- recursive_cte
- anchor_query
- recursive_query

---

### Tier 7 – DDL Foundation
Needed once SELECT & expressions are stable.

- data_type
- column_definition
- column_constraint
- table_constraint
- constraint_definition
- index_definition
- default_definition

---

### Tier 8 – Cursor Support
Less common, but structurally complex.

- cursor_name
- cursor_declaration
- cursor_option
- fetch_statement
- fetch_target
- cursor_status

---

### Tier 9 – Control Flow & Transactions
Usually optional for a “mini” parser.

- begin_end_block
- if_statement
- while_statement
- break_statement
- continue_statement
- transaction_statement

---

### Tier 10 – Hints & Optimization
Low priority, high syntax noise.

- hint_clause
- option_clause
- query_hint
- table_hint
- lock_hint

---

## 2. Rule Usage Mapping (DDL / DML / CTE / Cursor)

Legend:
- ✅ = Commonly Used
- ⚠️ = Sometimes Used
- ❌ = Rare / Not Used

| Rule / Category            | DDL | DML | CTE | Cursor |
|----------------------------|-----|-----|-----|--------|
| identifier                 | ✅ | ✅ | ✅ | ✅ |
| multipart_identifier       | ✅ | ✅ | ✅ | ✅ |
| expression                 | ⚠️ | ✅ | ✅ | ⚠️ |
| search_condition           | ❌ | ✅ | ✅ | ⚠️ |
| select_statement           | ❌ | ✅ | ✅ | ⚠️ |
| from_clause                | ❌ | ✅ | ✅ | ❌ |
| where_clause               | ❌ | ✅ | ✅ | ⚠️ |
| join_clause                | ❌ | ✅ | ✅ | ❌ |
| subquery                   | ❌ | ✅ | ✅ | ❌ |
| derived_table              | ❌ | ✅ | ✅ | ❌ |
| with_expression            | ❌ | ❌ | ✅ | ❌ |
| common_table_expression    | ❌ | ❌ | ✅ | ❌ |
| insert_statement           | ❌ | ✅ | ❌ | ❌ |
| update_statement           | ❌ | ✅ | ❌ | ❌ |
| delete_statement           | ❌ | ✅ | ❌ | ❌ |
| data_type                  | ✅ | ❌ | ❌ | ❌ |
| column_definition          | ✅ | ❌ | ❌ | ❌ |
| table_constraint           | ✅ | ❌ | ❌ | ❌ |
| index_definition           | ✅ | ❌ | ❌ | ❌ |
| cursor_declaration         | ❌ | ❌ | ❌ | ✅ |
| fetch_statement            | ❌ | ❌ | ❌ | ✅ |
| cursor_option              | ❌ | ❌ | ❌ | ✅ |
| begin_end_block            | ⚠️ | ⚠️ | ⚠️ | ✅ |
| if_statement               | ⚠️ | ⚠️ | ❌ | ⚠️ |
| transaction_statement      | ⚠️ | ⚠️ | ❌ | ⚠️ |
| hint_clause                | ⚠️ | ⚠️ | ⚠️ | ❌ |

---

## Suggested Build Order (Practical)

1. Identifiers + Expressions
2. Search conditions + predicates
3. SELECT + FROM + JOIN + WHERE
4. Subqueries + derived tables
5. DML (INSERT / UPDATE / DELETE)
6. CTEs
7. DDL
8. Cursor statements
9. Control flow & hints

---

End of document.
