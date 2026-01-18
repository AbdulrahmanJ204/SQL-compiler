
parser grammar TransactParser;
options {
    tokenVocab = SQLLexer;
}
import BasicParser;




transaction_statement
    : begin_transaction
    | begin_ditributed_transaction
    | commit_transaction
    | commit_work
    | rollback_transaction
    ;
//BEGIN DISTRIBUTED { TRAN | TRANSACTION }
//     [ transaction_name | @tran_name_variable ]
//[ ; ]
begin_ditributed_transaction:BEGIN DISTRIBUTED? (TRAN | TRANSACTION) transaction_name? SEMI?;
//BEGIN { TRAN | TRANSACTION }
//    [ { transaction_name | @tran_name_variable }
//      [ WITH MARK [ 'description' ] ]
//    ]
//[ ; ]
begin_transaction
    : BEGIN (TRAN | TRANSACTION)
      (transaction_name?
      with_mark_clause?)? SEMI?
    ;

with_mark_clause
    : WITH MARK STRING_LITERAL?
    ;

//COMMIT [ { TRAN | TRANSACTION }
//    [ transaction_name | @tran_name_variable ] ]
//    [ WITH ( DELAYED_DURABILITY = { OFF | ON } ) ]
//[ ; ]
commit_transaction
    : COMMIT ((TRAN | TRANSACTION) transaction_name? with_delay_durability_clause?)? SEMI?
    ;
with_delay_durability_clause
    : LPAREN WITH DELAYED_DURABILITY EQ (OFF | ON) RPAREN;


//COMMIT [ WORK ]
  //[ ; ]
commit_work: COMMIT  WORK? SEMI?;


//SAVE { TRAN | TRANSACTION } { savepoint_name | @savepoint_variable }
//[ ; ]
save_transaction
    : SAVE (TRAN | TRANSACTION) transaction_name SEMI?
    ;

//ROLLBACK { TRAN | TRANSACTION }
//    [ transaction_name | @tran_name_variable
//    | savepoint_name | @savepoint_variable ]
//[ ; ]
rollback_transaction
    : ROLLBACK (TRAN | TRANSACTION) transaction_name? SEMI?
    ;

//ROLLBACK [ WORK ]
  //[ ; ]
rollback_work: ROLLBACK WORK? SEMI?;

transaction_name
    : IDENTIFIER | USER_VARIABLE
    ;
