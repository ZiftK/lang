import re

from modules.variables import vars


def p_StringExpression(p):
    """StringExpression : StringConcat"""
    p[0] = p[1]


def p_StringList(p):
    """StringList : StringList Splitter StringConcat
                    | StringConcat Splitter StringConcat"""

    if p[1].__class__ is list:
        lst: list = p[1]
        lst.append(p[3])
        p[0] = lst

    else:
        p[0] = [p[1], p[3]]


def p_StringPrefix(p):
    """StringPrefix : Prefix SuperString"""

    str_val = p[2]

    p[0] = set(str_val[0:n] for n in range(len(str_val)+1))


def p_StringConcat(p):
    """StringConcat : StringConcat Concat StringPow
                    | StringPow"""
    if len(p) > 2:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]


def p_StringPow(p):
    """StringPow : StringPow Pow Integer
                | String"""

    vars: dict

    if len(p) > 2:

        if p.slice[3].type == "Integer":
            p[0] = p[1] * p[3]
            return

        value, value_type = vars.get(p[3])
        if not value_type == "Integer":
            raise Exception("The pow value must be an integer")

        p[0] = p[1] * value
    else:
        p[0] = p[1]


def p_StringLen(p):
    """StringLen : LenOp SuperString LenOp
                | LenOp SuperString On Alph LenOp
                | LenOp SuperString On VarName LenOp"""

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
