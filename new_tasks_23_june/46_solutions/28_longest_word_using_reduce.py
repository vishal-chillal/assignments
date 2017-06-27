# 28.Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
def find_longest_word(word_list):
    return reduce (lambda x,y: max(len(x),len(y)), word_list)

