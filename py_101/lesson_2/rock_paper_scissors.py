import random

VALID_CHOICES = ['rock', 'paper', 'scissors']
VALID_SHORT_CHOICES = ['r', 'p', 's']
VALID_SHORT_MAP = {'r':'rock', 'p':'paper', 's':'scissors'}

def display_winner():
    if player_wins == 3:
        prompt("You win!")
    else:
        prompt("You lose!")

def increment_winner(player_move, comp_move, num_player_wins, num_comp_wins):
    if ((player_move == 'rock' and comp_move == 'scissors') or
        (player_move == 'paper' and comp_move == 'rock') or
        (player_move == 'scissors' and comp_move == 'paper')):
        num_player_wins += 1
    elif ((comp_move == 'rock' and player_move == 'scissors') or
        (comp_move == 'paper' and player_move == 'rock') or
        (comp_move == 'scissors' and player_move == 'paper')):
        num_comp_wins += 1

    return (num_player_wins, num_comp_wins)

def prompt(message):
    print(f"==> {message}")

answer = 'y'

while answer[0] == 'y':

    player_wins = 0
    computer_wins = 0

    while player_wins < 3 and computer_wins < 3:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input()

        if choice in VALID_SHORT_CHOICES:
            choice = VALID_SHORT_MAP[choice]

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {choice}, computer chose {computer_choice}")

        player_wins, computer_wins = increment_winner(choice, computer_choice, player_wins, computer_wins)

        prompt(f"Your wins: {player_wins}, computer wins: {computer_wins}")

    display_winner()

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("That's not a valid choice")