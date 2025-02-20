import re
from modules.object_types.alph_object import Alph
from modules.object_types.int_object import Int


def p_IntegerExpression(p):
    """IntExpression : Int
        | StringLen
        | VInt"""
    if not (p[1].__class__ is Int):
        p[0] = Int(p[1])

    p[0] = p[1]


def p_StringLen(p):
    """StringLen : LenOp StringExpression LenOp
        | LenOp StringExpression On AlphExpression LenOp"""

    if len(p) == 4:
        p[0] = len(p[2])
        return

    alph: Alph = p[4]

    p[0] = alph.len_on(p[2])
