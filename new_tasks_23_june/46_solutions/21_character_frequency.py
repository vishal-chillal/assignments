# 21.Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(string):
    char_freq_dict = {}
    for char in string:
        try:
            char_freq_dict[char] += 1
        except KeyError:
            char_freq_dict[char] = 1
    return char_freq_dict

if __name__ == "__main__":
	print char_freq("abbabcbdbabdbdbabababcbcbab")

