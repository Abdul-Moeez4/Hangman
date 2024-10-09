import random
import os
import time
#import tkinter as tk


words = [
    'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm',
    'compiler', 'database', 'encryption', 'firewall', 'hardware',
    'internet', 'java', 'kernel', 'malware', 'network', 'object',
    'protocol', 'query', 'router', 'security', 'token', 'url',
    'virtual', 'wireless', 'xml', 'yaml', 'zip', 'abstract', 'binary',
    'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal',
    'iteration', 'juxtapose', 'keystroke', 'lambda', 'metadata', 'node']

hangman_stages = ["""
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""", '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''',]

def rules():
    os.system('cls')
    print("================ RULES =====================\n")
    
    print("   - Guess the hidden word by suggesting letters within limited attempts.\n")

    print("   - A random word is chosen and displayed as underscores (_).\n")

    print("   - Players guess one letter at a time.\n")

    print("   - Correct guesses reveal the letter; incorrect guesses draw part of the hangman.\n")
   
    print("   - 6 incorrect guesses lead to losing the game.\n")
 
    print("   - Win by guessing the word before the hangman is fully drawn.\n")

    print("   - Have fun and enjoy guessing the word!\n")

    ready = input("Ready to start the game? (y/n)\n")
    if (ready == 'y' or ready == 'Y'):
        game_start();
    else:
        return;

def hangman_status(attempts,word_display):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Attempts = {attempts}")
    print(hangman_stages[attempts])
    print("Current Word " + " ".join(word_display))


def game_start():

    os.system('cls')
    #count attempts
    attempts = 6;

    #choose a random word
    chosen_word = random.choice(words)

    #when random word chosen, creating '_' according to word chosen
    word_display = ['_' for _ in chosen_word]
    print('3\n')
    time.sleep(0.5)
    os.system('cls')
    
    print('2\n')
    time.sleep(0.5)
    os.system('cls')

    print('1\n')
    time.sleep(0.5)
    os.system('cls')
    
    print('Get Ready to Play\n')
    time.sleep(1)


    print("Guess the Word: \n")
   
    #take in user input
    while attempts > 0 and '_' in word_display:
        hangman_status(attempts, word_display) #currrent state of hangman model
        user_input = input("Enter a letter: ").lower()

        #check if guessed word part of the random word chosen
        if user_input in chosen_word:
           for index, letter in enumerate(chosen_word):
                if letter == user_input:
                        word_display[index] = user_input
        else:
            attempts -= 1

        #winning condition
        if '_' not in word_display:
            hangman_status(attempts, word_display)
            print("Congratulations! You've guessed the word!")
            print("The word was: ",chosen_word)
            break

    if attempts == 0:
     hangman_status(attempts, word_display)
     print("Game Over! You've lost the game!")
     print("The word was: ",chosen_word)

#prompt user
print(" =============================== WELCOME TO THE A.M.S HANGMAN GAME ================================= ")
print('\n')

user_name = input(" What is your Fine Name? ")

user_rule_choice = input(f"Hello {user_name}, would you like to read the Rules of this mystical Game? (Y/N): ")
if (user_rule_choice == 'Y' or user_rule_choice == 'y'):
    rules();
else:
    print("LET THE GAME COMMENCE!")
    time.sleep(1)
    game_start()