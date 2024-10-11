import random
from state_capitals import states

class Play:
    def __init__(self, name):
        self.name = name
        self.result = {"correct": 0, "incorrect": 0, "answered": 0}

    def __str__(self):
        return f"Result (correct: {self.result['correct']}, incorrect: {self.result['incorrect']}, answered: {self.result['answered']})"

    def welcome_message(self):
        print("Welcome to play", self.name)

    @staticmethod
    def get_unique_random_number(used_numbers, start, end):
        """Generate a unique random number within a range that hasn't been used yet."""
        available_numbers = set(range(start, end + 1)) - used_numbers
        if not available_numbers:
            raise ValueError("No more unique numbers available in the given range.")

        number = random.choice(list(available_numbers))
        used_numbers.add(number)
        return number

    def play(self):
        used_numbers = set()
        self.welcome_message()

        play_game = input("Would you like to play? 'y' for yes | 'n' for no: ").lower()
        if play_game != "y":
            print("Thanks for playing!")
            return

        while play_game == "y":
            for i in range(len(states)):
                unique_number = self.get_unique_random_number(used_numbers, 0, len(states) - 1)
                key = states[unique_number]
                key_name = key["name"]
                value_name = key["capital"].lower()

                capital = input(f"What is the capital of {key_name}: ").strip().lower()

                if capital == value_name:
                    self.result["correct"] += 1
                    print("Correct!")
                else:
                    self.result["incorrect"] += 1
                    print("Incorrect answer")
                    # print(f"Incorrect! The correct answer is {value_name}.")

                self.result["answered"] += 1
                print(self)

            play_game = input("Play again? press 'y': ").lower()
        print("Finished game for", self.name, "\n", self)

