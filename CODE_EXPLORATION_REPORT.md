# Code Exploration Report

## 1. Introduction and Scope

This repository contains a **Coding Language Learning Game**. It's a simple interactive terminal game made with python. It's designed to help users learn programming by predicting the output of Python code snippets. The game has difficulty levels, scoring, and a lives system to make learning more engaging.

## 2. Overview of the Codebase

### Repository Information
- **Original Repository**: https://github.com/avinashkranjan/Amazing-Python-Scripts/tree/main/Coding%20Language%20Learning%20Game
- **Our Repository**: https://github.com/felixleopold/adc_coding_language_learning_game.git

### Directory Structure

The codebase follows a very simple structure:
```
.
├── main.py              # Main game file
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## 3. Functionality Exploration

### Flow

1. **Initialization**: Game starts with `main()` function
2. **Difficulty Selection**: User selects difficulty level (easy, medium, hard)
3. **Game Loop**:
   - `get_random_code_snippet(difficulty)` - Selects random snippet from difficulty pool
   - Displays code snippet to user
   - Starts timer and waits for user input
   - Validates answer against expected output
   - Updates score and lives based on correctness and timing
   - Prompts for continuation
   - Repeats the game loop until the user stops

## 4. Code Execution and Analysis

### Execution Test

The code executes successfully without errors. Test run results:

```
Welcome to the Coding Language Learning Game!
Select difficulty (easy, medium, hard): easy

Code Snippet:
[coding problem]
Your Guess: [user input]
Correct! You earned 10 points.
Lives remaining: 3
Your current score: 10
Do you want to play again? (y/n): [user input]
```

## 5. Code quality

The readability of the code is very good. Every function is defined clearly with whitespaces between them. The complexity of the code is simple, even a beginning coder can understand it. It just includes function definitions, a while loop, if statements and dictionaries. So the strengthness of this code lays in the fact that it is very clear and easy to understand. However, in the dictionaries, the code is very wide, as it cannot be fit in one screen, not following the PEP8 principles. Once you chose a difficulty (either easy, medium or hard), you cannot change it anymore. Additionally, there are only 2 questions for each difficulty, which are picked randomly. Therefore, the same question can get repeated several times, especially if you can't change the difficulty.

## 6. Possible Extensions

**Improvements**

The content inside of the dictionaries de_snippets and difficulty_levels is very wide, so both should contain more linebreaks for better readability.

**Extensions**

A first logical extension of the program would be to be able to change the difficulty of the follow-up question after finishing a question, so the user can alternate between difficulties during one iteration of the program.
A second logical extension would be to prevent the same question from a particular difficulty to be asked twice during one iteration of the program, because in this way the point system does not give a not realistic enough representation for the player's knowledge.
A third logical extension for error prevention would be to add a try statement for the difficulty input, because now when inputting an invalid difficulty a Keyerror arises and the program terminates.