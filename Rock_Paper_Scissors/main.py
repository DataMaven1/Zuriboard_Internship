#A Simple program to create the Rock-Paper-Scissors game in Python
#Rock-Paper-Scissors is a simple two-player game
#one player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player).

import random

game_over = False

while not game_over:
    possible_choices = ["R", "P", "S"]
    player_choice = input("Welcome, Enter your Choice:\n")
    computer_choice = random.choice(possible_choices)

    print(f"Player: {player_choice}, Computer: {computer_choice}\n")

    if player_choice not in possible_choices:
        print("Invalid input, Try again\n")
        continue


    if player_choice == computer_choice:
        print(f"Both player select {player_choice}, Its a tie\n")

    elif player_choice == "R":
        if computer_choice == "S":
            print("Rock smashes Scissors, You Won\n")
            print("Game over")
        else:
            print("Oh no!, You lose")
            continue
        break

    elif player_choice == "S":
        if computer_choice == "P":
            print("Scissors cut paper, You won\n")
            print("Game Over")
        else:
            print("oh no, You lose\n")
            continue
        break

    elif player_choice == "P":
        if computer_choice == "R":
            print("Paper cover rock, You won")
            print("Game over")
        else:
            print("You lose")
            continue
        break
