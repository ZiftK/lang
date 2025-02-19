from modules.variables import vars


def p_Integer(p):
    r"""Integer : Int
                | StringLen"""

    if p.slice[1].type == "Int" or p.slice[1].type == "StringLen":
        p[0] = p[1]
        return

    if p.slice[1].type == "VarName":
        if not p[1] in vars:
            raise Exception(f"Undeclared varaible {p[1]}")
        tp = vars.get(p[1])[1]
        if not tp == "Int":
            raise Exception(f"A integer was expected. {p[1]} is a {tp}")
