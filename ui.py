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
                          text='your code isn\'t working bozo',  # a very polite error catch
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

        # Misc UI #

        # Save & Quit Button
        self.quit = PushButton(master=self,
                               text='Save & Quit',
                               align='bottom')
        # Counter 
        self.counter = Text(master=self,
                            text='Questions Answered',
                            size=10,
                            align='bottom')

    def update_question(self, ques):
        # sets the question itself
        print(str(ques))
        self.qtext.value = str(ques)
        # checks if the question has an image
        if ques.image is None:
            # if it doesn't, disable the image object
            self.image.enabled = False
        else:
            # if it does, enable the image object and set the image to the question's
            self.image.enabled = True
            self.image.image = ques.image

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

        # runs if the answer is not an integer
        except ValueError:
            self.feedback.text_color = 'goldenrod'
            self.feedback.value = 'Your answer is not an integer.'

        # runs if there is nothing inputted into the answer box
        except TypeError:
            self.feedback.text_color = 'goldenrod'
            self.feedback.value = "You didn't write an answer."

        finally:
            self.feedback.visible = True
            self.feedback.after(1500,
                                self._disable_feedback)

    def _disable_feedback(self):
        self.feedback.visible = False
