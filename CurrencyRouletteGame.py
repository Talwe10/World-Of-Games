import random
from currency_converter import CurrencyConverter
import Score


# 1. get_money_interval -Will get the current currency rate from USD to ILS and will generate an interval as follows:
#   a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
def get_money_interval(difficulty, random_num):
    c = CurrencyConverter()
    total = c.convert(random_num, 'USD', 'ILS')
    total_round = round(total)
    # print("checking point... ", total)  # checking point
    # print("checking point... ", total_round)  # checking point
    interval = range(round(total_round - (5 - difficulty)), round(total_round + (5 - difficulty)) + 1)
    # the range according to the difficulty, the (+1) in the end is beacuse in the range the last number is not count.
    return interval


# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of value to a given amount of USD
def get_guess_from_user():
    user_guess = input("Please enter a guess of value to a given amount of USD: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        return user_guess
    else:
        while not user_guess.isdigit():
            user_guess = input("one more try, please enter a number: ")
            if user_guess.isdigit():
                return user_guess
            else:
                exit()


# 3. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play_roulette(difficulty):
    random_num = random.randint(1, 100)
    print("\nThe number you need to convert from USD to ILS is: ", random_num)
    x = get_money_interval(difficulty, random_num)
    print(x, "checking point")  # checking point
    y = get_guess_from_user()
    #   print(y)  # checking point

    if y in x:
        print("Great guess, You Win!!!")
    else:
        counter = 2  # using counter for the user answers.
        while y not in x:
            y = int(input("no luck, please try again: "))  # give the user another try.
            counter -= 1  # count down the counter.
            if y in x:
                # update_user_score(difficulty)
                print("You Win!!!")
                break
            if counter == 0:  # all the tries are done.
                print("You are out of luck today")
                return difficulty == 0     # trying to send nothing (0) to points_of_winning = ((difficulty * 3) + 5)
                # break


def update_user_score(difficulty):
    return Score.add_score(difficulty)

