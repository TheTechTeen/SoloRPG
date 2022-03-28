from random import randint
import theme as t

def relation_to(c1, c2):
    r1 = c1.relationships
    r2 = c2.relationships

    o1 = c1.organization
    o2 = c2.organization

    if c2 in r1.keys():
        return r1[c2]

    org = False
    theme = False
    if o2 in r1.keys():
        org = True
        base = r1[o2]
    elif o1 & o2 in o1.relationships.keys():
        org = True
        base = o1.relationships[o2]
    elif c2.theme in r1.keys():
        theme = True
        base = r1[c2.theme]
    else:
        theme = True
        base = t.RELATIONSHIPS[c1.theme].get(c2.theme)

    if theme:
        rval = 2
        base += randint(-rval, rval)
    else:
        rval = 2 / c1.loyalty

    relationship = base + randint(-rval, rval)

    if relationship < -3:
        relationship = 3
    if relationship > 3:
        relationship = 3

    return relationship

def org_relation(o1, o2):
    r1 = o1.relationships
    r2 = o2.relationships

    if o2 in r1.keys():
        return r1[o2]
    else:
        return t.RELATIONSHIPS[o1.theme].get(o2.theme, 0)

    return base + randint(-rval, rval)    