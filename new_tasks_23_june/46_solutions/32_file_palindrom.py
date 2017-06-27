# Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.
import re

def is_palindrom(string):
    result = True
    regex = r"[\W]+"
    string = re.sub(regex,r"",string)
    n = len(string)-1
    if string == "\n" or string == "":
        result = False
    for i in range(n/2+1):
        if string[i] != string[n-i]:
            result = False
    return result

def palindrome(file_name):
    if file_name == None:
        return
    try:
        with open(file_name,'r') as fp:
            for line in fp.readlines():
                if is_palindrom(line):
                    print line
    except Exception as e:
        print e
