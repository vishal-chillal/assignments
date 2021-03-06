# Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good exercise.)Simple exercises including I/O
def map(function ,my_list):
    result = []
    for elt in my_list:
        result.append(function(elt)+1)
    return result

def filter(function ,my_list):
    result = []
    for elt in my_list:
        if function(elt) == True:
            result.append(elt)
    return result

def reduce(function,my_list):
    ln =  len(my_list)
    if ln < 2 :
        return
    val = my_list[0]
    for elt in range(1, ln):
        val = function(val,my_list[elt])
    return val

def square(elt1):
    return elt1**2

def add(elt1,elt2):
    return elt1+elt2

def is_even(elt1):
    return elt1%2 == 0

if __name__ == "__main__":
    inp_list = [1,2,3,4,5]
    print "map: square", map(square, inp_list)
    print "filter: is_even", filter(is_even, inp_list)
    print "reduce: addition", reduce(add, inp_list)
