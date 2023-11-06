import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    # Getting the unknown words file if exists
    french_words_not_known = pandas.read_csv("data/To_be_learn.csv")
except FileNotFoundError:
    # orient helps in arranging the csv file as [{key: value, key: value,.. }, {key: value, key: value}] for all the
    # rows
    all_french_words = pandas.read_csv("data/french_words.csv")
    french_words_to_learn_dict = all_french_words.to_dict(orient="records")
else:
    french_words_to_learn_dict = french_words_not_known.to_dict(orient="records")

# creating a global variable to store the present card
present_card = {}


def change_word():
    global present_card, flip_timer
    window.after_cancel(flip_timer)
    present_card = random.choice(french_words_to_learn_dict)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=present_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=present_card["English"], fill="white")


def remove_word():
    print(present_card)
    # adding the known word to a separate file
    french_words_to_learn_dict.remove(present_card)
    dump_dict = pandas.DataFrame(french_words_to_learn_dict)
    # index=False enables to not place index at beginning of the rows
    dump_dict.to_csv("data/To_be_learn.csv", index=False)

    change_word()



window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")

# setting the time to flip the card
flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# card_front_img
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
# card_back_img
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
# Title
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
# Word
canvas_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))


# Buttons
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)

tick_img = tkinter.PhotoImage(file="images/right.png")
tick_button = tkinter.Button(image=tick_img, highlightthickness=0, command=remove_word)
tick_button.grid(row=1, column=1)

change_word()

window.mainloop()

