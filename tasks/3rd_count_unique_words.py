from sys import argv

def open_file(file_name):
	''' check if any errors in the file like validity/permissions and return file handler'''
        try:
		fp = open(file_name,'r')
	except Exception as e:
		print e
		return
        file_text = ''.join(e for e in fp.read() if e.isalnum() or e == " ")
        return file_text

def count_unique_words_using_set(fp):
        word_list = fp.split()
        print "count of unique words in file is:", len(set(word_list))


def count_unique_words(fp):
        '''
        in this function actual words are counted and count maintained in dictionary
        with word as KEY and its count as VALUE
        '''
        word_list = fp.split()
        word_dict = {}
        for word in word_list:
                if word not in word_dict:
                        word_dict[word] = 1
                else:
                        word_dict[word] += 1
        print "unique_word_count: ", len(word_dict)

if __name__ == "__main__":
        if(len(argv) != 2):
                print "please give input file."
                exit(0)
        file_name = argv[1]
        fp = open_file(file_name)
        if fp == None:
                exit(0)
                
        count_unique_words(fp)
        
        count_unique_words_using_set(fp)
