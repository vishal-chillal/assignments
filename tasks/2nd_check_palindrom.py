def check_palindrom_using_inbuilt_functions(input_string):
    inp = list(input_string)
    rev = list(input_string)
    rev.reverse()
    if inp == rev:
        print "palindrom"
    else:
        print "not palindrom"
        
def validate_palindrom_using_for_loop(string):
    n = len(string)
    for i in xrange(n/2):
        if(string[i] != string[n-i-1]):
            print "not palindrom"
            return
    print "palindrom"


if __name__ == "__main__":
    print "Enter your shring :"
    inp = raw_input()
    check_palindrom_using_inbuilt_functions(inp)
    validate_palindrom_using_for_loop(inp)
