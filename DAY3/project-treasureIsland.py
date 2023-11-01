# conditional statements and logical operators
print("Welcome to Treasure Island.\n Your mission is to find the treasure")
cmd1 = input("choose either left or right?\n")
if(cmd1=="left"):
    print("Your choice is perfect")
    cmd2 = input("choose either swim or wait?\n")
    if(cmd2=="wait"):
        print("You are Brilliant")
        cmd3=input("choose the doors ahead of you which are Red, Yellow, Blue? Choose any of those three colours\n")
        if(cmd3=="Red"):
            print("Burned by fire. Game Over.")
        elif(cmd3=="Blue"):
            print("Eaten by beasts. Game Over.")
        elif(cmd3=="Yellow"):
            print("You Win")
        else:
            print("Game Over")                        
    else:
        print("Attacked by trout. Game Over.")    
else:
    print("Fall into a hole. \nGame Over.")
