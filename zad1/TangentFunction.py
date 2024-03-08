import numpy as np


class TangentFunction:
    pass

    def evaluate(self, x):
        return np.tan(x)

    def derivative(self, x):
        return 1 / (np.cos(x) * np.cos(x))
