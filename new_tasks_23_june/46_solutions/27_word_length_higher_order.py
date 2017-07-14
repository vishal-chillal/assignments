# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
def word_length_for_loop(word_list):
    length = []
    for word in word_list:
        length.append(len(word))
    return length

def word_length_higher_order(word_list):
    return map(lambda x:len(x), word_list)

def word_length_list_comprehensions(word_list):
    return [len(x) for x in word_list]



if __name__ == "__main__":
    word_list = ["hie", "there","bye","\n"]
    print word_length_list_comprehensions(word_list)

