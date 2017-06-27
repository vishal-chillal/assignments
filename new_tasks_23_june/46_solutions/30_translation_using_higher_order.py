# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} and use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.
def translate(word_list):
    base_dict =  {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    res = []
    return map(lambda y:base_dict[y] ,filter(lambda x: base_dict.has_key(x), word_list))

print translate(["happy","new","year"])
