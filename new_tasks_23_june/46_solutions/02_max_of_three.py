# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(n1, n2, n3):
    max1 = max(n1, n2)
    return max(max1, n3)

if __name__ == "__main__":
    inputs = raw_input("Enter space saperated 3 numbers: ").split()
    while(len(inputs) != 3):
        inputs.append(input())
    try:
        
        print max_of_three(float(inputs[0]),float(inputs[1]),float(inputs[2]))
    except ValueError:
        print "Invalid numbers"
