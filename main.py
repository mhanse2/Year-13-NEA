# local modules
import questions
import ui

# other modules
import random
from guizero import *


app = App('Mental Maths Quiz [App]', 600, 500)
app.tk.resizable(0, 0)
quiz_window = ui.QuizWindow(app)


def main():
    dummy = questions.Triangle([4], [4])
    quiz_window.qtext.value = str(dummy)
    quiz_window.submit.update_command(command=quiz_window.update_feedback,
                                      args=[dummy.ans])
    quiz_window.set_image(dummy.image)
    app.display()


if __name__ == '__main__':
    main()
