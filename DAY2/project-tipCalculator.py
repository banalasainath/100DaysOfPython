print("Welcome to the tip Calculator")
total_bill = float(input("What was the total bill? \n"))
people_count = int(input("How many people to split the bill?\n"))
percentage = int(input("What percentage tip would you like to give? 10,12 or 15?\n"))
tip = round((total_bill/100)*percentage, 2)
total_amount = total_bill + tip
print(f"Each person should pay {round(total_amount/people_count,2)}")
