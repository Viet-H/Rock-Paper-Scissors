import random

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors \n")
    user = user.lower()

    if user not in ['r', 'p', 's']:
        return "Invalid choice. Please select 'r', 'p', or 's'."

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "You and the computer have both chosen {}. It is a tie.".format(computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)

    return "You have chosen {} and the computer has chosen {}. You lost :(".format(user, computer)

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

if __name__ == '__main__':
    print(play())

    
    
