# 24.The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

def make_3sg_form(verb):
    if verb == None:
        return
    verb = verb.lower()
    set_of_end_points = ["o", "h", "s", "x", "z"]
    if verb.endswith('y'):
        vreb = vreb[:-1]+"ies"
    elif verb[-1] in set_of_end_points:
        if verb[-1] == "h" and (verb[-2] == "s" or verb[-2] == "c"):
            verb += "es"
        else:
            verb += "es"
    else:
        verb += "s"
    return verb
