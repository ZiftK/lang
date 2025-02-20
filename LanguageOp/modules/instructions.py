from lang.LanguageOp.modules.object_types.lang_object import Lang
from lang.LanguageOp.modules.variables import vars
from lang.LanguageOp.modules.object_types.alph_object import Alph
from lang.LanguageOp.modules.object_types.string_object import String
from lang.LanguageOp.modules.object_types.int_object import Int
from lang.LanguageOp.modules.object_types.object import Object
from lang.LanguageOp.modules.object_types.boolean_object import Boolean

types_eq = {
    "SuperString": "String",
    "SuperAlph": "Alph",
    "Integer": "Integer"
}


def declare_var(obj: Object):

    vars[obj.name] = {"value": obj, "type": "V" + obj.__class__.__name__}


def assign_var(left_object: Object, right_object: Object):

    if not (left_object.name in vars):
        raise Exception(f"Unknown variable {left_object.name}")

    variable: dict = vars.get(left_object.name)

    if not ("V" + right_object.__class__.__name__ == variable.get("type")):
        raise Exception(f"A {type} was passed, but a {variable.get('type')} was expected")

    left_object.copy(right_object)


def p_ShowVal(p):
    r"""ShowVal : Show expression"""

    print(p[2])
    p[0] = p[1]


def p_Declares(p):
    """Declares : StringDeclare
        | IntDeclare
        | AlphDeclare
        | LangDeclare
        | BooleanDeclare"""
    p[0] = p[1]


def p_Assigns(p):
    """Assigns : StringAssign
        | IntAssign
        | AlphAssign
        | LangAssign
        | BooleanAssign"""
    p[0] = p[1]


def p_StringDeclare(p):
    """StringDeclare : StringType VarName
                | StringType VarName Eq StringExpression
                | StringDeclare Splitter VarName
                | StringDeclare Splitter VarName Eq StringExpression"""

    if len(p) <= 4:
        unassigned: String = String(name=p[2])
        declare_var(unassigned)

    if len(p) == 5:
        string: String = p[4]
        string.name = p[2]
        declare_var(string)

    if len(p) == 6:
        string: String = p[5]
        string.name = p[3]
        declare_var(string)

    p[0] = p[2]


def p_StringAssign(p):
    """StringAssign : VString Eq StringExpression"""

    assign_var(left_object=p[1], right_object=p[3])

    p[0] = p[3]


def p_IntDeclare(p):
    """IntDeclare : IntType VarName
        | IntType VarName Eq IntExpression
        | IntDeclare Splitter VarName
        | IntDeclare Splitter VarName Eq IntExpression"""
    if len(p) <= 4:
        unassigned: Int = Int(name=p[2])
        declare_var(unassigned)

    if len(p) == 5:
        integer: Int = p[4]
        integer.name = p[2]
        declare_var(integer)

    if len(p) == 6:
        integer: Int = p[5]
        integer.name = p[3]
        declare_var(integer)

    p[0] = p[2]


def p_IntAssign(p):
    """IntAssign : VarName Eq IntExpression"""

    assign_var(left_object=p[1], right_object=p[3])

    p[0] = p[3]


def p_AlphDeclare(p):
    """AlphDeclare : AlphType VarName
        | AlphType VarName Eq AlphExpression
        | AlphDeclare Splitter VarName
        | AlphDeclare Splitter VarName Eq AlphExpression"""
    if len(p) <= 4:
        unassigned: Alph = Alph(name=p[2])
        declare_var(unassigned)

    if len(p) == 5:
        alph: Alph = p[4]
        alph.name = p[2]
        declare_var(alph)

    if len(p) == 6:
        alph: Alph = p[4]
        alph.name = p[3]
        declare_var(alph)

    p[0] = p[2]


def p_AlphAssign(p):
    """AlphAssign : VarName Eq AlphExpression"""

    assign_var(left_object=p[1], right_object=p[2])

    p[0] = p[3]


def p_LangDeclare(p):
    """LangDeclare : LangType VarName
        | LangType VarName Eq LangExpression
        | LangDeclare Splitter VarName
        | LangDeclare Splitter VarName Eq LangExpression"""
    if len(p) <= 4:
        unassigned: Lang = Lang(name=p[2])
        declare_var(unassigned)

    if len(p) == 5:
        lang: Lang = p[4]
        lang.name = p[2]
        declare_var(lang)

    if len(p) == 6:
        lang: Lang = p[5]
        lang.name = p[3]
        declare_var(lang)

    p[0] = p[2]


def p_LangAssign(p):
    """LangAssign : VLang Eq LangExpression"""


    assign_var(left_object=p[1], right_object=p[3])

    p[0] = p[3]


def p_BooleanDeclare(p):
    """BooleanDeclare : BooleanType VarName
                | BooleanType VarName Eq BooleanExpression
                | BooleanDeclare Splitter VarName
                | BooleanDeclare Splitter VarName Eq BooleanExpression"""

    if len(p) <= 4:
        unassigned: Boolean = Boolean(name=p[2])
        declare_var(unassigned)

    if len(p) == 5:
        boolean: Boolean = p[4]
        boolean.name = p[2]
        declare_var(boolean)

    if len(p) == 6:
        boolean: Boolean = p[5]
        boolean.name = p[3]
        declare_var(boolean)

    p[0] = p[2]


def p_BooleanAssign(p):
    """BooleanAssign : VarName Eq BooleanExpression"""

    assign_var(left_object=p[1], right_object=p[3])

    p[0] = p[3]
