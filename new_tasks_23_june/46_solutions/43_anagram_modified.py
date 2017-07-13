#43.An anagram is a type of word play,the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.

def get_words_from_file(file_name):
    '''
    assuming that the input file will have only one word per line.
    '''
    word_list = []
    try:
        with open(file_name,"r") as fp:
            word_len_dict = {}
            for word in fp:
                word = word.rstrip("\n")
                word_list.append(word)
                try:
                    word_len = len(word)
                    word_len_dict[word_len].append(word)
                except KeyError:
                    word_len_dict[word_len] = [word]
    except Exception as e:
        print e
        exit(0)
    return word_list,word_len_dict

def find_match(word,word_len_dict):
    word_list = word_len_dict[len(word)]
    index = 0
    global count
    sorted_word = sorted(word)
    remaining = []
    while word_list != []:
        try:
            check_word = word_list[index]
            if sorted_word == sorted(check_word):
                remaining.append(word_list.pop(index))
        except IndexError:
            break
        index += 1
    if(len(remaining) > 1):
        count += 1
        print remaining
def anagram():
    word_list,word_len_dict = get_words_from_file("unixdict.txt")
    map(lambda word:find_match(word,word_len_dict),word_list)
    print count

count = 0
anagram()
