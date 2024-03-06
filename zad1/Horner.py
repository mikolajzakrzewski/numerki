class Horner:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        degree = len(self.coefficients) - 1
        if degree == 0:
            return self.coefficients[0]
        else:
            result = self.coefficients[degree]

        for i in range(degree - 1, -1, -1):
            result = result * x + self.coefficients[i]

        return result
