import turtle
import pandas as pd

screen = turtle.Screen()
screen.listen()

turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.penup()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_coordinates(x, y):
#     print(x, y)
# helps in getting the coordinates where the pointer was clicked
# turtle.onclick(get_coordinates)
input_file = pd.read_csv('50_states.csv')
state_names = input_file["state"].to_list()
user_score = 0
identified_states = []

while user_score < 50:
    users_answer = screen.textinput(title=f"{user_score}/50 States", prompt="Enter the state name").capitalize()
    # Coming out of the loop whenever user enter exit
    if users_answer == "Exit":
        break
    if users_answer in state_names:
        identified_states.append(users_answer)
        user_score += 1
        # x_cor = int(input_file[input_file["state"] == users_answer.capitalize()]['x'])
        # y_cor = int(input_file[input_file["state"] == users_answer.capitalize()]['y'])
        state_row = input_file[input_file["state"] == users_answer]
        turtle1.goto(int(state_row.x), int(state_row.y))
        # turtle1.write(users_answer.capitalize())
        turtle1.write(state_row.state.item())


# turtle.mainloop is used to continue the program even if the program execution completed
# turtle.mainloop()
# unidentified_states = []
# for state in state_names:
#     if state not in identified_states:
#         unidentified_states.append(state)

unidentified_states = [state for state in state_names if state not in identified_states]


unidentified_states_df = pd.DataFrame({
        "Unidentified States": unidentified_states
    }
)

unidentified_states_df.to_csv('unidentified_states.csv')



