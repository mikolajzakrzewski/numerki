import numpy as np


class CosineFunction:
    pass

    def evaluate(self, x):
        return np.cos(x)

    def derivative(self, x):
        return -1 * np.sin(x)
