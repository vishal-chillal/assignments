#A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

def pangram(string):
    result = "Pangram"
    all_char = [x for x in range(ord('a'),ord('z')+1)]
    for char in all_char:
        if chr(char) not in string:
            result = "Not a Pangram"
            break
    return result

if __name__ == "__main__":
    string = "The quick brown fox jumps over the lazy dog"
    print string,"::\t",pangram(string)
    
