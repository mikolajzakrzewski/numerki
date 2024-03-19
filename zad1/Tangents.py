class Tangents:
    def __init__(self, a, b, function):
        self.a = a
        self.b = b
        self.function = function

    def tangents(self, epsilon):
        if self.function.evaluate(self.a) * self.function.evaluate(self.b) >= 0:
            print(
                "Uwaga: na krańcach badanego przedziału funkcja nie ma przeciwnych znaków, brak gwarancji rozwiązania."
            )

        x0 = (self.a + self.b) / 2
        derivative_at_x0 = self.function.derivative(x0)
        x1 = x0 - self.function.evaluate(x0) / derivative_at_x0
        iterations = 0
        while abs(x1 - x0) > epsilon:
            iterations += 1
            x0 = x1
            derivative_at_x0 = self.function.derivative(x0)
            x1 = x0 - self.function.evaluate(x0) / derivative_at_x0

            if x1 < self.a or x1 > self.b:
                print("Błąd. Miejsce zerowe nie znajduje się w podanym przedziale.")
                return None, None

        return x1, iterations

    def tangents_iterations(self, iterations):
        if self.function.evaluate(self.a) * self.function.evaluate(self.b) >= 0:
            print(
                "Uwaga: na krańcach badanego przedziału funkcja nie ma przeciwnych znaków, brak gwarancji rozwiązania."
            )

        x0 = (self.a + self.b) / 2
        precision = 0
        for i in range(iterations):
            derivative_at_x0 = self.function.derivative(x0)
            x1 = x0 - self.function.evaluate(x0) / derivative_at_x0
            precision = abs(x1 - x0)
            x0 = x1

            if x0 < self.a or x0 > self.b:
                print("Błąd. Miejsce zerowe nie znajduje się w podanym przedziale.")
                return None, None

        return x0, precision
