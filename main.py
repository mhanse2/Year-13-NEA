# local modules
import questions
import ui

# other modules
import random
from guizero import *


app = App('Mental Maths Quiz [App]', 600, 500)    # loads the app
app.tk.resizable(0, 0)    # makes the window unable to be resized
quiz_window = ui.QuizWindow(app)    # creates the quiz's window


def main():
    dummy = questions.Triangle([4], [4])
    quiz_window.submit.update_command(command=quiz_window.update_feedback,
                                      args=[dummy.ans])
    quiz_window.update_question(dummy)
    app.display()


if __name__ == '__main__':
    main()
