def welcome(name):
    text = f"Hello {name}, and welcome to the World of Games (WoG).\n Here you can find many cool games to play."
    return f"{text}"


def load_game1():
    text = "Please choose a game to play:"
    text1 = "1. Guess Game - guess a number and see if you chose like the computer"
    text2 = "2. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
    text3 = "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"

    return f"{text}\n{text1}\n{text2}\n{text3}\n"


name = input("Please enter your name here: ")
welcome_message = welcome(name)
print(welcome_message)
select_message = load_game1()
print(select_message)


class NegativeNumberException(Exception):
    pass


class NumberValueError(Exception):
    pass


def load_game():
    user_choice = None
    difficulty_level = None

    # choose which game
    while True:
        try:
            user_choice = int(input("Which game would you like to play? Please enter the game number here: "))
            if user_choice < 0:
              raise NegativeNumberException
            elif user_choice < 1 or user_choice > 3 :
              raise NumberValueError

        except  ValueError:
            print(f"Value is not valid. Please enter a valid number between 1 - 3.")
        except NegativeNumberException as e:
            print(f"The number you chose: ({user_choice}) is not valid. Negative numbers are not allowed.")
        except NumberValueError as e:
            print(f"The number you chose: ({user_choice}) is not valid. Please enter a valid number between 1 - 3.")
        else:
            print(f"Game {user_choice} is a great choise!")
            break

    ### choose difficulty
    while True:
        try:
            difficulty_level = int(input("Please choose a difficulty level from 1 to 5: "))
            if difficulty_level < 0:
                raise NegativeNumberException
            elif difficulty_level < 1 or difficulty_level > 5:
                raise NumberValueError

        except  ValueError:
            print(f"Value is not valid. Please enter a valid number between 1 - 5.")
        except NegativeNumberException as e:
            print(f"The number you chose: ({difficulty_level}) is not valid. Negative numbers are not allowed.")
        except NumberValueError as e:
            print(f"The number you chose: ({difficulty_level}) is not valid. Please enter a valid number between 1 - 5.")
        else:
            print(f"Starting the game, have fun!")
            return user_choice, difficulty_level
