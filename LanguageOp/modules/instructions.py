from modules.variables import vars

types_eq = {
    "SuperString": "String",
    "SuperAlph": "Alph",
    "Integer": "Integer"
}


def p_ShowVal(p):
    r"""ShowVal : Show Integer
                | Show SuperString"""
    if p.slice[2].type == "VarName":
        if not p[2] in vars:
            raise Exception(f"Undefined variable {p[2]}")
        print(vars.get(p[2])[0])
    else:
        print(p[2])
    p[0] = p[2]


def p_VarAssign(p):
    r"""VarAssign :  StringType VarName Eq SuperString
                    | AlphType VarName Eq SuperAlph
                    | IntType VarName Eq Integer"""

    base_type = types_eq[p.slice[4].type]

    vars[p[2]] = (p[4], base_type)
    p[0] = p[4]
