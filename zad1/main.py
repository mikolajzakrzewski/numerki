import Bisection
import CosineFunction
import ExponentialFunction
import PolynomialFunction
import SineFunction
import TangentFunction
import Tangents
import CompositeFunction

import numpy as np
from matplotlib import pyplot as plt


def function_choice():
    chosen_function = input()
    if chosen_function == '1':
        print('Wybierz funkcje trygonometryczna:\n1. Sinus\n2. Cosinus\n3. Tangens')
        trigonometric_function = input()
        if trigonometric_function == '1':
            return SineFunction.SineFunction()
        elif trigonometric_function == '2':
            return CosineFunction.CosineFunction()
        elif trigonometric_function == '3':
            return TangentFunction.TangentFunction()
        else:
            print('Niepoprawny wybór.')
    elif chosen_function == '2':
        print('Podaj podstawe funkcji(a):')
        base = float(input())
        # print('Podaj stala c:')
        # constant = float(input())
        return ExponentialFunction.ExponentialFunction(base)
    elif chosen_function == '3':
        print('Podaj stopien wielomianu:')
        degree = int(input())
        print('Podaj wspolczynniki wielomianu od najwyzszego:')
        coefficients = []
        for i in range(degree + 1):
            coefficients.append(float(input()))

        return PolynomialFunction.PolynomialFunction(coefficients)
    else:
        print('Niepoprawny wybór.')


def range_choice():
    print('Podaj początek przedziału a:')
    start = float(input())
    print('Podaj koniec przedziału b:')
    end = float(input())
    return start, end


def plot_function(range_start, range_end, function_to_plot, bisection_zero_point, tangents_zero_point):
    x = np.linspace(range_start, range_end, 10000)
    plt.figure(figsize=(8, 8))
    plt.plot(x, function_to_plot.evaluate(x), label='Wykres funkcji f(x)')
    plt.plot(
        bisection_zero_point, 0, 'o', label='Miejsce zerowe obliczone metodą bisekcji: ' + str(bisection_zero_point)
    )
    plt.plot(
        tangents_zero_point, 0, 'o', label='Miejsce zerowe obliczone metodą stycznych: ' + str(tangents_zero_point)
    )
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


def main():
    while True:
        print('--------------------Program do znajdowania miejsca zerowego równań nieliniowych--------------------')
        print('Wybierz rodzaj funkcji: \n1. Pojedyncza\n2. Złożona\n')
        choice = input()
        if choice == '1':
            print('Wybierz funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian')
            function = function_choice()
        elif choice == '2':
            print('Wybierz pierwszą funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian')
            function_1 = function_choice()
            print('Wybierz drugą funkcję: \n1. Trygonometryczna\n2. Wykładnicza\n3. Wielomian')
            function_2 = function_choice()
            function = CompositeFunction.CompositeFunction(function_1, function_2)

        a, b = range_choice()

        print('Wybierz warunek stopu:\n1. Zadana dokładność\n2. Metoda iteracyjna')
        method_choice = input()
        if method_choice == '1':
            print('Podaj epsilon:')
            epsilon = float(input())
            bisection = Bisection.Bisection(a, b, function)
            tangents = Tangents.Tangents(a, b, function)
            result_bisection = bisection.bisection(epsilon)
            result_tangents = tangents.tangents(epsilon)
            print('Miejsce zerowe funkcji obliczone metodą bisekcji: ' + str(result_bisection))
            print('Miejsce zerowe funkcji obliczone metodą stycznych: ' + str(result_tangents))
            plot_function(a, b, function, result_bisection, result_tangents)
        elif method_choice == '2':
            print('Podaj liczbę iteracji:')
            iterations = int(input())
            bisection_iterations = Bisection.Bisection(a, b, function)
            tangents_iterations = Tangents.Tangents(a, b, function)
            result_bisection = bisection_iterations.bisection_iterations(iterations)
            result_tangents = tangents_iterations.tangents_iterations(iterations)
            print('Miejsce zerowe funkcji obliczone metodą bisekcji: ' + str(result_bisection))
            print('Miejsce zerowe funkcji obliczone metodą stycznych: ' + str(result_tangents))
            plot_function(a, b, function, result_bisection, result_tangents)
        else:
            print('Niepoprawny wybór.')

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
