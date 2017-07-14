# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.

def sum(ls):
    sum_result = reduce(lambda x, y : x+y,ls)
    return sum_result

def multiply(ls):
    mul_result = reduce(lambda x, y : x*y,ls)
    return mul_result

if __name__ == "__main__":
    list_size = input("Enter the list size :")
    inputs = []
    while(len(inputs) <= list_size):
        inputs.append(input())
    try:
        inputs = map(lambda x:float(x), inputs)
        print "addition of is ", sum(inputs)
        print "multiplication is",multiply(inputs)
    except ValueError:
        print "Invalid numbers"
