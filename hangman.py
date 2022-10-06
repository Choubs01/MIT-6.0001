import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    inFile = open(WORDLIST_FILENAME)
    line = inFile.readline()
    wordlist = line.split()
    return wordlist
wordlist = load_words()

def choose_word(wordlist):
    return random.choice(wordlist)

def unique_characters(secret_word): #Finds the number of unique characters in secret_word
    secret_word = list(secret_word)
    lst = []
    for letters in secret_word:
        if letters not in lst:
            lst.append(letters)
    return len(lst)

def is_word_guessed(secret_word, letters_guessed): #Checks if word has been guessed
    n = 0
    m = 0
    secret_word = list(secret_word)
    for letters in secret_word:
        for letters1 in letters_guessed:
            m += 1
            if letters1 == letters:
                n += 1
    if n == len(secret_word):
        return True
    else:
        return False

def is_letter_guessed(secret_word, letters_guessed): #Checks if letter has been guessed correctly
    n = 0
    secret_word = list(secret_word)
    for letters in secret_word:
        for letters1 in letters_guessed:
            if letters1 == letters:
                return True

def get_guessed_word(secret_word, letters_guessed): #Returns guessed letters of secret word, and blanks (_ ) for unguessed letters
    secret_word = list(secret_word)
    lst = []
    for letters in secret_word:
        n = 0
        for letters1 in letters_guessed:
            n += 1
            if letters1 == letters:
                lst.append(letters1 + ' ')
                break
            elif n == len(letters_guessed):
                lst.append("_ ")
    return   ''.join(lst)

def get_available_letters(letters_guessed): #Returns remaining unguessed letters
    n = -1
    alphabet = list(string.ascii_lowercase)
    for letters in alphabet:
        n += 1
        if letters in letters_guessed:
            alphabet[n] = "_"
    return ' '.join(alphabet)

print("Welcome to Hangman. If you would like to quit, enter 'Quit'.")
def hangman(secret_word):
    guesses_left = 6
    letters_guessed = []
    print("I am thinking of a word that is " +str(len(secret_word))+ " letters long.", '\n-------------------------------------')
    print('You have 6 guesses left.')
    print("Letters remaining:", string.ascii_lowercase)
    while guesses_left > 0:
        try:
            guess = input("\nWhich letter would you like to guess? ").lower()
        except:
            print("Invalid input, please input a single letter")
        if len(guess) != 1:
            print("Error: You must input 1 character.")
            continue
        if guess in letters_guessed:
            print("You've already guessed this letter.")
            continue
        letter_guessed = list(guess)
        letters_guessed.append(guess)
        if is_letter_guessed(secret_word, letter_guessed) == True:
            print('Good Guess: ', get_guessed_word(secret_word, letters_guessed))
        else:
            print("Bad Guess: ", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
        print('You have ' +str(guesses_left)+ ' guesses left')
        print('Remaining letters: ', get_available_letters(letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("You won! The secret word was " +str(secret_word) +".", "Your score is " +str(guesses_left * unique_characters(secret_word)) +".")
            quit()
        elif is_word_guessed(secret_word, letters_guessed) == False and guesses_left == 0:
            print("You lost. The secret word was " +str(secret_word) +".")
            quit()

print(hangman(choose_word(wordlist)))
