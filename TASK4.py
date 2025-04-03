import random

# Game choices
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

while True:
    print("\nRock, Paper, Scissors Game")
    print("Choose: rock, paper, or scissors")
    
    user_choice = input("Enter your choice: ").strip().lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    
    # Computer's random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    # Display score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Final Score:")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break
