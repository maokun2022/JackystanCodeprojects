"""
File: hangman.py
Name: Jacky Chang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is a hangman game.
    Thanks TA Cherry and Jenny for new_ans setting and trouble shooting
    """
    s = str(random_word())
    print("The word looks like: " + str("-"*len(s)))
    print("You have " + str(N_TURNS) + " guesses left.")
    guess = input("Your guess: ")
    check(guess)
    guess = guess.upper()
    count = N_TURNS
    new_ans = "-" * len(s)
    while True:
        if guess in s:
            count = count
            print("You are correct!")
            ans = ""
            for i in range(len(s)):
                if s[i] == guess:
                    ans = ans + guess
                elif new_ans[i].isalpha():
                    ans = ans + new_ans[i]
                else:
                    ans = ans + '-'
            new_ans = ans
            if '-' not in new_ans:
                print("You win!")
                print("The word was: " + s)
                break
            else:
                print("The word looks like: " + new_ans)
                print("You have " + str(count) + " guesses left.")
                guess = input("Your guess: ")
                check(guess)
                guess = guess.upper()
        else:
            count = count - 1
            if count == 0:
                print("You are completely hung : (")
                print("The word was: " + s)
                break
            else:
                print("There is no " + str(guess) + "'s" + " in the word.")
                print("The word looks like: " + new_ans)
                print("You have " + str(count) + " guesses left.")
                guess = input("Your guess: ")
                check(guess)
                guess = guess.upper()


def check(guess):
    while True:
        if guess.isalpha():
            if len(guess) != 1:
                print("illegal format.")
                guess = input("Your guess: ")
            else:
                return guess
        else:
            print("illegal format.")
            guess = input("Your guess: ")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
