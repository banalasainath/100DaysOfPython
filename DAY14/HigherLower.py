from logo import logo,vs
from ref_values import data
import random
import os

def choice():
    record = random.choice(data)
    return record

def evaluate(rec1,rec2,user_choice):
    if(rec1['follower_count'] > rec2['follower_count']):
        return user_choice == 'A'    
    else:
        return user_choice == 'B'           
score=0
record2 = random.choice(data) 
print(logo)
while(True):
    #since for every next repetition the secord record becomes the first record
    record1 = record2  
    print(f"Compare A: {record1['name']}, a {record1['description']} from {record1['country']}")
    print(vs)
    while record1 == record2:
        record2 = choice()
    print(f"Against B: {record2['name']}, a {record2['description']} from {record2['country']}")
    user_choice = input("Whom do you think have more followers either A or B: ")
    os.system('cls')
    print(logo)
    if evaluate(record1,record2,user_choice):
        score = score+1
        print(f"Yeah! That's Correct. Your current Score is {score}")
    else:
        print(f"You Lost \nYour Final Score is {score}")
        break
