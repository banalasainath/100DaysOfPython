import tkinter

# creating a window using Tk() class
window = tkinter.Tk()
window.title("TKinter learning")
# Even though we can vary the size of the window, we can create the window with minsize
window.minsize(width=500, height=300)
# To add padding
window.config(padx=20, pady=20)


# Button, label, input_box .... are called widgets

# Tkinter has three layout managers: 1. Pack() 2. Place() 3. Grid().
# Pack() places the widgets next to each other in a logical format, Pack() by default starts from the top and adds the
# others down to it. If we use pack(side="left) to all widgets then all widgets will be in a single line from left to
# right, we can side to right or bottom.

# In place() we will pass x and y coordinates where the widget needs to be placed. This will be very precise. place(x=,y=)

# In grid() we will assume the whole window is divided into grids. We will specify column and row according to where
# that widget needs to be placed. grid(column=0, row=0)

# Note: We can't use grid() and pack() on a same program, we need to use either grid() or pack(),
# but we can use grid() and place() or place() and pack() once


# From all the three, grid() is the most preferred way of layout

# creating a label using the Label class
first_label = tkinter.Label(text="First Text", font=("Times New Roman", 24, "italic"))
# To display or bundle the label we need to use the pack(), with pack() we can change the position, etc.. of the label
# first_label.pack()
# first_label.place(x=100, y=100)
first_label.grid(column=0, row=0)
# We can add padding to widgets also
first_label.config(padx=20, pady=20)

# editing the variables of Label
first_label["text"] = "Editable text"
# or
first_label.config(text="Starting line")


# buttons
def button_clicked():
    # taking the input using Entry class object
    user_entered_input = user_input.get()
    # changing the label whenever the button got clicked
    first_label.config(text=user_entered_input)
    print("Button clicked")


button = tkinter.Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)


new_button = tkinter.Button(text="New_Click", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry class to take the input from the user
user_input = tkinter.Entry(width=20)
user_input.grid(column=3, row=2)
















# Command to remain the window open
window.mainloop()
