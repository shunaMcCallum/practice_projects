from random import randint
from modules.output import *


def menu_choice():
    choice = input("Please choose option 1, 2 or 3: ")
    return choice

def user_choice():
    choice = input("Please enter 'Rock', 'Paper', or 'Scissors': ")
    return choice

def random_number_generator():
    num = randint(1,3)
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    elif num == 3:
        return "Scissors"

def play_game():
    player_score = 0
    computer_score = 0
    while player_score and computer_score < 3:
        player_choice = user_choice()
        computer_choice = random_number_generator()
        if player_choice == "Rock":
            if computer_choice == "Rock":
                print("Computer chose Rock...")
                print("Draw!")
                print_current_score(player_score, computer_score)
            elif computer_choice == "Paper":
                print("Computer chose Paper...")
                print("Computer wins this round!")
                computer_score += 1
                print_current_score(player_score, computer_score)
            elif computer_choice == "Scissors":
                print("Computer chose Scissors...")
                print("You win this round!")
                player_score += 1
                print_current_score(player_score, computer_score)
        elif player_choice == "Paper":
            if computer_choice == "Rock":
                print("Computer chose Rock...")
                print("You win this round!")
                player_score += 1
                print_current_score(player_score, computer_score)
            elif computer_choice == "Paper":
                print("Computer chose Paper...")
                print("Draw!")
                print_current_score(player_score, computer_score)
            elif computer_choice == "Scissors":
                print("Computer chose Scissors...")
                print("Computer wins this round!")
                computer_score += 1
                print_current_score(player_score, computer_score)
        elif player_choice == "Scissors":
            if computer_choice == "Rock":
                print("Computer chose Rock...")
                print("Computer wins this round!")
                computer_score += 1
                print_current_score(player_score, computer_score)
            elif computer_choice == "Paper":
                print("Computer chose Paper...")
                print("You win this round!")
                player_score += 1
                print_current_score(player_score, computer_score)
            elif computer_choice == "Scissors":
                print("Computer chose Scissors...")
                print("Draw!")
                print_current_score(player_score, computer_score)
        else:
            print("Invalid choice. Please type either 'Rock', 'Paper' or 'Scissors'.")
    print_current_score(player_score, computer_score)
    play_again()

def play_again():
    play = input("Would you like to play again? Please enter 'y' for yes or 'n' for no: ")
    if play == "y":
       play_game()
    else:
       print_menu()

