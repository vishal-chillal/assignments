# Write a function max_in_list() that takes a list of numbers and returns the largest one.
def max_in_list(lst):

    if lst == []:
        result == ""
    else:
        result = lst[0]
    for i in lst:
        if i > result:
            result = i
    return result
