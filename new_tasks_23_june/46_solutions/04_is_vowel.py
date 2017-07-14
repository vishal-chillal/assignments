# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def is_vowel(character):
    vowels = "aeiou"
    return character.lower() in vowels

if __name__ == "__main__":
    char = raw_input("Enter single character: ")
    print is_vowel(char)
