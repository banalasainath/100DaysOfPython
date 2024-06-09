import random
import os
# 11-Ace, 10-king,queen,jack  Ace is treated as 1 when the total goes beyond 21
# BlackJack = ace+10 value card

def clear_console():
    os.system('cls')

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    pick= random.choice(cards)
    return pick

def calculate_score(cards):
    if len(cards)==2 and sum(cards)==21:
        return 0
    if(sum(cards)>21 and 11 in cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare():
    if (calculate_score(user_cards)>21 or calculate_score(computer_cards)==0):
        print(f"Your cards = {user_cards}\t computer_cards = {computer_cards}\n You Lost")
        return
    elif(calculate_score(user_cards)==0 or calculate_score(computer_cards)>21):
        print(f"your cards = {user_cards}\t computer_cards = {computer_cards}\n You Won")
        return
    elif calculate_score(computer_cards)==calculate_score(user_cards):
        print("TIE")
        return
    elif calculate_score(user_cards)>calculate_score(computer_cards):
        print("You have won")
        return
    else:
        print("You Have Lost")                      

while(True):
    user_wish = input("If you want to play Black Jack game enter \"yes\" else enter \"no\": ")
    clear_console() 
    if (user_wish=="yes"):
        user_cards = []
        computer_cards = []
        for i in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        if(calculate_score(computer_cards)==0 or calculate_score(user_cards)==0):
            compare()
            print(f"Your cards={user_cards} \t computer cards = {computer_cards}")
            break
        print(f"Your Cards = {user_cards}\t computer cards = {[computer_cards[0]]}")
        while(True):
            check = input("If you want hit another card enter \"yes\" else print \"no\":").lower()
            if check=="yes":
                user_cards.append(deal_card())
                if (calculate_score(user_cards)>21):
                    break
                elif(calculate_score(user_cards)==0):
                    break    
                else:
                    print(f"Your Cards = {user_cards}")   
            else:
                break
        while(calculate_score(computer_cards)<17):
            computer_cards.append(deal_card())
            if (calculate_score(computer_cards))>21:
                clear_console()
                break
            elif(calculate_score(computer_cards)==0):
                clear_console()
                break
        print(f"computer cards = {computer_cards}\t your cards = {user_cards}")    
        compare() 
    else:
        break                   
    
