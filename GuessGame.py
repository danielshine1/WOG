import random
from Live import load_game, welcome


class GenerateNumber:
    def __init__(self):
        self.secret_number = None

    def generate_number(self, difficulty_level):
        self.secret_number = random.randint(1, difficulty_level)
        return self.secret_number

    def prompt_user_for_number(self, difficulty_level):
        while True:
            try:
                user_number = int(
                    input(f"Please guess my secret number: enter a number between 1 and {difficulty_level}: "))
                if 1 <= user_number <= difficulty_level:
                    return user_number
                else:
                    print(f"Number must be between 1 and {difficulty_level}. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, secret_number, user_guess):
        if secret_number == user_guess:
            return True  # User guessed the correct number
        else:
            return False  # User did not guess the correct number

    def play(self, difficulty_level):
        self.generate_number(difficulty_level)
        user_input_number = self.prompt_user_for_number(difficulty_level)
        result = self.compare_results(self.secret_number, user_input_number)
        return result


# Main part of the code
user_choice, difficulty_level = load_game()

# Create an instance of GenerateNumber
number_generator = GenerateNumber()

# Call the play method to start the game
result = number_generator.play(difficulty_level)

if result:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {number_generator.secret_number}. Better luck next time.")
