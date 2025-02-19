import re


def p_IntegerExpression(p):
    """IntExpression : Int
        | StringLen
        | VarValue"""
    p[0] = p[1]


def p_StringLen(p):
    """StringLen : LenOp StringExpression LenOp
        | LenOp StringExpression On AlphExpression LenOp"""

    if len(p) == 4:
        p[0] = len(p[2])
        return

    pattern = "(" + ")|(".join(p[4]) + ")"
    pattern = re.compile(pattern)
    matches = re.findall(pattern, p[2])

    p[0] = len(matches)


def p_StringPrefix(p):
    """StringPrefix : Prefix StringExpression"""

    str_val = p[2]

    p[0] = set(str_val[0:n] for n in range(len(str_val) + 1))
