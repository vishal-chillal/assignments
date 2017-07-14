# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
def word_length(word_list):
    word_length_count_list = []
    for word in word_list:
        word_length_count_list.append(len(word))
    print word_list
    print word_length_count_list

def word_maping_by_using_dict(word_list):
    word_length_count_dict = {}
    for word in word_list:
        word_length_count_dict[word] = len(word)
    print word_length_count_dict.items()

if __name__ == "__main__":
    word_list = ["vishal", "v","is"]
    word_length(word_list)
    word_maping_by_using_dict(word_list)
