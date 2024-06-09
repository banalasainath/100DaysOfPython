import random
import os
logo = """
  _______               ___.                    ________                             
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >
        \/            \/    \/     \/                \/            \/     \/     \/ 
"""        
def number_comparision(guess,user_guess):
    if(user_guess>guess):
        print("Too High")
    elif(user_guess<guess):
        print("Too Low") 
    return            

def check_difficulty(difficulty):
    if(difficulty.lower() == "easy"):
        return 10
    elif(difficulty.lower() == "hard"):
        return 5

while(True):
    print(logo)
    print("Welcome to the number guessing game")
    print("I am thinking of number between 1 and 100")
    guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty level Either \"easy\" or \"hard\": ")
    attempts = check_difficulty(difficulty)
    for i in range(1,attempts+1):
        print(f"You have {attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if(user_guess==guess):
            print(f"you got the perfect match, i.e., {guess}")
            break
        else:
            number_comparision(guess, user_guess)    
        attempts-=1
    else:
        print(f"You loose the game, My guess is: {guess}")
    replay=input("Do you want to play once again? yes or no: ")
    if(replay.lower()=="no"):
        break 
    os.system('cls')




