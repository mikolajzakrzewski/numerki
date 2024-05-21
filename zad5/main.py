import numpy as np
import matplotlib.pyplot as plt

from AbsoluteValue import AbsoluteValue
from SineFunction import SineFunction
from CosineFunction import CosineFunction
from TangentFunction import TangentFunction
from ExponentialFunction import ExponentialFunction
from PolynomialFunction import PolynomialFunction
from CompositeFunction import CompositeFunction


def simpson(a, b, function):
    h = (b - a) / 2
    result = h / 3 * (function(a) * np.exp(-a) +
                      4 * function(a + h) * np.exp(-(a + h)) +
                      function(b) * np.exp(-b))
    return result


def composite_simpson(a, b, function, n):
    result = 0
    h = (b - a) / n
    for i in range(n):
        x = a + i * h
        x_1 = a + (i + 1) * h
        result += simpson(x, x_1, function)

    return result


def gauss_laguerre_nodes_weights(n):
    weights = []
    nodes = []
    with open('laguerre.txt', 'r') as f:
        i = 2
        j = 0
        temp_weights = []
        temp_nodes = []
        for line in f:
            if line.startswith('n') or line.strip() == '':
                continue
            else:
                values = line.strip().split()
                temp_weights.append(float(values[0]))
                temp_nodes.append(float(values[1]))
                j += 1
                if j == i:
                    weights.append(temp_weights.copy())
                    temp_weights.clear()
                    nodes.append(temp_nodes.copy())
                    temp_nodes.clear()
                    i += 1
                    j = 0
    return nodes[n], weights[n]


def hermite_coefficients(func, degree, num_nodes):
    nodes, weights = gauss_laguerre_nodes_weights(num_nodes)
    values = np.array([func.evaluate(node) for node in nodes])
    h = np.polynomial.hermite.Hermite.fit(nodes, values, degree, w=weights)
    return h.convert().coef


def function_choice():
    while True:
        chosen_function = input()
        if chosen_function == '1':
            print('Wybierz funkcje trygonometryczna:\n1. Sinus\n2. Cosinus\n3. Tangens')
            while True:
                trigonometric_function = input()
                if trigonometric_function == '1':
                    return SineFunction()
                elif trigonometric_function == '2':
                    return CosineFunction()
                elif trigonometric_function == '3':
                    return TangentFunction()
                else:
                    print('Niepoprawny wybór. Wybierz jeszcze raz.')

        elif chosen_function == '2':
            base = float(input('Podaj podstawe funkcji(a): '))
            return ExponentialFunction(base)
        elif chosen_function == '3':
            degree = int(input('Podaj stopien wielomianu: '))
            print('Podaj wspolczynniki wielomianu od najwyzszego:')
            coefficients = []
            for i in range(degree + 1):
                coefficients.append(float(input()))

            return PolynomialFunction(coefficients)
        elif chosen_function == '4':
            return AbsoluteValue()
        else:
            print('Niepoprawny wybór. Wybierz jeszcze raz.')


def range_choice():
    print('Podaj początek przedziału a:')
    start = float(input())
    print('Podaj koniec przedziału b:')
    end = float(input())
    return start, end


def approximation_error(func, approx_func, a, b, n):
    error_func = lambda x: (func.evaluate(x) - approx_func(x)) ** 2
    error = composite_simpson(a, b, error_func, n)
    return np.sqrt(error)


def main():
    while True:
        print('Wybierz rodzaj funkcji: \n1. Pojedyncza\n2. Złożona')
        while True:
            choice = input()
            if choice == '1':
                print('Wybierz funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian\n4. Moduł')
                function = function_choice()
                break
            elif choice == '2':
                print('Wybierz pierwszą funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian\n4. Moduł')
                function_1 = function_choice()
                print('Wybierz drugą funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian\n4. Moduł')
                function_2 = function_choice()
                function = CompositeFunction(function_1, function_2)
                break
            else:
                print('Niepoprawny wybór. Wybierz jeszcze raz.')

        a, b = range_choice()
        degree = int(input('Podaj stopień wielomianu aproksymacyjnego: '))
        num_nodes = int(input('Podaj liczbę węzłów: '))

        coefficients = hermite_coefficients(function, degree, num_nodes)
        print(f'Współczynniki wielomianu Hermite\'a: {coefficients}')

        approx_func = np.polynomial.hermite.Hermite(coefficients).convert()

        error = approximation_error(function, approx_func, a, b, 5)
        print(f'Błąd aproksymacji: {error}')

        x = np.linspace(a, b, 400)
        y = np.array([function.evaluate(xi) for xi in x])
        y_approx = approx_func(x)

        plt.plot(x, y, label='Oryginalna funkcja')
        plt.plot(x, y_approx, label='Aproksymacja Hermite\'a')
        plt.legend()
        plt.title('Aproksymacja funkcji wielomianem Hermite\'a')
        plt.show()

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()