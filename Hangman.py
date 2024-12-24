import random
print("Starting Hangman")

def printPrettyList(lst):
    # Replace empty strings with underscores
    formatted = [x if x != "" else "_" for x in lst]
    # Join the list into a single string with spaces between elements
    print(" ".join(formatted))

# Read words from the file
with open("words.txt", "r") as file:
    possibleWords = file.read().splitlines()
# Select a random word
randWord = random.choice(possibleWords)
# Turn word into a list
randomWord = list(randWord)

# Create base
print("Random Word Chosen")
guessedLetters = [""] * len(randomWord) 

lives = 5
while (lives > 0):
    printPrettyList(guessedLetters)
    chosenLetter = input("What is your guess?: ")
    if(chosenLetter in randomWord):
        print("yes")
        guessedLetters[randomWord.index(chosenLetter)] = chosenLetter
    else:
        print("no")
        lives -= 1
    if("" not in guessedLetters):
        print("YOU DID IT!!")
        break

    print("Lives left: ", lives)

print("The word was", randWord)
