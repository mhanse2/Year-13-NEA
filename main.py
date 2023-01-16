# local modules
import questions
import ui

# other modules
import random
from guizero import *


app = App('Mental Maths Quiz [App]', 600, 500)    # loads the app
app.tk.resizable(0, 0)    # makes the window unable to be resized
quiz_window = ui.QuizWindow(app)    # creates the quiz's window
cur_queue = questions.QuestionQueue(1)
app.display()


def main():
    quiz_window.update_question(cur_queue.current)
    quiz_window.submit.update_command(command=submit)


def submit():
    quiz_window.update_feedback(cur_queue.current.ans)
    try:
        if cur_queue.current.ans == int(quiz_window.answer.value):
            cur_queue.next_question()

    except ValueError:
        pass


if __name__ == '__main__':
    main()
