class CompositeFunction:
    def __init__(self, function_1, function_2):
        self.function_1 = function_1
        self.function_2 = function_2

    def evaluate(self, x):
        return self.function_1.evaluate(self.function_2.evaluate(x))

    def derivative(self, x):
        print(self.function_2.evaluate(x))
        print(self.function_1.derivative(self.function_2.evaluate(x)))
        return self.function_1.derivative(self.function_2.evaluate(x)) * self.function_2.derivative(x)
