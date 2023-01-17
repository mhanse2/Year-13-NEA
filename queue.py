import questions


class QuestionQueue:
    def __init__(self, level):
        self.queue = [questions.Addition([4], [5]), questions.Subtraction([2], [6]), questions.Triangle([4], [4])]
        self.finished = []
        self.current = self.queue[0]

    def next_question(self):
        q = self.queue.pop(0)
        self.finished.append(q)
        self._generate_question(q)
        self.current = self.queue[0]

    def _generate_question(self, old):
        self.queue.append(questions.Addition([1], [1]))
        # TODO
