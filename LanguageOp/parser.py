from ply import yacc
from lexer import tokens
from modules.strings import *
from modules.integers import *
from modules.alph import *
from modules.instructions import *
from modules.variables import *


precedence = (
    ("left", "Concat"),
    ("right", "Pow"),
)


def p_expressions(p):
    r"""expressions : expressions expression Term
                    | expression Term"""
    p[0] = p[1]


def p_expression(p):
    r"""expression : StringExpression
                    | IntExpression
                    | AlphExpression
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


if __name__ == "__main__":

    parser = yacc.yacc(start="expressions")

    with open("./test.lang", "r") as file:
        content = file.read()

    result = parser.parse(content, debug=False)

    # print(result)
    # print(f"{vars=}")

