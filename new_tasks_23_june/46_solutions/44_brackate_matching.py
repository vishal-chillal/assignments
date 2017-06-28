# Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.

from random import choice
import re
def generate_brackets(n):
    return "".join(choice("[]") for _ in range(n*2))

def validate_brackets():
    n = input()
    
    regex = r'(\[+\]+)'
    regex = r"[^[]*\[([^]]*)\]"

    for _ in range(n):
        stack = []
        # brackets_string = generate_brackets(n)
        brackets_string = "[[[[]][]]]"
        if(brackets_string.count(']') == brackets_string.count('[')):
            print re.findall(regex, brackets_string)
        else:
            print "err"
    # for i in brackets_string:
    #     if i == ']' and stack != [] and stack[-1] == '[':
    #         stack.pop()
    #     elif i == '[':
    #         stack.append(i)
    #     else:
    #         break
    # if stack != []:
    #     print brackets_string, "\tNOT OK"
    # else:
    #     print brackets_string, "\tOK"


validate_brackets()
