import random

def get_winner(player, computer):
    if player == computer:
        return "tie"
    
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def main():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    rounds_to_win = 2
    
    print("=== ROCK PAPER SCISSORS ===")
    print(f"first to {rounds_to_win} wins")
    
    while player_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\nscore: you {player_score} - {computer_score} computer")
        
        player_choice = input("rock, paper, or scissors? ").lower()
        
        if player_choice not in choices:
            print("thats not a choice. try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        
        if winner == "player":
            print("you win this round!")
            player_score += 1
        elif winner == "computer":
            print("computer wins this round :(")
            computer_score += 1
        else:
            print("tie! no points.")
    
    print(f"\n=== GAME OVER ===")
    if player_score > computer_score:
        print("you won the match! nice.")
    else:
        print("computer won. try again.")

if __name__ == "__main__":
    main()
