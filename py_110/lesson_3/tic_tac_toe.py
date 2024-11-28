import random
import pdb

board_dict = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

def reset_board():
    board_dict[0] = " "
    board_dict[1] = " "
    board_dict[2] = " "
    board_dict[3] = " "
    board_dict[4] = " "
    board_dict[5] = " "
    board_dict[6] = " "
    board_dict[7] = " "
    board_dict[8] = " "

def display_board():
    print("+++++++++")
    board_display = [f"{board_dict[0]} | {board_dict[1]} | {board_dict[2]}",
                 "---------",
                 f"{board_dict[3]} | {board_dict[4]} | {board_dict[5]}",
                 "---------",
                 f"{board_dict[6]} | {board_dict[7]} | {board_dict[8]}"]
    
    for row in board_display:
        print(row)

def prompt_user_choice():
    if " " not in board_dict.values():
        return

    choice = int(input("Select a square (0-8): "))
    while board_dict[choice] != " ":
        choice = int(input("Select a different square (0-8): "))

    board_dict[choice] = 'x'

def determine_tie():
    if " " not in board_dict.values() and not winner():
        return True
    
    return False

def computer_choice():
    if " " not in board_dict.values():
        return

    choice = random.randint(0,8)

    while board_dict[choice] != " ":
        choice = random.randint(0,8)

    board_dict[choice] = 'o'

def winner():
    if board_dict[0] == board_dict[1] == board_dict[2]:
        if board_dict[0] == 'x':
            print('You win!')
            return True
        elif board_dict[0] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[3] == board_dict[4] == board_dict[5]:
        if board_dict[3] == 'x':
            print('You win!')
            return True
        elif board_dict[3] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[6] == board_dict[7] == board_dict[8]:
        if board_dict[6] == 'x':
            print('You win!')
            return True
        elif board_dict[6] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[0] == board_dict[3] == board_dict[6]:
        if board_dict[0] == 'x':
            print('You win!')
            return True
        elif board_dict[0] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[1] == board_dict[4] == board_dict[7]:
        if board_dict[1] == 'x':
            print('You win!')
            return True
        elif board_dict[1] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[2] == board_dict[5] == board_dict[8]:
        if board_dict[2] == 'x':
            print('You win!')
            return True
        elif board_dict[2] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[0] == board_dict[4] == board_dict[8]:
        if board_dict[0] == 'x':
            print('You win!')
            return True
        elif board_dict[0] == 'o':
            print('Computer wins!')
            return True
    elif board_dict[2] == board_dict[4] == board_dict[6]:
        if board_dict[2] == 'x':
            print('You win!')
            return True
        elif board_dict[2] == 'o':
            print('Computer wins!')
            return True
        
    return False

def prompt_play_again():
    choice = input("Play again? (y/n)")

    while choice[0].lower() not in 'yn':
        choice = input("Invalid input. Play again? (y/n)")

    if choice[0] == 'y':
        return True
    
    return False

while True:
    display_board()
    for _ in range(9):
        prompt_user_choice()

        if winner():
            display_board()
            break

        computer_choice()
        display_board()
        
        if winner():
            break

    if determine_tie():
        print("It's a tie.")
    
    if not prompt_play_again():
        break

    reset_board()