# 36.A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.
def find_hapex_legomen(file_text):
    word_list = sorted(list(set(file_text.lower().split())), key = len)
    ln = len(word_list)
    for word in word_list:
        if len(filter(lambda x: word in x, word_list)) == 1:
            print word
        
def hapex_legomen(file_name):
    if file_name == "" or file_name == None:
        return
    try:
        with open(file_name, 'r') as fp:
            find_hapex_legomen(fp.read())
    except Exception as e:
        print e
        return

if __name__ == "__main__":
	hapex_legomen("semordnip_inp.txt")
