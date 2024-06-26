import AbsoluteValue
import SineFunction
import CosineFunction
import TangentFunction
import ExponentialFunction
import PolynomialFunction
import CompositeFunction
import quadratures as qu
import numpy as np
import matplotlib.pyplot as plt


def plot_function(range_start, range_end, function_to_plot):
    x = np.linspace(range_start, range_end, 10000)
    plt.figure(figsize=(8, 8))
    plt.plot(x, function_to_plot.evaluate(x), label='Wykres funkcji f(x)')
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.legend(loc='upper right')
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

        e = float(input('Podaj dokładność: '))

        print('Czy chcesz obliczyć całkę metodą Simpsona na dowolnym przedziale?\n1. Tak\n2. Nie')
        choice = int(input('Wybieram: '))

        if choice == 2:
            a = float(input('Podaj początek przedziału a: '))
            b = float(input('Podaj koniec przedziału b: '))
            print('Metoda Simpsona:')
            print(qu.simpson(a, b, function))
            plot_function(a, b, function)

        else:
            a = 0
            b = 1
            print('Metoda Simpsona:')
            n = 2
            current_integral = qu.composite_simpson(a, b, function, n)
            total_integral = 0
            while abs(current_integral) > e:
                n += 1
                current_integral = qu.simpson(a, b, function)
                total_integral += current_integral
                a = b
                b = b + 1

            print(f'Liczba przedziałów: {n}')
            print(total_integral)
            plot_function(0, 20, function)

        print('Kwadratura Gaussa-Laguerre\'a:')
        for i in range(4):
            print(f'Liczba węzłów: {i + 2} – ', qu.gauss_laguerre(i, function))

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
