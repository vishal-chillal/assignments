# 41.In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the following way:

# animal_list = ["tiger", "horse", "panther"]
def check_guess(name):
    guess = raw_input()
    guess_ln =  len(guess)
    ln = min(len(name),guess_ln)
    output = ""
    for index in range(ln):
        if guess[index] == name[index]:
            output += '['+guess[index]+']'
        elif guess[index] in name:
            output += '('+guess[index]+')'
        else:
            output += guess[index]
    if(guess_ln > ln):
        for index in range(ln,guess_ln):
            if guess[index] in name:
                output += '('+guess[index]+')'
            else:
                output += guess[index]
    print "Clue:  ",output
    if(name != guess):
        check_guess(name)

def lingo():
    animal = "tiger"
    check_guess(animal)

