import re


def p_IntegerExpression(p):
    """IntExpression : StringLen
        | AddSub"""
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
                | VarValue
                | Int"""
    match (len(p)):
        case 4:
            p[0] = p[2]
        case 2:
            p[0] = p[1]
