# 29.Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n

def filter_long_words(word_list,n):
    try:
        return filter(lambda x:len(x)>=n,word_list)
    except TypeError:
        print "Invalid List"
        exit(0)
    

if __name__ == "__main__":
    word_list = ["hie", "there","bye","as"]
    n = 3
    print filter_long_words(word_list,n)


    
