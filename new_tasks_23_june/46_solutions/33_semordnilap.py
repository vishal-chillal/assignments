# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

import re

def reverse_string(string):
    return string[::-1]

def check_semordinlap(file_text):
    regex = r"[\W]+"
    word_list_set = list(set(re.sub(regex,r" ",file_text).split()))
    n = len(word_list_set)
    for i in range(n):
        word = word_list_set[i]
        rev_str = reverse_string(word)
        if rev_str in word_list_set:
            print word , rev_str

def semordinlap(file_name):
    if file_name == "" or file_name == None:
        return
    try:
        with open(file_name, 'r') as fp:
            check_semordinlap(fp.read())
    except Exception as e:
        print e
        return

semordinlap("tmp")
