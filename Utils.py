import os

# 1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = "Scores.txt"

# 2. BAD_RETURN_CODE - A number representing a bad return code for a function.
BAD_RETURN_CODE = -1

# 3. Screen_cleaner - A function to clear the screen
def screen_cleaner():
    if os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:  # for Linux and Mac
        _ = os.system('clear')

# Additional utility functions can be added to this file as needed.
