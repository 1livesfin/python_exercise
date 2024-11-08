import random

def play():
    user = input("Apa pilihanmu? 'b' for batu, 'k' for kertas, 'g' for gunting")
    computer = random.choise(['b', 'k', 'g'])

    if user == computer:
        return 'Seri'
    
    if is_win(user, computer):
        return 'Anda menang!'
    
    return 'Anda kalah!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True