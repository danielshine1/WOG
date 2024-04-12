import random
import requests
from Live import load_game, welcome


def get_guess_from_user():
    while True:
        try:
            user_guess = float(input("Enter your guess for the value in ILS: "))
            return user_guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


class CurrencyGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_value = None

    def get_money_interval(self):
        # Call the free currency API to get the current exchange rate from USD to ILS
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        exchange_rate = response.json()['rates']['ILS']

        # Generate an interval based on the difficulty
        total_value_of_money = random.randint(1, 100)
        lower_bound = total_value_of_money - (5 - self.difficulty)
        upper_bound = total_value_of_money + (5 - self.difficulty)

        return exchange_rate, (lower_bound, upper_bound)

    def play(self):
        exchange_rate, interval = self.get_money_interval()
        self.secret_value = random.randint(1, 100)

        print(f"Current exchange rate: 1 USD = {exchange_rate} ILS")
        print(f"Generated value in USD: {self.secret_value}")

        user_guess = get_guess_from_user()

        if interval[0] <= user_guess <= interval[1]:
            print("Congratulations! Your guess is within the correct interval.")
            return True
        else:
            print(f"Sorry, the correct interval was ({interval[0]}, {interval[1]}).")
            return False


# Main part of the code
user_choice, difficulty = load_game()

# Create an instance of CurrencyGame
currency_game = CurrencyGame(difficulty)

# Call the play method to start the game
result = currency_game.play()

if result:
    print("You guessed the correct interval.")
else:
    print("Better luck next time.")
