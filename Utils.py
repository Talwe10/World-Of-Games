import os

# 1. SCORES_FILE_NAME - A string representing a file name. By default, “Scores.txt”
SCORES_FILE_NAME = os.path.dirname(__file__)
rel_path = "Scores.txt"
print(SCORES_FILE_NAME.read())


# 2. BAD_RETURN_CODE - A number representing a bad return code for a function.
BAD_RETURN_CODE = int(404)


# 3. Screen_cleaner - A function to clear the screen (useful when playing memory game or before a new game starts).
def _screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
