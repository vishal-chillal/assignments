# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python
def max(num1,num2):
    ''' takes two numbers and return maximum of them'''
    if num1 > num2:
        return num1
    return num2

if __name__ == "__main__":
    inputs = raw_input("Enter space saperated 2 numbers: ").split()
    if len(inputs) != 2:
        inputs.append(input())
    try:
        print max(float(inputs[0]),float(inputs[1]))
    except ValueError:
        print "Invalid numbers"
        
