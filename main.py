# local modules
import questions

# other modules
import random
from guizero import *


def main():
    app = App('Mental Maths Quiz [App]', 600, 500)
    main.tk.resizable(0, 0)
    init_windows()
    app.display()


def init_windows():
    ## QUIZ WINDOW ##
    quiz_window = Window(app, 'Mental Maths Quiz [Quiz State]', 600, 500)
    quiz_window.tk.resizable(0, 0)

    # Questions
    question_box = Box(quiz_window,
                       layout='grid',
                       align='top',
                       width=400,
                       height=500)
    question_text = Text(question_box,
                         text='i am a question',
                         grid=[0,1])
    question_answer = TextBox(question_box,
                              width=300,
                              grid=[0,2])       # TODO: Add command + arguments
    question_image = Picture(question_box,
                             grid=[0,0],
                             enabled=False)
    question_submit = PushButton(question_box,
                                 text='Submit') # TODO: Add command + arguments

    # Misc UI
    counter = Text(quiz_window,
                   text='Questions Answered',
                   size=10)
    quit_button = PushButton(quiz_window,
                             text='Submit')     # TODO: Add command + arguments

    quiz_window.hide()

    ## MENU WINDOW ##
    menu_window = Window(app, 'Mental Maths Quiz [Menu State]')
    menu_window.tk.resizable(0, 0)
