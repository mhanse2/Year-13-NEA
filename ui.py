from guizero import *


class QuizWindow(Window):
    def __init__(self, master, title='Mental Maths Quiz [Quiz State]',
                 width=600, height=500, layout='auto', bg=None, visible=True):
        super().__init__(master, title, width, height, layout, bg, visible)
        self.tk.resizable(0, 0)

        # Main Question UI
        self.qtext = Text(master=self,
                          text='i am a question',
                          align='top')
        self.answer = TextBox(master=self,
                              width=20,
                              align='top')
        self.image = Picture(master=self,
                             align='top',
                             enabled=False)
        self.submit = PushButton(master=self,
                                 text='Submit',
                                 align='top')

        # Misc UI
        self.quit = PushButton(master=self,
                               text='Save & Quit',
                               align='bottom')
        self.counter = Text(master=self,
                            text='Questions Answered',
                            size=10,
                            align='bottom')
