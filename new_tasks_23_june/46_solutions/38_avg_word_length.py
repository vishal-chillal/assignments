# 38.Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
def calculate_word_lenght(word_list):
    word_length_count_list = []
    for word in word_list:
        word_length_count_list.append(len(word))
    return word_length_count_list

def calculate_avg_word_length(word_length_count_list):
    return sum(word_length_count_list)/len(word_length_count_list)

def create_word_list(file_name):
    word_list = []
    try:
        with open(file_name,"r") as fp:
            word_list = fp.read().replace('\n',"").split()
    except Exception as e:
        print e
    return word_list

if __name__ == "__main__":
    file_name = raw_input("insert_filename: ")
    word_list = create_word_list(file_name)
    word_length_count_list = calculate_word_lenght(word_list)
    print calculate_avg_word_length(word_length_count_list)
                            
