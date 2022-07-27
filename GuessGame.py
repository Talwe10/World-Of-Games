import random
import Score


# 1. generate_number
def generate_number(difficulty_range):
    secret_number = random.randint(1, difficulty_range)  # a random number between 1 to difficulty_range.
    # print("the secret_number is: ", secret_number)  # checking point
    return secret_number


# 2. get_guess_from_user
def get_guess_from_user(difficulty_range):
    user_guess = input(f'\nPlease enter a number between 1 to {difficulty_range}: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        while user_guess < 1 or user_guess > difficulty_range:
            user_guess = int(input("Invalid number, please try again "))
        # print ("You choose the number: ", user_guess)  # checking point
        return user_guess
    else:
        while not user_guess.isdigit():
            user_guess = input("one more try, please enter a number: ")
            if user_guess.isdigit():
                user_guess = int(user_guess)
                while user_guess < 1 or user_guess > difficulty_range:
                    user_guess = int(input("Invalid number, please try again "))
                # print ("You choose the number: ", user_guess)  # checking point
                return user_guess
            else:
                exit()


def compare_numbers(secret_n, user_n,difficulty):
    counter = 1  # using counter for the user answers.
    while secret_n != user_n:  # While the two numbers are NOT equal do this:
        user_n = int(input("no luck, please try again: "))  # give the user another try.
        if secret_n == user_n:  # Before we are down the count we compare it again, because if the count==0 we will not know.
            return "You guess the right number!"
        if counter == 0:  # all the tries are done.
            return "You are out of luck today"
        counter -= 1  # count down the counter.

    if secret_n == user_n:
        update_user_score(difficulty)
        return "You guess the right number!"


# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play_guess_game(difficulty):
    print("Hello and welcome to the GuessGame!!! ")
    difficulty_range = difficulty * 3  # to make it more difficult for the user
    secret_n = generate_number(difficulty_range)
    #   print("checking point: ", secret_n)  # checking point
    user_n = get_guess_from_user(difficulty_range)
    #   print(user_n)  # checking point
    print(compare_numbers(secret_n, user_n,difficulty))


def update_user_score(difficulty):
    return Score.add_score(difficulty)
