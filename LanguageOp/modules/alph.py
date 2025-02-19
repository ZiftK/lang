def p_SuperAlph(p):
    """SuperAlph : Alph
                | StringPrefix"""
    p[0] = p[1]


def p_Alph(p):
    r"""Alph : OpenStruct StringList CloseStruct
            | OpenStruct SuperString CloseStruct"""
    if p.slice[2] == "SuperString":
        p[0] = {p[2]}
    else:
        p[0] = set(p[2])
