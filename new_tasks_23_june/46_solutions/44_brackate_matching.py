# Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.

from random import choice
import re
def generate_brackets(n):
    return "".join(choice("[]") for _ in range(n*2))

def validate_brackets():
    n = input()
    stack = 0
    brackets_string = "]][["
    # brackets_string = generate_brackets(n)
    for i in brackets_string:
        if i == ']' and stack != 0:
            stack -= 1

        elif i == '[':
            stack += 1

        else:
            stack = -1
            break
    if stack != 0:
        print brackets_string, "\tNOT OK"
    else:
        print brackets_string, "\tOK"

if __name__ == "__main__":

	validate_brackets()
