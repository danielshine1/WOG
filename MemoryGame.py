import random
import time
from Live import load_game, welcome

class MemoryGame:
    def __init__(self):
        self.sequence = None

    def generate_sequence(self, difficulty, display_duration=0.7):
        self.sequence = [random.randint(1, 101) for _ in range(difficulty)]
        print(f"Generated sequence: {self.sequence}")

        # Display the sequence for a specified duration
        time.sleep(display_duration)

        # Clear the screen or use other methods to hide the sequence (platform-dependent)
        print("\033[H\033[J")

        return self.sequence

    def get_list_from_user(self, difficulty):
        while True:
            try:
                user_list = [int(input(f"Enter number {i + 1} out of {difficulty}: ")) for i in range(difficulty)]
                return user_list
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self, difficulty):
        generated_sequence = self.generate_sequence(difficulty)
        user_sequence = self.get_list_from_user(difficulty)
        result = self.is_list_equal(generated_sequence, user_sequence)
        return result

# Main part of the code
user_choice, difficulty_level = load_game()

# Create an instance of MemoryGame
memory_game = MemoryGame()

# Call the play method to start the game
result = memory_game.play(difficulty_level)

if result:
    print("Congratulations! You guessed the correct sequence.")
else:
    print(f"Sorry, the correct sequence was {memory_game.sequence}. Better luck next time.")
