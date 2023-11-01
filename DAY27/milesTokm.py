import tkinter

window = tkinter.Tk()
window.title("Miles To KM Converter")
# Even though we can vary the size of the window, we can create the window with minsize
window.minsize(width=300, height=200)

miles_label = tkinter.Label(text="Miles", font=("Times New Roman", 10, "bold"))
miles_label.grid(column=2, row=0)

isequal_label = tkinter.Label(text="is Equal to", font=("Times New Roman", 10, "bold"))
isequal_label.grid(column=0, row=1)

answer_label = tkinter.Label(text=0, font=("Times New Roman", 10, "bold"))
answer_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Times New Roman", 10, "bold"))
km_label.grid(column=2, row=1)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)


def converter():
    miles = int(user_input.get())
    km = miles * 1.60
    answer_label.config(text=km)


button = tkinter.Button(text="Convert", command=converter)
button.grid(column=1, row=2)

window.mainloop()