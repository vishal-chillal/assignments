# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
def find_longest_word(word_list):
    word_length_list = map( lambda x:len(x), word_list)
    return max(word_length_list)

def find_longest_word_using_for_loop(word_list):
    max_len = 0
    for word in word_list:
        word_len = len(word)
        if max_len > word_len :
            max_len = word_len
    return max_len

