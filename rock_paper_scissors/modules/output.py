def print_menu():
    print("Please choose from the following options:")
    print("1: Play Game")
    print("2: Help")
    print("3: Quit")

def help_menu():
    print("Type the number corresponding to what you want to do. For example, if you want to play the game, just type 2 and you will be taken to the game.")
    print_menu()

def print_current_score(player_score, computer_score):
    print(f"Current score is: PLAYER = {player_score}  COMPUTER == {computer_score} ")

