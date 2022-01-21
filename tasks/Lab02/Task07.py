import random

name = input("Your Name: ")
print("Good Luck ! ", name)

words = ["python", "data", "iti", "course"]
word = random.choice(words)         # get random word

print("------------Guess the characters------------")

guesses = ''

turns = 7           # turns number

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end = '')
        else:
            print("_")
            failed += 1     # increment when fails

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    guess = input("guess a character: ")     # enter another char if failed

    guesses += guess            # store all inputs in guesses

    # check input with the character in word
    if guess not in word:
        turns -= 1
        print("Wrong Guess !")
        print(f"remaining {turns} turns")
        if turns == 0:
            print("You Loose ... no more turns")
