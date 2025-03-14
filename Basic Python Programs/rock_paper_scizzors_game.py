# Program to create a Rock-Paper-Scissors Game...

import random

item_list = ['Rock', 'Paper', 'Scizzor']

def play_game():
    user = input("Enter your move: ")
    computer = random.choice(item_list)

    print(f"You chose {user}")
    print(f"Computer chose {computer}\n")

    if (user == computer):
        print(f"Both players selected {user}. It's a tie!")
    elif (user == 'Rock'):
        if computer == 'Paper':
            print(f"Paper covers Rock. Computer wins!")
        else:
            print(f"Rock smashes Scizzor. You win!")
    elif(user == 'Paper'):
        if computer == 'Rock':
            print(f"Paper covers Rock. You win!")
        else:
            print(f"Scizzor cuts Paper. Computer wins!")
    elif(user == 'Scizzor'):
        if computer == 'Rock':
            print(f"Rock smashes Scizzor. Computer wins!")
        else:
            print(f"Scizzor cuts Paper. You win!")
    else:
        print("Invalid input")

#Game starts from here
print("Welcome to Rock-Paper-Scizzors Game!")    
play_game()

while(True):
    print("\nDo you want to play again? (yes/no): ")
    play_again = input().lower()
    if play_again == "yes":
        print("Let's play again!")
        play_game()
    else:
        print("Thanks for playing!")
        exit()
