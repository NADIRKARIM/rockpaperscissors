import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
