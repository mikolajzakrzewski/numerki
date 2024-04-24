import AbsoluteValue
import SineFunction
import CosineFunction
import TangentFunction
import ExponentialFunction
import PolynomialFunction
import CompositeFunction

import numpy as np
import matplotlib.pyplot as plt


def get_chebyshev_nodes(a, b, k):
    nodes = np.zeros(k)
    for i in range(k):
        node = ((a + b) / 2) + ((b - a) / 2) * np.cos((((2 * i) + 1) * np.pi) / (2 * k))
        nodes[i] = node
    return nodes


def divided_difference(a, b, k, function):
    nodes_x_values = get_chebyshev_nodes(a, b, k)
    n = len(nodes_x_values)
    nodes_y_values = np.zeros(n)
    for i in range(n):
        nodes_y_values[i] = function.evaluate(nodes_x_values[i])

    coefficients = np.zeros([n, n])
    coefficients[:, 0] = nodes_y_values
    for i in range(1, n):
        for j in range(n - i):
            coefficients[j, i] = (
                (coefficients[j + 1, i - 1] - coefficients[j, i - 1]) /
                (nodes_x_values[j + i] - nodes_x_values[j])
            )

    return coefficients[0]


def newton_polynomial_evaluate(x_to_evaluate, x_values, coefficients):
    n = len(x_values)
    result = 0
    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x_to_evaluate - x_values[j])
        result += term
    return result


def plot_function(range_start, range_end, function_to_plot,
                  chebyshev_x_values, coefficients,
                  x_values_to_evaluate, evaluated_y_values, limit_y):
    x = np.linspace(range_start, range_end, 10000)
    plt.figure(figsize=(8, 8))
    plt.plot(
        x, function_to_plot.evaluate(x), label='Wykres funkcji oryginalnej'
    )
    plt.plot(
        x, newton_polynomial_evaluate(x, chebyshev_x_values, coefficients), label='Wykres wielomianu interpolującego'
    )
    chebyshev_y_values = np.zeros(len(chebyshev_x_values))
    for i in range(len(chebyshev_x_values)):
        chebyshev_y_values[i] = function_to_plot.evaluate(chebyshev_x_values[i])

    plt.scatter(chebyshev_x_values, chebyshev_y_values, label='Węzły Czebyszewa')
    plt.scatter(x_values_to_evaluate, evaluated_y_values, label='Obliczone punkty')

    if limit_y == 1:
        y_values = np.zeros(len(x))
        for i in range(len(y_values)):
            y_values[i] = function_to_plot.evaluate(x[i])

        median = np.median(y_values)
        plt.ylim(median - 100, median + 100)

    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def function_choice():
    while True:
        chosen_function = input()
        if chosen_function == '1':
            print('Wybierz funkcje trygonometryczna:\n1. Sinus\n2. Cosinus\n3. Tangens')
            while True:
                trigonometric_function = input()
                if trigonometric_function == '1':
                    return SineFunction.SineFunction()
                elif trigonometric_function == '2':
                    return CosineFunction.CosineFunction()
                elif trigonometric_function == '3':
                    return TangentFunction.TangentFunction()
                else:
                    print('Niepoprawny wybór. Wybierz jeszcze raz.')

        elif chosen_function == '2':
            base = float(input('Podaj podstawe funkcji(a): '))
            return ExponentialFunction.ExponentialFunction(base)
        elif chosen_function == '3':
            degree = int(input('Podaj stopien wielomianu: '))
            print('Podaj wspolczynniki wielomianu od najwyzszego:')
            coefficients = []
            for i in range(degree + 1):
                coefficients.append(float(input()))

            return PolynomialFunction.PolynomialFunction(coefficients)
        elif chosen_function == '4':
            return AbsoluteValue.AbsoluteValue()
        else:
            print('Niepoprawny wybór. Wybierz jeszcze raz.')


def range_choice():
    start = float(input('Podaj początek przedziału a: '))
    end = float(input('Podaj koniec przedziału b: '))
    return start, end


def nodes_number_choice():
    nodes_number = int(input('Podaj liczbę węzłów Czebyszewa: '))
    return nodes_number


def x_values_choice():
    number_of_x_values = int(input('Podal liczbę punktów x do wyliczenia: '))
    x_values = np.zeros(number_of_x_values)
    for i in range(number_of_x_values):
        x_values[i] = (float(input('Podaj wartość punktu nr ' + str(i + 1) + ': ')))

    return x_values


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
                function = CompositeFunction.CompositeFunction(function_1, function_2)
                break
            else:
                print('Niepoprawny wybór. Wybierz jeszcze raz.')

        a, b = range_choice()
        k = nodes_number_choice()
        coefficients = divided_difference(a, b, k, function)
        chebyshev_x_values = get_chebyshev_nodes(a, b, k)

        x_values = x_values_choice()
        evaluated_y_values = np.zeros(len(x_values))
        for i in range(len(evaluated_y_values)):
            evaluated_y_values[i] = newton_polynomial_evaluate(x_values[i], chebyshev_x_values, coefficients)

        limit_y = int(input('Czy chcesz ustawić limit na osi OY? (środkowa wartość - 100, środkowa wartość + 100)'
                            '\n 0 – nie'
                            '\n 1 – tak'
                            '\n'))
        plot_function(a, b, function, chebyshev_x_values, coefficients, x_values, evaluated_y_values, limit_y)
        print('Wartości wielomianu interpolującego dla zadanych punktów:')
        for i in range(len(evaluated_y_values)):
            print('x = ' + str(x_values[i]) + ', y = ' + str(evaluated_y_values[i]))

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
