import re

from modules.variables import vars


def p_StringExpression(p):
    """StringExpression : StringConcat"""
    if not (p[1].__class__ is String):
        p[0] = String(content=p[1])
        return
    p[0] = p[1]


def p_StringConcat(p):
    """StringConcat : StringConcat Concat StringPow
                    | StringPow"""
    if len(p) > 2:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]


def p_StringPow(p):
    """StringPow : StringPow Pow IntExpression
                | StringGroup """

    if len(p) > 2:
        p[0] = p[1] * p[3]
        return
    p[0] = p[1]


def p_StringGroup(p):
    """StringGroup : LGroup StringExpression RGroup
                    | String
                    | VString"""

    if len(p) > 2:
        p[0] = p[2]
        return
    p[0] = p[1]
