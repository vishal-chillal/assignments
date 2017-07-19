# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.

def is_member(value,a):
    result = False
    for val in a:
        if val == value:
            result = True
            break
    return result

def is_member_by_filter(value, a):
    print filter(lambda x : x == value, a) != []

if __name__ == "__main__":
    value = 12
    search_list = [1, 12, 4, "nine"]
    print is_member(value, search_list)
    is_member_by_filter(value, search_list)
