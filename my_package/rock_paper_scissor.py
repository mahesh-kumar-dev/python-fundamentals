# rock_paper_scissors.py - Main game using module
import game_utils

print("Rock Paper Scissor Game>>>")
options = ["rock","paper","scissors"]

player_wins = 0
computer_wins = 0


while True:
    player = game_utils.get_player_choice("Your move: ",options)
    computer = game_utils.roll_dice(3)-1
    computer = options[computer]

    print(f"Computer choose: {computer}")

    winner = game_utils.determine_winner(player,computer)

    if winner == "player":
        print("You win!")
        player_wins +=1
    elif winner == "computer":
        print("Computer win!")
        computer_wins +=1
    else:
        print("Tie")


    print(f"Your Score: {player_wins}")
    print(f"Computer Score: {computer_wins}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break 

print("Thanks for playing 😊")