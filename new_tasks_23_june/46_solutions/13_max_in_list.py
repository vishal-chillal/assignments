# Write a function max_in_list() that takes a list of numbers and returns the largest one.
def max_in_list(lst):

    if lst == []:
        result = ""
    else:
        result = lst[0]
    for number in lst:
        if number > result:
            result = number
    return result

if __name__ == "__main__":
    print max_in_list([1,2,3,-110,140.9,02])
