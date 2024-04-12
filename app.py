from flask import Flask, render_template
from Score import core_server
from GuessGame import GenerateNumber
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyGame

app = Flask(__name__)


class NegativeNumberException(Exception):
    pass


class NumberValueError(Exception):
    pass


def play_game():
    global difficulty_level, user_choice
    score = 0

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

            # Call the corresponding game's play function based on user's choice
            if user_choice == 1:
                guess_game = GenerateNumber()
                score += guess_game.play()
            elif user_choice == 2:
                memory_game = MemoryGame()
                score += memory_game.play()
            elif user_choice == 3:
                difficulty_level = int(input("Please choose a difficulty level from 1 to 5: "))
                if difficulty_level < 1 or difficulty_level > 5:
                    print("Invalid difficulty level. Exiting...")
                    return
                currency_game = CurrencyGame(difficulty_level)
                score += currency_game.play()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Your final score is: {score}")
    return score


@app.route('/')
def index():
    score = play_game()
    return render_template('index_scores.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
