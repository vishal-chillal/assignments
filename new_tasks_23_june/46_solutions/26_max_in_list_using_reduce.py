# 26.Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
def max_in_list(num_list):
    try:
        return reduce(lambda x,y: max(x,y),num_list)
    except TypeError:
        print "Invalid List"
        exit(0)

if __name__ == "__main__":
    value_list = [02.2,4,12]
    print max_in_list(value_list)



