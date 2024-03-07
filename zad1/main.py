import Bisection
import ExponentialFunction
import PolynomialFunction
import SinusFunction
import Tangents
import CompositeFunction


def function_choice():
    chosen_function = input()
    if chosen_function == '1':
        return SinusFunction.SinusFunction()
    elif chosen_function == '2':
        print('Podaj podstawe funkcji(a):')
        base = float(input())
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


if __name__ == '__main__':
    print('--------------------Program do znajdowania miejsca zerowego równań nieliniowych--------------------')
    print('Wybierz rodzaj funkcji: \n1. Pojedyncza\n2. Złożona\n')
    choice = input()
    if choice == '1':
        print('Wybierz funkcję: \n1. Sinus\n2. Wykładnicza\n3. Wielomian')
        function = function_choice()
    elif choice == '2':
        print('Wybierz pierwszą funkcję: \n1. Sinus\n2. Wykładnicza\n3. Wielomian')
        function_1 = function_choice()
        print('Wybierz drugąfunkcję: \n1. Sinus\n2. Wykładnicza\n3. Wielomian')
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
    elif method_choice == '2':
        print('Podaj liczbę iteracji:')
        iterations = int(input())
        bisection_iterations = Bisection.Bisection(a, b, function)
        tangents_iterations = Tangents.Tangents(a, b, function)
        result_bisection = bisection_iterations.bisection_iterations(iterations)
        result_tangents = tangents_iterations.tangents_iterations(iterations)
        print('Miejsce zerowe funkcji obliczone metodą bisekcji: ' + str(result_bisection))
        print('Miejsce zerowe funkcji obliczone metodą stycznych: ' + str(result_tangents))
    else:
        print('Niepoprawny wybór.')
