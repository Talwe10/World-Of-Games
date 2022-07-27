# World_Of_Games (WOG)


In this project the user will be able to play 3 games.
The code was written in **Python**, using **Flask** and **HTML** for web creation, Version Control was managed by **GIT**.


# The Games:

**1. Memory Game** - a sequence of numbers will appear for 0.7 seconds and you have to guess it back.

The purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds and then prompt them from the user for the numbers that he remember. If he was right with all the numbers the user will win otherwise he will lose.

**2. Guess Game** - guess a number and see if you chose like the computer.

The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called ​difficulty.​ The game will get a number input from the user and update if is same the number or not.

**3. Currency Roulette** - try and guess the value of a random amount of USD in ILS.

In this game the user should guess the value of the generated number from USD to ILS.
Depending on the user’s difficulty his answer will be correct if the guessed value is between the interval surrounding the correct answer



# Other files in this project:

**Live.py** - This program is for getting inputs for WorldOfGames, includes name, game, difficulty.

**MainGame.py** - The purpose of this file is to call the functions from Live.py and run everything.

**Utils.py** - This file contains variables and functions for general project use.

	**SCORES_FILE_NAME** - A string representing “Scores.txt” file name. Used in the Score.py and MainScores.py files.
	**BAD_RETURN_CODE** - A value that represents an error in case of a function error, Used in MainScores.py file.
	**screen_cleaner** - Function to clear the screen when starting a new game.

**Score.py** - This file is responsible for keeping the user's score in case of a text file win.
The score is determined by a formula\
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5\
If there is already a file with a score, the new score will be added to the existing one.\
If no score file exists, a new file will be created.


**MainScores.py** - This file is responsible for reading the score file and publishing it to HTTP using HTML, this process will be done using Python FLASK library.\
In the event of an error in reading the score file, the error code we defined will be displayed.


## Execution
The Python version, used for this project is 3.10.
All required dependencies are in the file **requirements.txt**.
Run **MainGame.py**, you will be prompt to enter Name, choose Game, and select Difficulty.
