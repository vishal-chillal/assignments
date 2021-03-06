# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
def over_laping_using_IN_fun(lst1, lst2):
    result = False
    for elt1 in lst1:
        if elt1 in lst2:
            result = True
            break
    return result

def over_laping_using_for_loops(lst1, lst2):
    for elt1 in lst1:
        for elt2 in lst2:
            if elt1 == elt2:
                return True                
    return False

def overlaping_using_sets(lst1, lst2):
    res = False
    if len(set(lst1).intersection(set(lst2))) > 0:
        res = True
    return res

def using_filter(lst1, lst2):
    op = filter(lambda elt1:elt1 in lst2,lst1 )
    return op != []



if __name__ == "__main__":

    list1 = [1,2,3]
    list2 = [11,12,1]

    print overlaping_using_sets(list1, list2)
