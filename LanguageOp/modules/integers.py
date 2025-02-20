import re
from modules.object_types.alph_object import Alph
from modules.object_types.int_object import Int


def p_IntegerExpression(p):
    """IntExpression : StringLen
        | AddSub"""
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

def p_IntAddSub(p):
    """AddSub : MultDiv Add AddSub
                | MultDiv Sub AddSub
                | MultDiv"""
    match (len(p)):
        case 2:
            p[0] = p[1]
        case 4 :
            if p.slice[2].type == "Add":
                p[0] = p[1] + p[3]
        case 4:
            if p.slice[2].type == "Sub":
                p[0] = p[1] - p[3]


def p_IntMultDiv(p):
    """MultDiv : MultDiv Concat Unary
                | MultDiv Div Unary
                | Unary"""
    match (len(p)):
        case 2:
            p[0] = p[1]
            return
        case 4:
            if p.slice[2].type == "Concat":
                p[0] = p[1] * p[3]
                return
        case 4 if p.slice[2].type == "Div":
            p[0] = p[1] // p[3]
            return


def p_IntUnary(p):
    """Unary : Sub Primary
               | Primary"""
    if len(p) > 2:
        p[0] = - p[2]
    else:
        p[0] = p[1]


def p_IntPrimary(p):
    """Primary : LGroup IntExpression RGroup
                | VInt
                | Int"""
    match (len(p)):
        case 4:
            p[0] = p[2]
        case 2:
            p[0] = p[1]