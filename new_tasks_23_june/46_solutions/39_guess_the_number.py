# 39.Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20.

from random import randint
def check_the_guess(number, guess_count):
    guess_count += 1
    guess_number = get_the_guess()
    if guess_number == answer:
        print "Good job," + user_name + " ! You guessed my number in " + str(guess_count) + " guesses!"
        return 1
    else:
        print "Your guess is too low."
        return check_the_guess(number, guess_count)
def get_the_guess():
    print "Take a guess."
    guess = raw_input()
    try:
        guess = int(guess)
    except Exception as e:
        print e
        get_the_guess()
    return guess

def get_user_name():
    user_name = raw_input()
    if user_name == "":
        print "please entyer your name"
        return get_user_name()
    return user_name

if __name__ == "__main__":
    print "Hello! What is your name?"
    global user_name
    user_name = get_user_name()
    print "Well," + user_name + ", I am thinking of a number between 1 and 20"
    guess_count = 0
    answer = randint(1,20)
    check_the_guess(answer, guess_count)
