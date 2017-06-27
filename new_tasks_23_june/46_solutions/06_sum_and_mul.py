# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.

def sum(ls):
    sum_result = reduce(lambda x, y : x+y,ls)
    
def multiply(ls):
    mul_result = reduce(lambda x, y : x*y,ls)
