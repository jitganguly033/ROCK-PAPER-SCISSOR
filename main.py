import random  # Importing the random module to use its functions

AI = random.choice([-1, 0, 1])  # Randomly chooses a value from [-1, 0, 1] for AI (rock, paper, or scissors)

youstr = input("Enter your choice: ")  # Takes input from the user (R, P, or S)

# Dictionary that maps the user's input (R, P, S) to corresponding numeric values (rock = 1, paper = 0, scissors = -1)
youDict = {"R": 1, "r": 1, "S": -1, "s": -1, "p": 0, "P": 0}

# Reverse dictionary that maps numeric values back to the choice names (rock, paper, or scissors)
reverseDict = {1: "ROCK", -1: "SCISSORS", 0: "PAPER"}

you = youDict[youstr]  # Converts user's input into corresponding numeric value

# Prints the choices made by both user and AI using the reverse dictionary
print(f"You chose {reverseDict[you]}\nAI chose {reverseDict[AI]}")

# If both AI and the user choose the same, it's a draw
if AI == you:
    print("It's a draw")

else:
    # Nested conditions to determine if the user wins or loses based on the game's rules
    if AI == -1 and you == 1:  # Rock beats scissors
        print("You win!")

    elif AI == -1 and you == 0:  # Paper beats scissors
        print("You lose!")

    elif AI == 1 and you == -1:  # Scissors lose to rock
        print("You lose!")

    elif AI == 1 and you == 0:  # Paper beats rock
        print("You win!")

    elif AI == 0 and you == -1:  # Scissors beat paper
        print("You win!")

    elif AI == 0 and you == 1:  # Rock loses to paper
        print("You lose!")

    # In case an invalid input is provided
    else:
        print("Please... Enter the letters according to this game (R, P, S)...")