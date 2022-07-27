import Score
import random
import sys
import time

# 1. generate_sequence - Will generate a list of random numbers between 1 and 101. The list length will be difficulty.
top_range = 101
time_to_clear_the_screen = 0.7


def generate_sequence(difficulty):
    secret_sequence = [random.randint(1, top_range) for i in range(difficulty * 2)]
    print(secret_sequence, end="")
    sys.stdout.flush()
    time.sleep(time_to_clear_the_screen)  # 0.7 is the time until the line will be clear.
    print("\rI Hope you got it")
    return secret_sequence


# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
def get_list_from_user(difficulty):
    user_list = (
        input(
            f'Please enter a list of numbers between 1-101, the list will be at length of {difficulty * 2} numbers, and separated by space:  '))
    user_list = list(int(num) for num in user_list.strip().split(" "))[:difficulty * 2]
    # each number of the list we got we need to separate it and split it and convert it to list
    return user_list


# 3. is_list_equal - A function to compare two lists if they are equal. The function will return True / False.
def compare_lists(L1, L2, difficulty):
    L1.sort()  # we need to sort the number is the list for the comparison.
    L2.sort()
    counter = 2  # using counter for the user answers.
    while L1 != L2:  # While the two lists are NOT equal do this:
        L2 = input("no luck, please try again: ")
        L2 = sorted(list(int(num) for num in L2.strip().split(" ")))[:difficulty * 2]  # give the user another try.
        if L1 == L2:  # Before we are down the count we compare it again, because if the count==0 we will not know.
            return "You are correct, the lists are equals."
        if counter == 0:  # The trials are over.
            return "You are out of luck today."
        counter -= 1  # count down the counter.
    if L1 == L2:
        return "You are correct, the lists are equals."


# 4. play - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play_memory(difficulty):
    ready_to_play = input(
        f'\n\nHello and welcome to the MemoryGame!!! \nTry to remember the following numbers, click on the Enter key to start ')
    L1 = generate_sequence(difficulty)
    print(L1, "---The secret_sequence---")  # checking point
    L2 = get_list_from_user(difficulty)
    #   print(type(L2))  # checking point
    print(compare_lists(L1, L2, difficulty))


def update_user_score(difficulty):
    return Score.add_score(difficulty)
