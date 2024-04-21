import SineFunction
import CosineFunction
import TangentFunction
import ExponentialFunction
import PolynomialFunction
import CompositeFunction

import numpy as np


def get_nodes(a, b, k):
    nodes = np.zeros(k)
    for i in range(k):
        node = ((a + b) / 2) + ((b - a) / 2) * np.cos((((2 * i) + 1) * np.pi) / (2 * k))
        nodes[i] = node
    return nodes


def divided_diff(a, b, k, function):
    nodes_x_coordinates = get_nodes(a, b, k)
    n = len(nodes_x_coordinates)
    nodes_y_coordinates = np.zeros(n)
    for i in range(n):
        nodes_y_coordinates[i] = function.evaluate(nodes_x_coordinates[i])

    coefficients = np.zeros([n, n])
    coefficients[:, 0] = nodes_y_coordinates
    for i in range(1, n):
        for j in range(n - i):
            coefficients[j, i] = (
                    coefficients[j + 1, i - 1] - coefficients[j, i - 1] /
                    (nodes_x_coordinates[j + i] - nodes_x_coordinates[j])
            )

    return coefficients[0]


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
        else:
            print('Niepoprawny wybór. Wybierz jeszcze raz.')


def range_choice():
    start = float(input('Podaj początek przedziału a: '))
    end = float(input('Podaj koniec przedziału b: '))
    return start, end


def nodes_number_choice():
    nodes_number = int(input('Podaj liczbę węzłów Czebyszewa: '))
    return nodes_number


def main():
    while True:
        print('Wybierz rodzaj funkcji: \n1. Pojedyncza\n2. Złożona')
        while True:
            choice = input()
            if choice == '1':
                print('Wybierz funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian')
                function = function_choice()
                break
            elif choice == '2':
                print('Wybierz pierwszą funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian')
                function_1 = function_choice()
                print('Wybierz drugą funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian')
                function_2 = function_choice()
                function = CompositeFunction.CompositeFunction(function_1, function_2)
                break
            else:
                print('Niepoprawny wybór. Wybierz jeszcze raz.')

        a, b = range_choice()
        k = nodes_number_choice()
        print(divided_diff(a, b, k, function))
        # TODO
        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
