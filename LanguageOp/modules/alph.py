from modules.object_types.alph_object import Alph


def p_AlphExpression(p):
    """AlphExpression : AlphConcat"""
    if not p[1].__class__ is set:
        p[0] = p[1]
        return

    p[0] = Alph(p[1])


def p_AlphConcat(p):
    """AlphConcat : AlphConcat Concat AlphPow
        | AlphPow"""

    match len(p):
        case 2:
            p[0] = p[1]
        case 4:
            lalph: Alph = p[1]
            ralph: Alph = p[3]
            p[0] = lalph.concat(ralph)


def p_AlphPow(p):
    """AlphPow : AlphPow Pow IntExpression
            | AlphGroup"""
    match len(p):
        case 2:
            p[0] = p[1]
        case 4:
            lalph: Alph = p[1]
            p[0] = lalph.pow(p[3])


def p_AlphGroup(p):
    """AlphGroup : LGroup AlphExpression RGroup
    | Alph
    | VAlph"""
    match len(p):
        case 4:
            p[0] = p[2]
        case 2:
            p[0] = p[1]


def p_Alph(p):
    r"""Alph : OpenStruct StringList CloseStruct
            | OpenStruct StringExpression CloseStruct"""

    if p[2].__class__ is str:
        p[0] = {p[2]}
    else:
        real_content = [x.content for x in p[2]]
        p[0] = set(real_content)


def p_StringList(p):
    """StringList : StringList Splitter StringExpression
                    | StringExpression Splitter StringExpression"""

    if p[1].__class__ is list:
        lst: list = p[1]
        lst.append(p[3])
        p[0] = lst

    else:
        p[0] = [p[1], p[3]]