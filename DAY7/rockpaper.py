# Rock, Paper, Scissors

import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Let's play Rock, Paper, Scissors!")
print("Type 'quit' at any time to stop.\n")

while True:
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice == "quit":
        print("Thanks for playing!")
        break

    if player_choice not in options:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")