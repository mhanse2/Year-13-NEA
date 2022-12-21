import random

class Addition:
    def __init__(self, a, b):
        # all questions take lists as parameters which are then used to pick a random number
        self.a = a[random.randint(0, len(a) - 1)]
        self.b = b[random.randint(0, len(b) - 1)]
        self.ans = self.calc_ans()

    def __str__(self):
        return f'{self.a} + {self.b}'

    def calc_ans(self):
        return self.a + self.b


class Subtraction(Addition):
    def __str__(self):
        return f'{max(self.a, self.b)} - {min(self.a, self.b)}'
    
    def calc_ans(self):
        return max(self.a, self.b) - min(self.a, self.b)


class NegativeSubtraction(Subtraction):
    def __str__(self):
        return f'{min(self.a, self.b)} - {max(self.a, self.b)}'
        
    def calc_ans(self):
        return min(self.a, self.b) - max(self.a, self.b)


class Multiplication(Addition):
    def __str__(self):
        return f'{self.a} × {self.b}'
        
    def calc_ans(self):
        return self.a * self.b


class Division(Addition):
    def __str__(self):
        return f'{self.a} ÷ {self.b}'

    def calc_ans(self):
        return self.a / self.b