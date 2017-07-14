# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.

def is_member(value,a):
    result = False
    for val in a:
        if val == value:
            result = True
            break
    return result

if __name__ == "__main__":
    value = 12
    search_list = [1,2,4,"nine"]
    print is_member(value, search_list)
