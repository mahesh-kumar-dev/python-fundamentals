# my_package/game_utils.py 
# Game Utitlities Module

import random

def roll_dice(sides=6):
    """Roll a Dice"""
    return random.randint(1,sides)

def get_player_choice(prompt, option):
    """Get Valid choice from Player"""
    while True:
        choice = input(prompt).lower()
        if choice in option:
            return choice
        print(f"Choice from:  {', '.join(option)}")


def determine_winner(player, computer):
    """Determine winner in rock-paper-scissors"""
    if player == computer:
        return "tie"
    if  (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
            return "player"
    return "computer"

if __name__ == "__main___":
    print("Testing Game utils.....")
    print(f"Roll a dice: {roll_dice()}")

