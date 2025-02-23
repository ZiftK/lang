from ply import yacc
import logging
from lexer import tokens
from modules.integers import *
from modules.alph import *
from modules.instructions import *
from modules.variables import *
from modules.lang import *
from modules.strings import *
from modules.boolean import *

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
