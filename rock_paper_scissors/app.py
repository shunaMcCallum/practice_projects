from modules.input import *
from modules.output import *

print("Welcome to ROCK, PAPER, SCISSORS!!!")
print_menu()

while (True):
    choice = menu_choice()
    if choice == "1":
        print("Let's play...best out of 5 wins!!!")
        play_game()
    elif choice == "2":
        help_menu()
    elif choice == "3":
        quit()
    else:
        print("Invalid entry. Please choose 1, 2 or 3.")

