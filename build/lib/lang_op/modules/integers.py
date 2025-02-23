import re
from lang_op.modules.object_types.alph_object import Alph
from lang_op.modules.object_types.int_object import Int

def check_is_int(value):
    if not isinstance(value, Int):
        return Int(content=value)
    return value


def p_IntegerExpression(p):
    """IntExpression : AddSub"""
    p[0] = check_is_int(p[1])


def p_StringLen(p):
    """StringLen : LenOp StringExpression LenOp
        | LenOp StringExpression On AlphExpression LenOp"""

    if len(p) == 4:
        p[0] = Int(content=len(p[2]))
        return

    alph: Alph = p[4]

    p[0] = Int(content=alph.len_on(p[2].content))


def p_IntAddSub(p):
    """AddSub : AddSub Add MultDiv
                | AddSub Sub MultDiv
                | MultDiv"""
    match (len(p)):
        case 2:
            p[0] = p[1]
        case 4:
            if p.slice[2].type == "Add":
                p[0] = p[1] + p[3]
            if p.slice[2].type == "Sub":
                p[0] = p[1] - p[3]


def p_IntMultDiv(p):
    """MultDiv : MultDiv Concat IntPow
                | MultDiv Div IntPow
                | IntPow"""
    match (len(p)):
        case 2:
            p[0] = p[1]
            return
        case 4:
            if p.slice[2].type == "Concat":
                p[0] = p[1] * p[3]
                return
            if p.slice[2].type == "Div":
                val = p[1] // p[3]
                if val.content < 0:
                    val += 1
                p[0] = val
                return


def p_IntPow(p):
    """IntPow : IntPow Pow Unary
                | Unary"""
    match len(p):
        case 2:
            p[0] = p[1]
        case 4:
            p[0] = p[1] ** p[3]


def p_IntUnary(p):
    """Unary : Sub Primary
            | Primary"""
    if len(p) > 2:
        p[0] = Int(content=-p[2])
    else:
        p[0] = p[1]


def p_IntPrimary(p):
    """Primary : LGroup IntExpression RGroup
                | StringLen
                | VInt
                | Int"""
    match (len(p)):

        case 4:
            if not (p[2].__class__ is Int):
                p[0] = Int(content=int(p[2]))
                return
            p[0] = p[2]

        case 2:
            if not (p[1].__class__ is Int):
                p[0] = Int(content=int(p[1]))
            p[0] = p[1]

