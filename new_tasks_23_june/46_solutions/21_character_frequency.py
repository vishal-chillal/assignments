# 21.Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(string):
    char_freq_dict = {}
    for char in string:
        if char not in char_freq_dict:
            char_freq_dict[char] = 1
        else:
            char_freq_dict[char] += 1
    return char_freq_dict

print char_freq("abbabcbdbabdbdbabababcbcbab")

