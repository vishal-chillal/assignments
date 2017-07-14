# Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
def reverse(string):
    return string[::-1]

def rev_using_for_loop(string):
    rev_str = ""
    for char in string:
        rev_str = char+rev_str
    return rev_str

if __name__ == "__main__":
    string = raw_input("Enter String: ")
    print reverse(string)
    print rev_using_for_loop(string)
