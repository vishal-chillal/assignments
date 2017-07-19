# Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def length_of_string(string):
    length = 0
    for _ in string:
        length += 1 
    return length

def length_using_reduce(string):
    print reduce(lambda count, char: count + 1, string, 0)

if __name__ == "__main__":
    inputs = raw_input("Enter Your String OR List: ")
    print "for loop: ", length_of_string(inputs)
    print "reduce function: ", length_using_reduce(inputs)

