from guizero import *


class QuizWindow(Window):
    def __init__(self, master, title='Mental Maths Quiz [Quiz State]',
                 width=600, height=500, layout='auto', bg=None, visible=True):
        super().__init__(master, title, width, height, layout, bg, visible)
        self.tk.resizable(0, 0)

        # Main Question UI #

        # Question Image
        self.image = Picture(master=self,
                             align='top',
                             enabled=False)
        # Question Text
        self.qtext = Text(master=self,
                          text='i am a question',
                          align='top')
        # Answer Box
        self.answer = TextBox(master=self,
                              width=20,
                              align='top')
        # Submit Button
        self.submit = PushButton(master=self,
                                 text='Submit',
                                 align='top',
                                 command=self.update_feedback)
        # Small Feedback Text
        self.feedback = Text(master=self,
                             size=10,
                             color='red',
                             align='top',
                             visible=False)

        # Misc UI
        self.quit = PushButton(master=self,
                               text='Save & Quit',
                               align='bottom')
        self.counter = Text(master=self,
                            text='Questions Answered',
                            size=10,
                            align='bottom')

    def update_feedback(self, ans):
        # compares the given answer to the actual answer
        try:
            # if the answer's correct
            if ans == int(self.answer.value):
                self.feedback.text_color = 'green'
                self.feedback.value = 'Correct!'
            # if the answer's not correct
            else:
                self.feedback.text_color = 'red'
                self.feedback.value = 'Incorrect.'
            # clears the answer box
            self.answer.value = ''

        # only runs if the answer is not an integer
        except ValueError:
            self.feedback.text_color = 'goldenrod'
            self.feedback.value = 'Your answer is not an integer.'

        self.feedback.visible = True
        self.feedback.after(1500,
                            self.disable_feedback)

    def disable_feedback(self):
        self.feedback.visible = False

    def set_image(self, image):
        if image is None:
            self.image.enabled = False
        else:
            self.image.enabled = True
            self.image.image = image
