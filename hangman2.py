#Hangman
#Justin H


import os
import random

def start_screen():
    path = "art"
    file = 'art/splash_screen.txt'

    with open(file, 'r') as f:
        lines = f.read()
        
    print(lines)

def show_credits():
    path = "art"
    files = 'art/credits.txt'

    with open(files, 'r') as f:
        lines = f.read()
        
    print(lines)
    
def get_puzzle():
    path = "puzzles"

    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        with open(path + "/" + f, "r") as f:
            beginning_lines = f.read().splitlines()
        category_name = beginning_lines[0]
        print(str(i + 1) + ") " + category_name)
              
    print()
    choice = input("Please pick the number of the category that you would like to play. ")
    print()
    print("*NOTE*: if you think that my word has a space, press the space bar as a guess.")
    choice = int(choice)
    choice = choice - 1

    file = path + "/" + file_names[choice]
  

    with open(file,"r")as f:
        lines = f.read().splitlines()

    

    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    print(category_name)
    return puzzle
    

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if len(letter) == 1:
            if(letter).isalpha():
                return letter
            else:
                print("Only enter one letter.")
                print()
        else:
                print("Only enter one letter.")
                print()

def display_board(solved):
    print(solved)

def show_result(result):
    if result == 0:
         print("Congradulations! You won")
    else:
        print("You suck.")
    

def play_again(name):
    while True:
        decision = input("Would you like to play again " + name + " ? (y/n)")
        print()
        decision = decision.lower()

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            print("See you later!")
            return False
        
        else:
            print("Enter valid response.")
    
def play(name):
    print("You are now playing Hangman, " + name + "!! ")
    print()
    print("I will give you 6 guesses to guess the word.")
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6
    result = 0
    print(solved)
    gameover = 0

    while solved != puzzle and gameover == 0:
        letter = get_guess()

        if letter not in puzzle:
            strikes +=1
            print("That letter is not in the word.")
            print()
            print("You have " + str(strikes) + " strikes.")
            print()
            if strikes == limit:
                print("You lost. How can you be so dumb?")
                print()
                result = 1
                gameover = 1
                print(puzzle)
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(result)

    
# Game starts running here
start_screen()
playing = True

while playing:
    name = input("What name would you like to go by? ")
    play(name)
    playing = play_again(name)
show_credits()
