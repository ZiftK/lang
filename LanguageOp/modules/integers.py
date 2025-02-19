from modules.variables import vars


def p_IntegerExpression(p):
    """IntExpression : Int
        | StringLen
        | VarValue"""
    p[0] = p[1]


def p_StringLen(p):
    """StringLen : LenOp StringExpression LenOp"""
    p[0] = len(p[2])


def p_StringPrefix(p):
    """StringPrefix : Prefix StringExpression"""

    str_val = p[2]

    p[0] = set(str_val[0:n] for n in range(len(str_val) + 1))
