def p_AlphExpression(p):
    """AlphExpression : Alph
    | VarValue"""
    p[0] = p[1]


def p_Alph(p):
    r"""Alph : OpenStruct StringList CloseStruct
            | OpenStruct StringExpression CloseStruct"""
    if p.slice[2] == "SuperString":
        p[0] = {p[2]}
    else:
        p[0] = set(p[2])


def p_StringList(p):
    """StringList : StringList Splitter StringExpression
                    | StringExpression Splitter StringExpression"""

    if p[1].__class__ is list:
        lst: list = p[1]
        lst.append(p[3])
        p[0] = lst

    else:
        p[0] = [p[1], p[3]]

