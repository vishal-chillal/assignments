#43.An anagram is a type of word play,the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.

def get_words_from_file(file_name):
    '''
    assuming that the input file will have only one word per line.
    '''
    word_list = []
    try:
        with open(file_name,"r") as fp:
            word_list = fp.read().split('\n')

    except Exception as e:
        print e
    return word_list

def find_anagram(char_dict,word):
    anagram_list = {}
    if len(word) != 1:
        for char in word:
            tmp_lst = set(filter(lambda x:x.count(char) == word.count(char) and  len(x) == len(word) ,char_dict[char]))
            if anagram_list == {}:
                anagram_list = tmp_lst
            else:
                anagram_list = anagram_list.intersection(tmp_lst)
    return anagram_list

def create_dict(word_list):
    char_dict = {}
    for word in word_list:
        for char in word:
            if char not in char_dict:
                char_dict[char] = {word}
            else:
                char_dict[char].add(word)
    return char_dict
    
def anagram():

    word_list = get_words_from_file("unixdict.txt")
    char_dict = create_dict(word_list)
    cnt = -1
    anagram_word_lst = {1}
    for word in word_list:
        if word not in anagram_word_lst:
            lst = find_anagram(char_dict, word)
            if len(lst) > 2:
                print lst, word
                anagram_word_lst.update(lst)
    print anagram_word_lst     
anagram()
