import math


class ExponentialFunction:
    def __init__(self, base):
        self.base = base

    def evaluate(self, x):
        return self.base ** x

    def derivative(self, x):
        if self.base > 0:
            return self.evaluate(x) * math.log(self.base)
        else:
            raise ValueError("Podstawa wykładnicza musi być większa od zera.")
