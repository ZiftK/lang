from modules.variables import vars

types_eq = {
    "SuperString": "String",
    "SuperAlph": "Alph",
    "Integer": "Integer"
}


def declare_var(*, name: str, type: str, value=None):
    vars[name] = {"value": value, "type": type}


def assign_var(*, name: str, value, type: str):
    if not (name in vars):
        raise Exception(f"Unknown variable {name}")

    variable: dict = vars.get(name)

    if not (type == variable.get("type")):
        raise Exception(f"A {type} was passed, but a {variable.get('type')} was expected")

    variable["value"] = value


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
        declare_var(name=p[len(p) - 1], type="VString")

    if len(p) == 5:
        declare_var(name=p[2], type="VString", value=p[4])

    if len(p) == 6:
        declare_var(name=p[3], type="VString", value=p[5])

    p[0] = p[2]


def p_StringAssign(p):
    """StringAssign : VarName Eq StringExpression"""

    assign_var(name=p[1], value=p[3], type="VString")

    p[0] = p[3]


def p_IntDeclare(p):
    """IntDeclare : IntType VarName
        | IntType VarName Eq IntExpression
        | IntDeclare Splitter VarName
        | IntDeclare Splitter VarName Eq IntExpression"""
    if len(p) <= 4:
        declare_var(name=p[len(p) - 1], type="VInt")

    if len(p) == 5:
        declare_var(name=p[2], type="VInt", value=p[4])

    if len(p) == 6:
        declare_var(name=p[3], type="VInt", value=p[5])

    p[0] = p[2]


def p_IntAssign(p):
    """IntAssign : VarName Eq IntExpression"""

    assign_var(name=p[1], value=p[3], type="VInt")

    p[0] = p[3]


def p_AlphDeclare(p):
    """AlphDeclare : AlphType VarName
        | AlphType VarName Eq AlphExpression
        | AlphDeclare Splitter VarName
        | AlphDeclare Splitter VarName Eq AlphExpression"""
    if len(p) <= 4:
        declare_var(name=p[len(p) - 1], type="VAlph")

    if len(p) == 5:
        declare_var(name=p[2], type="VAlph", value=p[4])

    if len(p) == 6:
        declare_var(name=p[3], type="VAlph", value=p[5])

    p[0] = p[2]


def p_AlphAssign(p):
    """AlphAssign : VarName Eq AlphExpression"""

    assign_var(name=p[1], value=p[3], type="VAlph")

    p[0] = p[3]


def p_LangDeclare(p):
    """LangDeclare : LangType VarName
        | LangType VarName Eq LangExpression
        | LangDeclare Splitter VarName
        | LangDeclare Splitter VarName Eq LangExpression"""
    if len(p) <= 4:
        declare_var(name=p[len(p) - 1], type="VLang")

    if len(p) == 5:
        declare_var(name=p[2], type="VLang", value=p[4])

    if len(p) == 6:
        declare_var(name=p[3], type="VLang", value=p[5])

    p[0] = p[2]


def p_LangAssign(p):
    """LangAssign : VarName Eq LangExpression"""

    assign_var(name=p[1], value=p[3], type="VLang")

    p[0] = p[3]


def p_BooleanDeclare(p):
    """BooleanDeclare : BooleanType VarName
                | BooleanType VarName Eq BooleanExpression
                | BooleanDeclare Splitter VarName
                | BooleanDeclare Splitter VarName Eq BooleanExpression"""

    if len(p) <= 4:
        declare_var(name=p[len(p) - 1], type="VBoolean")

    if len(p) == 5:
        declare_var(name=p[2], type="VBoolean", value=p[4])

    if len(p) == 6:
        declare_var(name=p[3], type="VBoolean", value=p[5])

    p[0] = p[2]


def p_BooleanAssign(p):
    """BooleanAssign : VarName Eq BooleanExpression"""

    assign_var(name=p[1], value=p[3], type="VBoolean")

    p[0] = p[3]
