from antlr4.error.ErrorListener import ErrorListener

class SQLErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        msg,
        e
    ):
        error_type = "Lexer" if recognizer.__class__.__name__.endswith("Lexer") else "Parser"

        self.errors.append({
            "type": error_type,
            "line": line,
            "column": column,
            "message": msg,
            "symbol": offendingSymbol
        })
