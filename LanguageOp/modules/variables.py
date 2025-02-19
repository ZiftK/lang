vars = {}


def p_VarValue(p):
    """VarValue : VarName"""

    if not (p[1] in vars):
        raise Exception(f"Unknown variable {p[1]}")

    variable: dict = vars.get(p[1])
    p[0] = variable.get("value")
    p.slice[0].type = variable.get("type")
