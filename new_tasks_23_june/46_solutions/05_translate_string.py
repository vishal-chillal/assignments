# Write a function translate() that will translate a text into
# " (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between.
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".


def translate(string):
    exceptions = "aeiou \n"
    result = ""
    for i in string:
        if i not in exceptions:
            result += i+'o'+i
        else:
            result += i
    return result

