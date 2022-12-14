# local modules
import questions
import ui

# other modules
import random
from guizero import *


def main():
    app = App('Mental Maths Quiz [App]', 600, 500)
    app.tk.resizable(0, 0)
    quiz_window = ui.QuizWindow(app)
    dummy = questions.Addition([3], [5])
    quiz_window.qtext.value = str(dummy)
    app.display()


if __name__ == '__main__':
    main()
