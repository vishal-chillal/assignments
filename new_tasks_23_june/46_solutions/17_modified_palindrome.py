#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

def palindrom_modified(string):
    n = len(string)
    start = 0
    end = n-1
    for i in xrange(n/2):
        if not(string[start].isalnum()):
            start += 1
            continue
        elif not(string[end].isalnum()):
            end -= 1
            continue
        elif(string[start] != string[end]):            
            print "not palindrom"
            return
    print "palindrom"
    return
