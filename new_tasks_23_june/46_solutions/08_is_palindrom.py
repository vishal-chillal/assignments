# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True
def is_palindrom(string):
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
    string = raw_input("Enter String: ")
    is_palindrom(string)
