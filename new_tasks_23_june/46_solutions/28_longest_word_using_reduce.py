# 28.Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
def find_longest_word(word_list):
    try:
        return len(reduce(lambda x,y: max(x,y), word_list))
    except TypeError:
        print "Invalid List"
        exit(0)
    

if __name__ == "__main__":
    word_list = ["hie", "there","bye","as"]
    print find_longest_word([])
