# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s.
def generate_n_chars(n,character):
    result = ""
    for _ in range(n):
        result += character
    return result

def generate_n_chars_using_lambda(n,character):
    result = lambda x:x*character
    return result(n)
