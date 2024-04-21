class Horner:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        result = self.coefficients[0]
        for i in range(1, len(self.coefficients)):
            result = result * x + self.coefficients[i]

        return result
