# 20.Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"arr"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate(word_list):
    base_dict =  {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"arr"}
    res = []
    for i in word_list:
        if i in base_dict:
            res.append(base_dict[i])
    return res

