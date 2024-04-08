import os

import numpy as np

import jacobi_method


def file_read(filename):
    with open(filename, 'r') as file:
        num_unknowns = int(file.readline().strip())

        matrix_line = file.readline().strip().split()
        matrix = [list(map(float, matrix_line[i:i + num_unknowns])) for i in
                  range(0, len(matrix_line), num_unknowns)]

        vector = list(map(float, file.readline().strip().split()))
        vector = np.array(vector)
        matrix = np.array(matrix)
        return num_unknowns, matrix, vector


def manual_matrix_input():
    print("Wprowadź wymiar macierzy:")
    num_unknowns = int(input())
    matrix = np.zeros([num_unknowns, num_unknowns])

    for i in range(num_unknowns):
        print("Wprowadź wartości elementów " + str(i + 1) + " rzędu macierzy oddzielone spacjami:")
        matrix_input = [float(x) for x in input().split()]
        matrix[i] = matrix_input

    vector = [float(x) for x in input("Wprowadź wektor wynikowy oddzielony spacjami: ").split()]

    return num_unknowns, np.array(matrix), np.array(vector)


def main():
    while True:
        print('--------------------Program do rozwiazywania układu N równań liniowych z N niewiadomymi '
              'metodą iteracyjną Jacobiego--------------------')

        print('Wybierz opcję:')
        print('1. Wybierz plik z układem równań')
        print('2. Wprowadź własną macierz')
        choice = input()

        if choice == '1':
            filename = input("Wybierz plik z układem równań - [a,b,c,d,e,f,g,h,i,j]: ") + ".txt"
            print("Wybrany plik:", filename)
            if not os.path.exists(filename):
                print("Plik nie istnieje, wpisz jeszcze raz")
                continue
            data = file_read(filename)
            num_unknowns, matrix, vector = data
            x = np.zeros(len(vector))

        elif choice == '2':
            data = manual_matrix_input()
            num_unknowns, matrix, vector = data
            x = np.zeros(len(vector))
        else:
            print('Niepoprawny wybór. Wybierz jeszcze raz.')
            continue

        print('Wybrana macierz:')
        print(matrix)
        print('Wektor rozwiązań:')
        print(vector)
        print('Wybierz warunek stopu:\n1. Zadana dokładność\n2. Metoda iteracyjna')
        while True:
            method_choice = input()
            if method_choice == '1':
                print('Podaj epsilon:')
                epsilon = float(input())
                result_epsilon = jacobi_method.solve_precision(matrix, vector, x, epsilon)
                if result_epsilon is not None:
                    print("Wektor rozwiązań:")
                    print(result_epsilon)
                break

            elif method_choice == '2':
                print('Podaj liczbę iteracji:')
                iterations = int(input())
                result_iterations = jacobi_method.solve_iterations(matrix, vector, x, iterations)
                if result_iterations is not None:
                    print("Wektor rozwiązań:")
                    print(result_iterations)
                break
            else:
                print('Niepoprawny wybór. Wybierz jeszcze raz.')

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
