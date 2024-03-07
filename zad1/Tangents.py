class Tangents:
    def __init__(self, a, b, function):
        self.a = a
        self.b = b
        self.function = function

    def tangents(self, epsilon):
        x0 = (self.a + self.b) / 2
        derivative_at_x0 = self.function.derivative(x0)
        if derivative_at_x0 == 0:
            raise ArithmeticError('Błąd. Dzielenie przez zero.')
        x1 = x0 - self.function.evaluate(x0) / derivative_at_x0
        while abs(x1 - x0) > epsilon:
            x0 = x1
            derivative_at_x0 = self.function.derivative(x0)
            if derivative_at_x0 == 0:
                raise ArithmeticError('Błąd. Dzielenie przez zero.')
            x1 = x0 - self.function.evaluate(x0) / derivative_at_x0

        return x1

    def tangents_iterations(self, iterations):
        x0 = (self.a + self.b) / 2
        for i in range(iterations):
            derivative_at_x0 = self.function.derivative(x0)
            if derivative_at_x0 == 0:
                raise ArithmeticError('Błąd. Dzielenie przez zero.')
            x0 = x0 - self.function.evaluate(x0) / derivative_at_x0

        return x0