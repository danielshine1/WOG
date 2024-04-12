
from GuessGame import GenerateNumber
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyGame


class NegativeNumberException(Exception):
    pass


class NumberValueError(Exception):
    pass


def load_game():
    # choose which game
    global difficulty_level, user_choice
    while True:
        try:
            user_choice = int(input("Which game would you like to play? Please enter the game number here: "))
            if user_choice < 0:
                raise NegativeNumberException
            elif user_choice < 1 or user_choice > 3:
                raise NumberValueError

        except ValueError:
            print("Value is not valid. Please enter a valid number between 1 - 3.")
        except NegativeNumberException as e:
            print(f"The number you chose: ({user_choice}) is not valid. Negative numbers are not allowed.")
        except NumberValueError as e:
            print(f"The number you chose: ({user_choice}) is not valid. Please enter a valid number between 1 - 3.")
        else:
            print(f"Game {user_choice} is a great choice!")
            break

    # choose difficulty
    while True:
        try:
            difficulty_level = int(input("Please choose a difficulty level from 1 to 5: "))
            if difficulty_level < 0:
                raise NegativeNumberException
            elif difficulty_level < 1 or difficulty_level > 5:
                raise NumberValueError

        except ValueError:
            print("Value is not valid. Please enter a valid number between 1 - 5.")
        except NegativeNumberException as e:
            print(f"The number you chose: ({difficulty_level}) is not valid. Negative numbers are not allowed.")
        except NumberValueError as e:
            print(
                f"The number you chose: ({difficulty_level}) is not valid. Please enter a valid number between 1 - 5.")
        else:
            print("Starting the game, have fun!")

        # Call the corresponding game's play function based on user's choice
        if user_choice == 1:
            guess_game = GenerateNumber()
            return guess_game.play()
        elif user_choice == 2:
            memory_game = MemoryGame()
            return memory_game.play()
        elif user_choice == 3:
            currency_game = CurrencyGame(difficulty_level)
            return currency_game.play()
