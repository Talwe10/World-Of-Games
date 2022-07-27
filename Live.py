import MemoryGame
import GuessGame
import CurrencyRouletteGame
import Score
from WOG.tal_py_project.MainScores import run_score_service


name = input("Please enter your name: ")
difficulty = input("Please choose game difficulty from 1 to 5: ")
while not difficulty.isdigit():
    difficulty = input("You didn't enter a valid number, please try again ")
difficulty = int(difficulty)
while difficulty < 1 or difficulty > 5:
    difficulty = int(input("Invalid number, please try again "))


def welcome(user_name):
    print("\nHello", user_name, "and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    global difficulty
    select_game = input("Please choose a game to play:\n"
                        "1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to guess it back.\n"
                        "2. Guess Game - guess a number and see if you chose like the computer does.\n"
                        "3. Currency Roulette - try to guess the value of a random amount of USD in ILS.\n"
                        "What it will be: 1 / 2 / 3 ? ")
    while not select_game.isdigit():
        select_game = input("You didn't enter a valid number, please try again ")
    select_game = int(select_game)

    while select_game < 1 or select_game > 3:
        select_game = int(input("Invalid number, please try again "))
    if select_game == 1:
        print("You choose to play the Memory Game in difficulty number :", difficulty)
        MemoryGame.play_memory(difficulty)
    if select_game == 2:
        print("You choose to play the Guess Game in difficulty number :", difficulty)
        GuessGame.play_guess_game(difficulty)
    if select_game == 3:
        print("You choose to play the Currency Roulette in difficulty number :", difficulty)
        CurrencyRouletteGame.play_roulette(difficulty)


def update_user_score(difficulty_score):
    return Score.add_score(difficulty_score)


def play_game():
    global difficulty
    welcome(name)
    load_game()
    update_user_score(difficulty)
    run_score_service()



