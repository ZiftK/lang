import copy
import re

from ply import lex

from modules.variables import vars

"""
Language contexts

code
comments
"""

states = (
    ("comment", "exclusive"),
)

# object types
types = {
    "String": "StringType",
    "Lang": "LangType",
    "Alph": "AlphType",
    "Int": "IntType",
    "Boolean": "BooleanType"
}

instructions = {
    "on": "On",
    "show": "Show",
    "showil": "ShowInLine",
    "prefixof": "Prefix",
    "suffixof": "Suffix",
    "true": "True",
    "false": "False",
    "or": "Or",
    "and": "And"
}

var_types = {"T" + x: "V" + v.replace("Type", "") for x, v in types.items()}

reserved_words = {
    **types,
    **instructions,
    **var_types
}

tokens = [
             "Eq",
             "String",
             "Int",
             "OpenStruct",
             "CloseStruct",
             "Splitter",
             "Concat",
             "Pow",
             "LenOp",
             "VarName",
             "Term",
             "NextLine",
             "LGroup",
             "RGroup",
             "SuchThat",
             "KleeneC",
             "PositiveC",
             "Add",
             "Sub",
             "Div",
             "InitComment",
             "EndComment",
             "CommentText"

         ] + list(reserved_words.values())

t_ANY_ignore = r"[ ]"
t_Eq = r"="
t_OpenStruct = r"{"
t_CloseStruct = r"}"
t_Splitter = r","
t_Concat = r"\*"
t_Pow = r"\^"
t_LenOp = r"\|"
t_Term = r";"
t_LGroup = r"\("
t_RGroup = r"\)"
t_SuchThat = r":"
t_KleeneC = r"(\*\*)"
t_PositiveC = r"(\*\+)"
t_Sub = r"-"
t_Div = r"/"


def t_InitComment(t):
    r"""//\("""
    t.lexer.begin("comment")


def t_comment_EndComment(t):
    r"""\)"""
    t.lexer.begin("INITIAL")


def t_comment_CommentText(t):
    r"""[^)]"""


def t_Add(t):
    r"""\+"""
    return t


def t_VarName(t):
    r"""[_A-Za-z][_A-Za-z0-9]*"""
    val: str = t.value

    if val in vars:
        t.value = vars.get(val).get("value")
        t.type = vars.get(val).get("type")

    if val in reserved_words:
        t.type = reserved_words.get(val)

    return t


def t_String(t):
    r"""\"[^\"]*\""""
    t.value = t.value.replace("\"", "")
    return t


def t_Int(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_ANY_NextLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")


def t_ANY_error(t):
    print(f"Unknown token value at line {t.lexer.lineno}: ", end="")
    print(t.value)


lexer = lex.lex()
if __name__ == "__main__":

    with open("./test.lang", "r") as file:
        content = file.read()

    lexer.input(content)

    token = lexer.token()

    while token:
        print(token)

        try:
            token = lexer.token()
        except StopIteration:
            print("Fin...")
            break
