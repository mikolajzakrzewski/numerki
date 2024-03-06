import math


class ExponentialFunction:
    def __init__(self, base):
        self.base = base

    def evaluate(self, x):
        result = 1.0
        for i in range(int(x)):
            result *= self.base

        return result

    def derivative(self, x):
        return self.evaluate(x) * math.log(self.base)
