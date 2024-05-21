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
    result = h / 3 * (function(a) * np.exp(-a ** 2) +
                      4 * function(a + h) * np.exp(-(a + h) ** 2) +
                      function(b) * np.exp(-b ** 2))
    return result


def composite_simpson(a, b, function, n):
    result = 0
    h = (b - a) / n
    for i in range(n):
        x = a + i * h
        x_1 = a + (i + 1) * h
        result += simpson(x, x_1, function)

    return result


def get_hermite_coefficient(k, x):
    if k == 0:
        return 1
    elif k == 1:
        return 2 * x
    else:
        nodes = [1, 2 * x]
        for i in range(2, k + 1):
            nodes.append(2 * x * nodes[i - 1] - 2 * (i - 1) * nodes[i - 2])

        return nodes[k]


def get_approximation_coefficients(a, b, function, degree, n):
    coefficients = [((composite_simpson(a, b, lambda x: function.evaluate(x) * get_hermite_coefficient(k, x), n)) /
                     (composite_simpson(a, b, lambda x: get_hermite_coefficient(k, x) ** 2, n)))
                    for k in range(degree + 1)]

    return coefficients


def approximate(coefficients, x):
    result = 0
    for k in range(len(coefficients)):
        result += coefficients[k] * get_hermite_coefficient(k, x)

    return result


def approximation_error(func, approx_func, a, b, n):
    error = composite_simpson(a, b, lambda x: (func.evaluate(x) - approx_func(x)) ** 2, n)
    return np.sqrt(error)


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
        choice = input('Wybierz tryb pracy:\n'
                       '1. Aproksymacja dla zadanego stopnia wielomianu aproksymacyjnego\n'
                       '2. Aproksymacja dla oczekiwanego błędu aproksymacji\n')
        if choice == '1':
            degree = int(input('Podaj stopień wielomianu aproksymacyjnego: '))
            num_ranges = int(input('Podaj liczbę podprzedziałów do obliczania całki złożoną kwadraturą Simpsona: '))
            coefficients = get_approximation_coefficients(a, b, function, degree, num_ranges)
            calculated_error = approximation_error(function, lambda x: approximate(coefficients, x), a, b, num_ranges)
        else:
            degree = 1
            num_ranges = int(input('Podaj liczbę podprzedziałów do obliczania całki złożoną kwadraturą Simpsona: '))
            desired_error = float(input('Oczekiwany błąd aproksymacji: '))
            coefficients = get_approximation_coefficients(a, b, function, degree, num_ranges)
            calculated_error = approximation_error(function, lambda x: approximate(coefficients, x), a, b, num_ranges)
            while calculated_error > desired_error:
                degree += 1
                coefficients = get_approximation_coefficients(a, b, function, degree, num_ranges)
                calculated_error = approximation_error(function, lambda x: approximate(coefficients, x), a, b, num_ranges)

        print(f'Stopień wielomianu aproksymacyjnego: {degree}')
        print(f'Współczynniki wielomianu Hermite\'a: {coefficients}')
        print(f'Błąd aproksymacji: {calculated_error}')

        x = np.linspace(a, b, 400)
        y = np.array([function.evaluate(xi) for xi in x])
        y_approx = np.array([approximate(coefficients, xi) for xi in x])

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
