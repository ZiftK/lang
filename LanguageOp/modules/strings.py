import re

from modules.variables import vars


def p_StringExpression(p):
    """StringExpression : StringConcat"""
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
        p[0] = p[1]*p[3]
        return
    p[0] = p[1]


def p_StringGroup(p):
    """StringGroup : LGroup StringExpression RGroup
                    | String
                    | VarValue"""

    if len(p) > 2:
        p[0] = p[2]
        return
    p[0] = p[1]

