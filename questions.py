# local modules
import util

# other modules
import random


class QuestionQueue:
    def __init__(self, level):
        pass # TODO: generate a list of questions based on the level


class Addition:
    def __init__(self, a, b):
        # all questions take lists as parameters which are then used to pick a random number
        self.a = a[random.randint(0, len(a) - 1)]
        self.b = b[random.randint(0, len(b) - 1)]
        self.ans = self._calc_ans()
        self.image = None

    def __str__(self):
        return f'{self.a} + {self.b}'

    def _calc_ans(self):
        return self.a + self.b


class Subtraction(Addition):
    def __str__(self):
        return f'{max(self.a, self.b)} - {min(self.a, self.b)}'
    
    def _calc_ans(self):
        return max(self.a, self.b) - min(self.a, self.b)


class NegativeSubtraction(Subtraction):
    def __str__(self):
        return f'{min(self.a, self.b)} - {max(self.a, self.b)}'
        
    def _calc_ans(self):
        return min(self.a, self.b) - max(self.a, self.b)


class Multiplication(Addition):
    def __str__(self):
        return f'{self.a} × {self.b}'
        
    def _calc_ans(self):
        return self.a * self.b


class Division(Addition):
    def __str__(self):
        return f'{self.a} ÷ {self.b}'

    def _calc_ans(self):
        return self.a / self.b


class Power(Addition):
    def __str__(self):
        return f'{self.a}{util.superscript(self.b)}'

    def _calc_ans(self):
        return pow(self.a, self.b)


class Root(Power):
    def __str__(self):
        return f'{util.superscript(self.b) if self.b != 2 else ""}√{self.a}'

    def _calc_ans(self):
        return pow(self.a, 1/self.b)


class Triangle(Addition):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.image = 'images/triangle.png'

    def __str__(self):
        return f'a = {self.a} & b = {self.b}\nWhat is the area of this right-angled triangle?'

    def _calc_ans(self):
        return (self.a * self.b) / 2


class SquareArea(Addition):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.image = 'images/square.png'

    def __str__(self):
        return f'a = {self.a} & b = {self.b}\nWhat is the area of this rectangle?'

    def _calc_ans(self):
        return self.a * self.b


class SquarePerimeter(SquareArea):
    def __str__(self):
        return f'a = {self.a} & b = {self.b}\nWhat is the perimeter of this rectangle?'

    def _calc_ans(self):
        return 2 * (self.a * self.b)


class CircleArea:
    def __init__(self, a):
        self.a = a[random.randint(0, len(a) - 1)]
        self.ans = self._calc_ans()
        self.image = 'images/circle.png'

    def __str__(self):
        return f'r = {self.a}\nWhat is the area of this circle?'

    def _calc_ans(self):
        return pow(self.a, 2)


class CirclePerimeter(CircleArea):
    def __str__(self):
        return f'r = {self.a}\nWhat is the perimeter of this circle?'

    def _calc_ans(self):
        return 2 * self.a


'''
    QUESTION EXPLANATIONS
    
    Addition: Addition. 
        a + b = c
    Subtraction: Subtraction. Always results in a positive or zero answer. 
        a - b = c, where a > b.
    NegativeSubtraction: Subtraction. Always results in a negative or zero answer. 
        a - b = c, where a < b.
    Multiplication: Multiplication.
        a * b = c
    Division: Division. Given inputs will always result in an integer answer.
        a / b = c, where a > b and c = int
'''