# An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:
# "board": makes "bad" and "or".
# "waists": makes "wit" and "ass

def  print_alternade(word_list, word):
    ln = len(word)
    even_pos_word = ""
    odd_pos_word = ""
    for i in range(ln):
        if i%2 ==0:
            even_pos_word += word[i]
        else:
            odd_pos_word += word[i]
    if even_pos_word in word_list and odd_pos_word in word_list:
        print "\"" + word + "\" makes \"" + odd_pos_word + "\" and \"" + even_pos_word + "\""

def alternade():
    try:
        with open("unixdict.txt", 'r') as fp:
            file_text = fp.read()
    except Exception as e:
        print e
        return 0

    word_list = file_text.split()
    map(lambda x: print_alternade(word_list, x),word_list)

if __name__ == "__main__":

	alternade()
