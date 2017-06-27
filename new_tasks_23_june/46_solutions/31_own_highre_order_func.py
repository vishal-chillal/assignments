# Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good exercise.)Simple exercises including I/O
def map(function ,my_list):
    result = []
    for elt in my_list:
        result.append(function(elt)+1)
    return result

def filter(function ,my_list):
    result = []
    for elt in my_list:
        result.append(function(elt))
    return result

def reduce(function,my_list):
    ln =  len(my_list)
    if ln < 2 :
        return
    val = my_list[0]
    for elt in range(1,ln):
        val = function(val,my_list[elt])
    return val
