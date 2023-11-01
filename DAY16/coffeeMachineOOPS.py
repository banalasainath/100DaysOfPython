# What a real world object can have are the attributes of the class, and what the object can do are the 
# methods of the class
# A class name should strt with CapitalLetter and every word in the name should be of Capital letter and 
# there shouldn't be any spaces or underscores inside the name, this type of case is known as pascal case
# from turtle import Turtle, Screen
#
# turt = Turtle()
# turt.forward(100)
# turt.color("green")
# turt.shape("classic")
# screen = Screen()
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name", ["Sainath", "Surya", "Krishnavamsi"])
table.add_column("Roll No", [10, 8, 56])
table.align = "l"
print(table)
