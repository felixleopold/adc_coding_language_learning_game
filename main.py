import random # library used to make a random decision
import time # library to measure time taken for an exercise

# Dictionary containing Python code snippets and their expected outputs
code_snippets = {
    "print('Hello, world!')": "Hello, world!",
    "print(2 + 3)": "5",
    "print('Python' + ' is ' + 'fun')": "Python is fun",
    "numbers = [1, 2, 3, 4, 5]\nprint(numbers)": "[1, 2, 3, 4, 5]",
    "num1 = 10\nnum2 = 5\nprint(num1 * num2)": "50",
    "def fibonacci(n):\n    if n <= 0:\n        return 'Invalid input'\n    elif n == 1:\n        return 0\n    elif n == 2:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\nprint(fibonacci(6))": "5",
}

# Difficulty levels with corresponding sets of code snippets
difficulty_levels = {
    "easy": ["print('Hello, world!')", "print(2 + 3)"],
    "medium": ["print('Python' + ' is ' + 'fun')", "numbers = [1, 2, 3, 4, 5]\nprint(numbers)"],
    "hard": ["num1 = 10\nnum2 = 5\nprint(num1 * num2)", "def fibonacci(n):\n    if n <= 0:\n        return 'Invalid input'\n    elif n == 1:\n        return 0\n    elif n == 2:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\nprint(fibonacci(6))"]
}


def get_random_code_snippet(difficulty):
    """Return a random Python code snippet based on the selected difficulty."""
    return random.choice(difficulty_levels[difficulty])

# Main function where all the other functions are called in
def main():
    print("Welcome to the Coding Language Learning Game!")
    difficulty = input("Select difficulty (easy, medium, hard): ").lower() # User can choose their difficulty

    # Initialize game settings
    lives = 3
    score = 0
    time_limit = 45  # Time limit in seconds for each code snippet

    #While loop during the game
    while True:
        code_snippet = get_random_code_snippet(difficulty) # function call
        expected_output = code_snippets[code_snippet] # Corresponding answer (the right answer)

        print("\nCode Snippet:")
        print(code_snippet)

        start_time = time.time() # Time limit
        user_guess = input("Your Guess: ") # Guess of the user

        elapsed_time = time.time() - start_time 

        # if statement to first check if time is up
        if elapsed_time > time_limit:
            print(f"Time's up! The correct output was: {expected_output}")
            lives -= 1
        # When answer is right (+10 points)
        elif user_guess == expected_output:
            print("Correct! You earned 10 points.")
            score += 10
        # Else a wrong answer
        else:
            print(f"Oops! The correct output was: {expected_output}")
            lives -= 1
        # The user's game finishes when they run out of lives
        if lives == 0:
            print("Game Over! You've run out of lives.")
            break

        print(f"Lives remaining: {lives}")
        print(f"Your current score: {score}")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

    print(f"Your final score: {score}")

# Call of main function (when user runs this python file)
if __name__ == "__main__":
    main()
