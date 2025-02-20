from modules.object_types.boolean_object import Boolean


def p_BooleanExpression(p):
    """BooleanExpression : BooleanOr"""
    if not (p[0].__class__ is Boolean):
        p[0] = Boolean(content=p[1])
        return
    p[0] = p[1]


def p_BooleanOr(p):
    """BooleanOr : BooleanOr Or BooleanAnd
                | BooleanAnd"""
    match (len(p)):
        case 2:
            p[0] = p[1]
            return
        case 4:
            p[0] = p[1] or p[3]
            return


def p_BooleanAnd(p):
    """BooleanAnd : BooleanAnd And BooleanGroup
                    | BooleanGroup"""
    match (len(p)):
        case 2:
            p[0] = p[1]
            return
        case 4:
            p[0] = p[1] and p[3]
            return


def p_BooleanGroup(p):
    """BooleanGroup : LGroup BooleanExpression RGroup
                    | Boolean
                    | VBoolean"""
    match (len(p)):
        case 4:
            p[0] = p[2]
            return
        case 2:
            p[0] = p[1]
            return


def p_Boolean(p):
    """Boolean : True
                | False"""
    match p.slice[1].type:

        case "False":
            p[0] = False
            return
        case "True":
            p[0] = True
