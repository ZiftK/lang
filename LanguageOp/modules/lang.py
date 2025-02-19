
def p_LangExpression(p):
    """LangExpression : StringPrefix"""
    p[0] = p[1]


def p_StringPrefix(p):
    """StringPrefix : Prefix StringExpression"""

    str_val = p[2]

    p[0] = set(str_val[0:n] for n in range(len(str_val) + 1))
