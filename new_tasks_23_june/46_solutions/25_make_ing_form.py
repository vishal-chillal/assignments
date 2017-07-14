# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:
import re
def make_ing_form(verb):
    if verb[-1] == 'e':
        regex = r"ee$|ye$|oe$"
        if verb[-2] == 'i':
            verb = verb[:-2]+"y"
        elif re.search(regex, verb) == None:
            verb = verb[:-1]
    else:
        regex = r"([bcdfghjklmnpqrstvwxz][aeiou][bcdfghjklmnpqrstvwxz])$"
        if re.search(regex, verb) != None:
            verb += verb[-1]
    return verb+"ing"

if __name__ == "__main__":
    word = raw_input()
    print make_ing_form(word)

