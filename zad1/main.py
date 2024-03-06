import Bisection
import ExponentialFunction
import PolynomialFunction
import SinusFunction
import Tangents

if __name__ == '__main__':
    print('--------------------Program do znajdowania miejsca zerowego równań nieliniowych--------------------')
    print('Wybierz funkcję: \n1. Sinus\n2. Wykładnicza\n3. Wielomian\n3. Funkcja zlozona(nie dziala) \n')
    function_choice = input()
    if function_choice != '1' and function_choice != '2' and function_choice != '3':
        print('Niepoprawny wybór.')
    else:
        print('Podaj początek przedziału a:')
        a = float(input())
        print('Podaj koniec przedziału b:')
        b = float(input())
        if function_choice == '1':
            function = SinusFunction.SinusFunction()
        elif function_choice == '2':
            print('Podaj podstawe funkcji(a):')
            base = float(input())
            function = ExponentialFunction.ExponentialFunction(base)
        elif function_choice == '3':
            print('Podaj stopien wielomianu:')
            degree = int(input())
            print('Podaj wspolczynniki wielomianu od najwyzszego:')
            coefficients = []
            for i in range(degree):
                coefficients.append(float(input()))

            function = PolynomialFunction.PolynomialFunction(coefficients)

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
