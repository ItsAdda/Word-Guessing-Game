import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

randomWordList = ["sun", "world", "happiness", "amazing" "water", "grass", "fork", "rain", "interrogation", "universe"]
randomWordListt = randomWordList.copy()


def getRandomWord():
    global randomWordListt
    os.system("title Word Game")
    guessedletters = set()
    lives = 5
    randomWord = random.choice(randomWordListt)
    randomWordListt.remove(randomWord)
    if not randomWordListt:
        print("You have guessed all the words")
        return
    lettersInRandomWord = set(randomWord)

    print(f"The word has {len(randomWord)} letters")
    display = ["_"] * len(randomWord)
    print(" ".join(display))

    while True:
        guess = input("guess a letter or the word: ").lower().strip()
        if not guess:
            continue

        if len(guess) > 1:
            if guess == randomWord:
                print(f"you guessed the word and it was '{randomWord}'")





            else:
                print("guess is incorrect")

        if guess not in guessedletters:
            guessedletters.add(guess)
            if guess in lettersInRandomWord:
                positions = [i + 1 for i, letter in enumerate(randomWord) if letter == guess]
                spots = ", ".join(map(str, positions))
                print(f"there is a letter '{guess}' in the spot(s): {spots}")
                for i, letter in enumerate(randomWord):
                    if letter == guess:
                        display[i] = guess
                print(" ".join(display))

                if lettersInRandomWord.issubset(guessedletters):
                    print(f"You guessed the word and it was '{randomWord}'")



            else:
                lives -= 1
                print(f"you have {lives} lives left")
                if len(guess) == 1:
                    print(f"there is no letter '{guess}' in the word")
                if lives <= 0:
                    print("you lost")
                    restart = input("Do you want to restart? (yes/no): ").lower()
                    if restart == "yes":
                        randomWordListt = randomWordList.copy()
                        getRandomWord()
                    else:
                        break
        else:
            print("you have already guessed that letter")


while True:
    if not randomWordListt:
        restart = input("do you want to restart? (yes/no): ").lower().strip()
        if restart == "yes":
            randomWordListt = randomWordList.copy()
            getRandomWord()

    else:
        getRandomWord()


