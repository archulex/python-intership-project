import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print(" Welcome to Rock Paper Scissors Game!")

while True:
    # User Input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print(" Invalid choice! Please try again.")
        continue

    # Computer Choice
    computer_choice = random.choice(choices)

    print(f" You chose: {user_choice}")
    print(f" Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print(" It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print(" You Win!")
        user_score += 1
    else:
        print(" You Lose!")
        computer_score += 1

    # Display Score
    print(f" Score -> You: {user_score} | Computer: {computer_score}")

    # Play Again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n Thanks for playing!")
        break