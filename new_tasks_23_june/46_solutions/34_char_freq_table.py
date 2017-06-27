# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.
def char_freq_table(file_name):
    try:
        with open(file_name, "r") as fp:
            file_text = fp.read()
    except Exception as e:
        print e
        return
    print file_text
    char_freq_dict = {}
    for char in file_text:
        if char in char_freq_dict:
            char_freq_dict[char] += 1
        else:
            char_freq_dict[char] = 1
    lst = sorted(char_freq_dict.items(), key = lambda tup: tup[0])
    print "char \t ascii_value \t count"
    for entry in lst:
        print entry[0], "\t  ", ord(entry[0]), "\t\t ", entry[1] 
if __name__ == "__main__":
    file_name = raw_input()
    char_freq_table(file_name)
