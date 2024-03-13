class Bisection:
    def __init__(self, a, b, function):
        self.a = a
        self.b = b
        self.function = function

    def bisection(self, epsilon):
        x0 = (self.a + self.b) / 2
        x1 = x0
        epsilon_reached = False
        iterations = 0
        while not epsilon_reached:
            iterations += 1
            x0 = x1
            print(self.function.evaluate(self.a))
            if self.function.evaluate(self.a) * self.function.evaluate(x0) <= 0:
                self.b = x0
            else:
                self.a = x0

            x1 = (self.a + self.b) / 2
            if abs(x0 - x1) <= epsilon:
                epsilon_reached = True

            if x1 < self.a or x1 > self.b:
                print("Błąd. Miejsce zerowe nie znajduje się w podanym przedziale.")
                return None, None

        return x1, iterations

    def bisection_iterations(self, iterations):
        x0 = (self.a + self.b) / 2
        x1 = x0
        for i in range(iterations):
            x0 = x1
            if self.function.evaluate(self.a) * self.function.evaluate(x0) <= 0:
                self.b = x0
            else:
                self.a = x0

            x1 = (self.a + self.b) / 2

            if x1 < self.a or x1 > self.b:
                print("Błąd. Miejsce zerowe nie znajduje się w podanym przedziale.")
                return None, None

        precision = abs(x0 - x1)
        return x1, precision
