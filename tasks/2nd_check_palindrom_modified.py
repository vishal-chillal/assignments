def validate_palindrom_using_for_loop(string):
    n = len(string)
    start = 0
    end = n-1
    for i in xrange(n/2):
        if not(string[start].isalnum()):
            start += 1
            continue
        elif not(string[end].isalnum()):
            end -= 1
            continue
        elif(string[start] != string[end]):            
            print "not palindrom"
            return
    print "palindrom"
    return

if __name__ == "__main__":
    print "Enter your shring :"
    inp = raw_input()
    validate_palindrom_using_for_loop(inp)
