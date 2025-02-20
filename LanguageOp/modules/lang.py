from lang.LanguageOp.modules.object_types.lang_object import Lang
from lang.LanguageOp.modules.object_types.alph_object import Alph


def p_LangExpression(p):
    """LangExpression : StringPrefix
    | StringSuffix
    | AlphKleeneC
    | AlphPositiveC
    | LangKleeneC
    | LangPositiveC
    | LangUnion"""
    p[0] = p[1]


def p_LangUnion(p):
    """LangUnion : LangUnion Add LangConcat
                | LangConcat"""
    match len(p):
        case 2:
            p[0] = p[1]
        case 4:
            left_lang: Lang = p[1]
            right_lang: Lang = p[3]
            p[0] = left_lang.union(right_lang)


def p_LangConcat(p):
    """LangConcat : LangConcat Concat LangGroup
                | LangGroup"""
    match len(p):
        case 2:
            p[0] = p[1]
        case 4:
            left_lang: Lang = p[1]
            right_lang: Lang = p[3]
            p[0] = left_lang.concat(right_lang)


def p_LangGroup(p):
    """LangGroup : LGroup LangExpression RGroup
    | VLang"""
    match len(p):
        case 2:
            p[0] = p[1]
        case 4:
            p[0] = p[2]


def p_AlphKleeneC(p):
    """AlphKleeneC : AlphExpression KleeneC IntExpression"""
    alph: Alph = p[1]
    p[0] = alph.get_kleene_clau(p[3])


def p_AlphPositiveC(p):
    """AlphPositiveC : AlphExpression PositiveC IntExpression"""
    alph: Alph = p[1]
    p[0] = alph.get_positive_clau(p[3])


def p_LangKleeneC(p):
    """LangKleeneC : LangExpression KleeneC IntExpression"""
    lang: Lang = p[1]
    p[0] = lang.get_kleene_clau(p[3])


def p_LangPositiveC(p):
    """LangPositiveC : LangExpression PositiveC IntExpression"""
    lang: Lang = p[1]
    p[0] = lang.get_positive_clau(p[3])


def p_StringPrefix(p):
    """StringPrefix : Prefix StringExpression"""

    str_val = p[2]

    p[0] = [str_val[0:n] for n in range(len(str_val) + 1)]


def p_StringSuffix(p):
    """StringSuffix : Suffix StringExpression"""
    str_val = p[2]

    p[0] = [str_val[:-n] for n in range(1, len(str_val) + 1)]
    p[0] = [str_val] + p[0]
