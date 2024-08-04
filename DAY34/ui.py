from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizLayout:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        # window creation
        self.window = Tk()
        self.window.title("SelfAssessment")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label for score
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas for question showup
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Added lesser width for create_text than the Canvas to get the text wrapped in the canvas
        self.question_layout = self.canvas.create_text(150, 125,
                                                       width=280,
                                                       text="Question to be answered",
                                                       fill=THEME_COLOR,
                                                       font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_chosen)
        self.true_button.grid(row=2, column=1)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_chosen)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # redoing the bg color white, after it got changed to either green or red based on the previous answer
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_layout, text=next_question)
        else:
            self.canvas.itemconfig(self.question_layout, text="You've completed your quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_chosen(self):
        is_correct = self.quiz.check_answer("True")
        self.validate_answer(is_correct)

    def false_chosen(self):
        self.validate_answer(self.quiz.check_answer("False"))

    def validate_answer(self, is_correct):
        if is_correct:
            # changing the bg color to green when the answer chosen was right
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # 1000 refers to the millisecond
        self.window.after(1000, self.get_next_question)
