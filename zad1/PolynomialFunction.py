import Horner


def calculate_derivative_coefficients(coefficients):
    n = len(coefficients)
    if n <= 1:
        return 0

    derivative_coefficients = []
    for i in range(n):
        derivative_coefficients.append(coefficients[i] * i)

    return derivative_coefficients


class PolynomialFunction:
    def __init__(self, coefficients):
        self.horner = Horner.Horner(coefficients)

    def evaluate(self, x):
        return self.horner.evaluate(x)

    def derivative(self, x):
        derivative_coefficients = calculate_derivative_coefficients(self.horner.coefficients)
        derivative_horner = Horner.Horner(derivative_coefficients)
        return derivative_horner.evaluate(x)
