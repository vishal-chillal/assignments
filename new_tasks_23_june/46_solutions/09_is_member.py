# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.

def is_member(value,list_of_value):
    result = False
    for val in list_of_value:
        if val == value:
            result = True
            break
    return result
