from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.tk_window = Tk()
        self.tk_label = Label(text=f"Score:{0}", bg=THEME_COLOR, fg="white")
        self.tk_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.tk_window.title("Quizler App")
        self.tk_window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.true_btn = Button(text="True", background="green", command=self.true, font=("Arial", 20, "bold"), border=0)
        self.true_btn.config(pady=20, padx=20)
        self.true_btn.grid(column=1, row=2)
        self.false_btn = Button(text="False", background="red", font=("Arial", 20, "bold"), border=0,
                                command=self.false)
        self.false_btn.config(pady=20, padx=20)
        self.false_btn.grid(column=0, row=2)
        self.quiz_text = self.canvas.create_text(150, 125, width=280, text="Questions", font=("Arial", 20, "italic"),
                                                 fill=THEME_COLOR)
        self.question()

        self.tk_window.mainloop()

    def question(self):
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            self.tk_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true(self):
        self.feed_back(self.quiz.check_answer("True"))

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.feed_back(is_right)

    def feed_back(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.tk_window.after(1000, self.question)

