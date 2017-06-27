# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
def word_length(word_list):
    word_length_count_list = []
    for word in word_list:
        word_length_count_list.append(len(word))
    
