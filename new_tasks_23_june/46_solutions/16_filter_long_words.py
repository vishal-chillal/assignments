# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
def filter_long_words(word_list,n):
    return filter(lambda x:len(x)>n,word_list)

if __name__ == "__main__":
    word_list = ["vishal", "v","is"]
    print filter_long_words(word_list,3)
