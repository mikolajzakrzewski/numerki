import math


class TangentFunction:
    pass

    def evaluate(self, x):
        return math.tan(x)

    def derivative(self, x):
        return 1/(math.cos(x)*math.cos(x))
