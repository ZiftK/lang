from modules.object_types.lang_object import Lang
from modules.object_types.alph_object import Alph
from modules.object_types.string_object import String


def check_is_lang(value):
    if not (value.__class__ is Lang):
        return Lang(content=value)
    return value


def p_LangExpression(p):
    """LangExpression : StringPrefix
    | StringSuffix
    | AlphKleeneC
    | AlphPositiveC
    | LangKleeneC
    | LangPositiveC
    | LangUnion
    | StringSubSequence
    | StringSubString"""
    p[0] = check_is_lang(p[1])


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

    str_val: String = p[2]

    p[0] = str_val.calc_prefix()


def p_StringSuffix(p):
    """StringSuffix : Suffix StringExpression"""
    str_val: String = p[2]

    p[0] = str_val.calc_suffix()


def p_StringSubSequence(p):
    """StringSubSequence : SubSequence StringExpression"""
    string: String = p[2]
    p[0] = string.calc_sub_sequences()


def p_StringSubString(p):
    """StringSubString : SubString StringExpression"""
    string: String = p[2]
    p[0] = string.calc_sub_strings()
