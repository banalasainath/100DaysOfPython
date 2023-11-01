import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
while(True):
    player_intent = input("Are you interested to play? Give us response by either yes or no : ")
    if(player_intent=="yes"):
        player_choice = int(input("Enter your choice 0 for \"rock\" 1 for \"paper\" 2 for \"scissors\" : "))
        system_choice = random.randint(0, 2)
        print(player_choice,system_choice)
        if(player_choice>=3 or player_choice<0):
            print("Invalid Input")
        else:
            print(f"Your Choice:\n {choices[player_choice]}")
            print(f"System Choice:\n {choices[system_choice]}")    
            if(player_choice==system_choice):
                print("==========TIE===========")  
            elif(player_choice==0 and system_choice==2):
                print("==========You Won===========") 
            elif(player_choice==2 and system_choice==0):
                print("==========You Lost===========")       
            elif(player_choice>system_choice):
                print("==========You Won===========")
            elif(player_choice<system_choice):
                print("==========You Lost===========") 
    else:
        break                
