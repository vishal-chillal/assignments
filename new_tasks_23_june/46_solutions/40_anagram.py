# 40.An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that, when started 1) randomly picks a word w from given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user, and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to work with (say) colour words only. The interaction with the program may look like so:
import random

color_list =  ["white", "silver", "gray", "black", "navy", "blue", "cerulean", "skyblue", "turquoise", "chartreuse",
               "teal", "cyan", "green", "lime", "olive", "yellow", "amber", "orange", "brown", "azure", "gold",
               "red", "maroon", "violet", "magenta", "purple", "indigo", "peach", "apricot", "ochre", "plum"]

def anagram(color_list):
    color = random.choice(color_list)
    anagram = ''.join(random.sample(color,len(color)))
    return anagram,color

def check_guess(color):
    if color == raw_input().replace(" ",""):
        print "Correct!"
        return
    else:
        print "Guess the colour word!"
        check_guess(color)

if __name__ == "__main__":
    anagram,color = anagram(color_list)
    print "Color word anagram:  ", anagram
    check_guess(color)
