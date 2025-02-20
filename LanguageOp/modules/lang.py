from modules.object_types.lang_object import Lang
from modules.object_types.alph_object import Alph


def p_LangExpression(p):
    """LangExpression : StringPrefix
    | StringSuffix
    | AlphKleeneC
    | VLang"""
    p[0] = p[1]


def p_AlphKleeneC(p):
    """AlphKleeneC : AlphExpression KleeneC IntExpression"""
    alph: Alph = p[1]
    p[0] = alph.calc_kleene_clau(p[3])


def p_StringPrefix(p):
    """StringPrefix : Prefix StringExpression"""

    str_val = p[2]

    p[0] = [str_val[0:n] for n in range(len(str_val) + 1)]


def p_StringSuffix(p):
    """StringSuffix : Suffix StringExpression"""
    str_val = p[2]

    p[0] = [str_val[:-n] for n in range(1, len(str_val) + 1)]
    p[0] = [str_val] + p[0]
