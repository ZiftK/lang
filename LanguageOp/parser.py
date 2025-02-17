from ply import yacc
from lexer import tokens
import re

vars = {}

precedence = (
    ("left", "Concat"),
    ("right", "Pow"),
)


def p_expressions(p):
    r"""expressions : expressions expression Term
                    | expression Term"""
    p[0] = p[1]


def p_expression(p):
    r"""expression : VarAssign
                    | ShowVal"""
    p[0] = p[1]


def p_ShowVal(p):
    r"""ShowVal : Show Integer
                | Show StringConcat
                | Show Alph
                | Show VarName"""
    if p.slice[2].type == "VarName":
        print(vars.get(p[2])[0])
    else:
        print(p[2])
    p[0] = p[2]


def p_VarAssign(p):
    r"""VarAssign :  StringType VarName Eq StringConcat
                    | AlphType VarName Eq Alph
                    | IntType VarName Eq Integer"""

    vars[p[2]] = (p[4], p.slice[4].type)
    p[0] = p[4]


def p_Alph(p):
    r"""Alph : OpenStruct StringList CloseStruct
            | OpenStruct String CloseStruct"""
    if p[2].__class__ is str:
        p[0] = {p[2]}
    else:
        p[0] = set(p[2])


def p_StringList(p):
    r"""StringList : StringList Splitter StringConcat
                    | StringConcat Splitter StringConcat"""

    if p[1].__class__ is list:
        lst: list = p[1]
        lst.append(p[3])
        p[0] = lst

    else:
        p[0] = [p[1], p[3]]


def p_StringConcat(p):
    r"""StringConcat : StringConcat Concat StringPow
                    | StringPow"""
    if len(p) > 2:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]


def p_StringPow(p):
    r"""StringPow : StringPow Pow Integer
                | StringPow Pow VarName
                | String"""

    if len(p) > 2:

        if p.slice[3].type == "Integer":
            p[0] = p[1] * p[3]
            return

        value, value_type = vars.get(p[3])
        if not value_type == "Integer":
            raise Exception("The pow value must be an integer")

        p[0] = p[1]*value
    else:
        p[0] = p[1]


def p_Integer(p):
    r"""Integer : Int
                | StringLen"""

    if len(p) > 2:
        p[0] = len(p[2])

    else:
        p[0] = p[1]


def p_StringLen(p):
    r"""StringLen : LenOp String LenOp
                | LenOp String On Alph LenOp
                | LenOp String On VarName LenOp"""

    if len(p) == 4:
        p[0] = len(p[2])
        return

    if p.slice[4].type == "VarName":

        if not p[4] in vars:
            raise Exception("Unknown variable")

        value, value_type = vars.get(p[4])
        value: set

        if not value_type == "Alph":
            raise Exception(f"Wrong type")

        pattern = ")|(".join(value)
        pattern = "(" + pattern + ")"
        pattern = re.compile(pattern)
        matches = re.findall(pattern, p[2])
        p[0] = len(matches)


def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (Línea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")


if __name__ == "__main__":
    parser = yacc.yacc()

    with open("./test.lang", "r") as file:
        content = file.read()

    result = parser.parse(content)

    # print(f"\n\n{result=}")
    print(f"{vars=}")
