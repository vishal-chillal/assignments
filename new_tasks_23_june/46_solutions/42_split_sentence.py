# 42.A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that

# Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
# Periods followed by a digit with no intervening whitespace are not sentence boundaries.
# Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
# Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
# Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.
import re

abbrivations = ["Mr.", "Miss.", "Jr.", "Dr."]

regex = r"([^\.\!\?]*.?[\s\.\?\!]?[a-z\d\s\.,']*)"

# regex = r"([\w\d\s\.,']*.?[\s\.\?\!]?[a-z\d\s\.,']*)"



s = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't"
x = re.findall(regex,s)
# print s,"\n\n"

for i in x:
    i = i.strip(" ")
    if i in abbrivations:
        print i,
    else:
        print i
