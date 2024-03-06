class Bisection:
    def __init__(self, a, b, function):
        self.a = a
        self.b = b
        self.function = function

    def bisection(self, epsilon):
        x0 = (self.a + self.b) / 2
        x1 = x0
        epsilon_reached = False
        while not epsilon_reached:
            x0 = x1
            if self.function.evaluate(self.a) * self.function.evaluate(x0) < 0:
                self.b = x0
            else:
                self.a = x0

            x1 = (self.a + self.b) / 2
            if abs(x0 - x1) <= epsilon:
                epsilon_reached = True

        return x1

    def bisection_iterations(self, iterations):
        x0 = (self.a + self.b) / 2
        x1 = x0
        for i in range(iterations):
            x0 = x1
            if self.function.evaluate(self.a) * self.function.evaluate(x0) < 0:
                self.b =x0
            else:
                self.a = x0

            x1 = (self.a + self.b) / 2

        return x1

