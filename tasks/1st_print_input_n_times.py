def validate_digit(n):
    return n.isdigit()

def print_input_n_times(inp, n, option):
    ''' function for printing given input given n times '''
    if option == 1:
        for x in range(n):
            print inp 
    elif option == 2:
        print inp*n
    else:
          print "sorry ...! Invalid selection"
    return
    
if __name__ == "__main__":
    print "Enter N :"
    n = raw_input()
    if validate_digit(n):
        n = int(n)
        print "enter string for printing"
        inp = raw_input()
        print "select mode:\n1.print on new line.\n2.print on same line."
        option = raw_input()
        if validate_digit(option):
            print_input_n_times(inp, int(n), int(option))
            exit(0)
    print "Invalid Input"
        
        
