import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

POINTS_OF_WINNING = 5  # Assuming POINTS_OF_WINNING = (DIFFICULTY X 3) + 5


def add_score(difficulty):
    try:
        # Try to read the current score from the scores file
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
    except (FileNotFoundError, ValueError):
        # If the file doesn't exist or is empty, create a new one with the default score (0)
        current_score = 0

    # Calculate the points for winning based on the given difficulty
    points_for_winning = (difficulty * 3) + POINTS_OF_WINNING

    # Add the points to the current score
    new_score = current_score + points_for_winning

    # Save the new score to the scores file
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
        return new_score
    except IOError:
        return BAD_RETURN_CODE


def core_server():
    try:
        # Try to read the current score from the scores file
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
        return current_score
    except (FileNotFoundError, ValueError):
        # If the file doesn't exist or is empty, return a default score (0)
        return 66
    except IOError:
        return BAD_RETURN_CODE


def add_new_Score(diff, param):
    return None