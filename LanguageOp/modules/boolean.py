def p_BooleanExpression(p):
    """BooleanExpression : BooleanOr"""
    p[0] = p[1]


def p_BooleanOr(p):
    """BooleanOr : BooleanAnd Or BooleanAnd
                | BooleanAnd"""
    match (len(p)):
        case 2:
            p[0] = p[1]
            return
        case 4:
            p[0] = p[1] or p[3]
            return


def p_BooleanAnd(p):
    """BooleanAnd : BooleanAnd And BooleanAnd
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

