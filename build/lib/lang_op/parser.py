from ply import yacc
import logging
from lang_op.lexer import tokens
from lang_op.modules.integers import *
from lang_op.modules.alph import *
from lang_op.modules.instructions import *
from lang_op.modules.variables import *
from lang_op.modules.lang import *
from lang_op.modules.strings import *
from lang_op.modules.boolean import *

precedence = (
    ("left", "Add", "Sub"),
    ("left", "Concat", "Div"),
    ("right", "Pow")
)


def p_expressions(p):
    r"""expressions : expressions expression Term
                    | expression Term"""

    p[0] = p[1]


def p_expression(p):
    r"""expression : IntExpression
                    | AlphExpression
                    | StringExpression
                    | LangExpression
                    | BooleanExpression
                    | ShowVal
                    | Assigns
                    | Declares"""
    p[0] = p[1]


def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (Línea {p.lineno})")
        print(f"Token tipo [{p.type}] inesperado")
    else:
        print("Error de sintaxis al final del archivo")

logger = logging.getLogger("plylogger")
logger.disabled = True

parser = yacc.yacc(start="expressions", errorlog=logger)

if __name__ == "__main__":
    with open("./test.lang", "r") as file:
        content = file.read()

    result = parser.parse(content, debug=False)

    # print(result)
    # print(f"{vars=}")
