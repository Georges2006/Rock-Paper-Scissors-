import random
import math
# r:Rock , p:Paper , s:scissors
def play():
    player = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissors").lower()
    computer = random.choice(['r' ,'p' , 's'])
    
    if player == computer:
        return ( 0 , player , computer)
    
    if win(player , computer):
        return ( 1, player , computer )
    
    return( -1 , player , computer )
    
    
def win(player , computer):
    #return True if player beat opponent and False Otherwise
    #condition for win r > s ; p > r ; s > p
    if( player == 'r' and computer == 's' or player =='p' and computer == 'r' or player == 's' and computer =='p'):
        return True 
    
    return False

def best_partie(n):
    player_win = 0
    computer_win = 0
    necessary_part = math.ceil(n/2)
    while player_win < necessary_part and computer_win < necessary_part:
        result, player, computer = play()

        if result == 0 :
            print(f" It is a Tie . You and Computer have both choice {computer}")
        elif result == 1 :
            player_win += 1
            print(f"You choice {player} and computer {computer} . win :)")
        else:
            computer_win += 1
            print(f" You choice {player} and computer {computer} , Loss :(")
    if player_win > computer_win :
        print(" Winner")
    else:
        print("Loss")

            
    

if __name__ == '__main__':
    print(best_partie(5))
    
        
        