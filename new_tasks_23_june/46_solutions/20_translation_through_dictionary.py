# 20.Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"arr"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

base_dict =  {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"arr"}
res = []

def translate(word_list):
    for i in word_list:
        try:
            res.append(base_dict[i])
        except:
            res.append(i)
    return res

def translate_using_map(word_list):
    res = map(lambda x:base_dict[x], word_list)
    return res

print translate_using_map(["happy","merry","new"])
print translate(["happy","and"])
