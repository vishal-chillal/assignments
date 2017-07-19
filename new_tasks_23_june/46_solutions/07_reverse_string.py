# Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
def reverse(string):
    return string[::-1]

def rev_using_for_loop(string):
    rev_str = ""
    for char in string:
        rev_str = char+rev_str
    return rev_str

def reverse_str(string):
    return "".join([string[x] for x in range(len(string)-1,-1,-1)])
if __name__ == "__main__":
#def main():
    string = raw_input("Enter String: ")
    print reverse(string)
    print rev_using_for_loop(string)
    print reverse_str(string)
#main()
