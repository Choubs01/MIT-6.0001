import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def load_words(): #Gets words from txt file and compiles them into a list
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    return wordlist
wordlist = load_words()

def get_frequency_dict(sequence): #Returns frequency of each letter in a word as a dictionary
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n): #Returns the score for a word, where word is the input word, and n is the letters in the available hand
    x = 0 #Sum of scores for letters in word
    word = list(word.lower())
    for letters in word:
        for a, b in SCRABBLE_LETTER_VALUES.items():
            if letters == a:
                x += int(b)
    y = 7*len(word) - 3*(n - len(word)) #Second component for score
    if y < 0:
        y = 1
    return x*y


def display_hand(hand): #Prints the hand in a visible way, e.g. 'bvfek' --> b v f e k
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')
    print()

def deal_hand(n):  #Returns a hand of n/3 rounded up minus 1 vowels, 1 wildcard, and the rest are consonants
    hand={}
    num_vowels = int(math.ceil(n / 3)) #Adds floor of n/3 vowels
    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1 #Add wild card

    for i in range(num_vowels, n):  #Adds remaining n consonants
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand

def update_hand(hand, word): #Returns a new dictionary that contains the hand minus the letters used in word
    hand1 = hand.copy()
    word = list(word.lower())
    dict = get_frequency_dict(word)

    for letters in hand1.keys():
        for letters1 in dict.keys():
            if letters == letters1:
                hand1[letters] = hand1.get(letters, 0) - dict[letters]

    lst = []
    for a, b in hand1.items():  #Weird but only method for deleting terms in a dictionary, can't loop through it simply
        if b < 1:
            lst.append(a)
    for letters in lst:
        hand1.pop(letters)

    return hand1

def is_valid_word(word, hand, word_list):  #First check if word is composed only of letters in hand, then check if word matches up with number of letters in hand, then check if word is in data
    dict = get_frequency_dict(word.lower())
    hand1 = hand.copy()
    wordlst = list(word.lower())
    handlst = []
    word_matches_hand = True

    for keys in hand1.keys():   #Check if word is composed only of letters available in hand
        handlst.append(keys)
    for letters in wordlst:
        if letters not in handlst:
            return False

    for letters in hand1.keys():    #Check that letters in word don't exceed available letters in hand
        for letters1 in dict.keys():
            if letters == letters1:
                hand1[letters] = hand1[letters] - dict[letters]
    for values in hand1.values():
        if values < 0:
            return False

    if '*' in wordlst: #Accounts for wildcard if it exists, else just checks if word is in data
        wildcard_position = ''.join(wordlst).find('*')
        for i in list(VOWELS):
            wordlst[wildcard_position] = i
            if ''.join(wordlst) in word_list:
                return True
        return False
    elif word.lower() in word_list:
        return True
    else:
       return False

def calculate_handlen(hand): #Calculates the number of letters in a hand
    sum = 0
    for a in hand.values():
        sum += int(a)
    return sum

def play_hand(hand, word_list):
    hand1 = hand.copy()
    score = 0
    print("\nCurrent Hand:"), display_hand(hand1)
    substitute = str(input("Would you like to change a letter in the current hand? ")).lower()
    if substitute == 'yes' or substitute == 'y':
        try:
            substitute_letter = str(input("Which letter would you like to change? "))
            hand1 = substitute_hand(hand1, substitute_letter)
        except:
            print("Invalid input.")

    while True:
        if len(hand1) == 0:
            print("You have exhausted your current hand. Your score for this hand: " + str(score) + ' points.')
            return score
        print("\nCurrent Hand:"), display_hand(hand1)
        word = input("\nWhat is your word? ")
        if word == '!!':
            print("Total score for this hand " + str(score) + ' points.')
            return score
        elif word == '!!!':
            print("Total score: " + str(score) + ' points.')
            exit()
        if is_valid_word(word, hand1, word_list) == True:
            score += get_word_score(word, calculate_handlen(hand1))
            print("-", word, '-', "has earned", str(get_word_score(word, calculate_handlen(hand1))), "points.")
            hand1 = update_hand(hand1, word)
            continue
        else:
            print("Invalid word.")
            hand1 = update_hand(hand1, word)
            continue

def substitute_hand(hand, letter):  #Substitutes a letter in current hand
    hand1 = hand.copy()
    handlst = []
    for keys in hand1.keys():
        handlst.append(keys)

    alphabet = list('qwertyuiopasdfghjklzxcvbnm')
    alphabet.remove(letter)
    random_letter = random.choice(alphabet)
    value = hand1[letter]
    hand1.pop(letter, None)

    if random_letter in handlst:  #Need to account for case when the random letter is a letter already in hand
        hand1[random_letter] += value
    else:
        hand1[random_letter] = value
    return hand1

def play_game(word_list):
    score = 0
    print("Welcome to this word game. If you would like to end your current hand, type '!!'. Else if you would like to quit, type '!!!'.")
    try:
        hands = int(input("Enter the number of hands you would like to play: "))
    except:
        print("Invalid input.")
    for i in range(hands):
        score += int(play_hand(deal_hand(8), word_list))
        print("Total score: ", score, "points.")
        print("-------------------", '\n')

play_game(wordlist)
