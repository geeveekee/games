from hangman import display_hangman
import random

def getRandomWord():
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']
    word = random.choice(words)
    return word.upper()

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Lets play!")
    print(display_hangman(tries))
    print(wordCompletion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word").upper()

        #checking the guess (letter)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You've already guessed that letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -=1
                guessedLetters.append(guess)
            else:
                print("Great!, ", guess, " is in the word")
                guessedLetters.append(guess)
                wordList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordList[index] = guess
                wordCompletion = "".join(wordList)
                if "_" not in wordCompletion:
                    guessed = True

        #checking the guess (word)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, " is not the word")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word

        #checking for all other input cases
        else:
            print("Please enter a vlid guess.")
        print(display_hangman(tries))
        print(wordCompletion)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the word, You win!")
    else:
        print("Sorry, you ran out of tries. The word was"+ word)

def main():
    word = getRandomWord()
    play(word)
    while input("Play again? (y/n)") == 'y':
        word = getRandomWord()
        play(word)
