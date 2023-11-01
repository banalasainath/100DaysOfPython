import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# 1st, 3rd, 5th, 7th rep - 25 mins work
# 2nd, 4th, 6th rep - 5 mins break
# 8th rep - 20 mins break
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # resetting the timer on the canvas
    window.after_cancel(timer)
    # setting the timer to 00:00
    canvas.itemconfig(timer_canvas, text="00:00")
    # updating the session label to Timer
    session_label.config(text="Timer")
    # Removing all the checkmarks
    tick_label.config(text="")
    global reps
    # resetting the reps to 0
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    # Long break
    if reps == 8:
        session_label.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        reset_timer()
    elif reps % 2 == 0:
        session_label.config(text="BREAK", fg=PINK)
        # work
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 2 == 1:
        session_label.config(text="WORK", fg=GREEN)
        # short break
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    time_min = math.floor(count / 60)
    time_sec = count % 60
    if time_sec < 10:
        # Dynamic typing happening here, we are changing an integer to a string
        time_sec = f"0{time_sec}"

    # Updating the timer canvas
    canvas.itemconfig(timer_canvas, text=f"{time_min}:{time_sec}")
    if count > 0:
        global timer
        # window.after is used to call a fn or do something after a specified amount of time in milli secs
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmarks = ""
        # Adding the checkmarks after every successful 25 mins work session
        checkmarks = math.floor(reps / 2) * "✔"
        if reps % 2 != 0:
            tick_label.config(text=checkmarks)
        # restarting the timer
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas widget is similar to a canvas which allows us to layer the things one upon another
canvas = tkinter.Canvas(width=250, height=240, bg=YELLOW, highlightthickness=0)
# image param in create_image() only PhotoImage type objects
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(120, 120, image=tomato_image)

timer_canvas = canvas.create_text(120, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

session_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, 'italic'), fg=GREEN, bg=YELLOW)
session_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = tkinter.Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()
