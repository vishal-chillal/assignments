# Write a function translate() that will translate a text into
# " (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between.
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".


def translate(string):
    """Take an input string and returns translated "robber's" language string """
    exceptions = "aeiou "
    result = ""
    for i in string:
        if i.lower() not in exceptions:
            result += i+'o'+i
        else:
            result += i
    return result

if __name__ == "__main__":
    string = raw_input("Enter Your Text For Translation: ")
    print translate(string)
