import os

import numpy as np

import jacobi_method
import matrix_operations as mo
import jacobi_method as jm


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


def main():
    while True:
        print('--------------------Program do rozwiazywania układu N równań liniowych z N niewiadomymi '
              'metodą iteracyjną Jacobiego--------------------')

        filename = input("wybierz plik z układem równań - [a,b,c,d,e,f,g,h,i,j]: ") + ".txt"
        print("wybrany plik:", filename)

        if not os.path.exists(filename):
            print("plik nie istnieje, wpisz jeszcze raz")
            continue

        data = file_read(filename)

        if data is None:
            continue

        num_unknowns, matrix, vector = data

        x = np.zeros(len(vector))

        print('Wybierz warunek stopu:\n1. Zadana dokładność\n2. Metoda iteracyjna')
        while True:
            method_choice = input()
            if method_choice == '1':
                print('Podaj epsilon:')
                epsilon = float(input())
                result_epsilon = jacobi_method.solve_precision(matrix, vector, x, epsilon)
                if result_epsilon is not None:
                    print("Wynik: Macierz x: ")
                    print(result_epsilon)
                break

            elif method_choice == '2':
                print('Podaj liczbę iteracji:')
                iterations = int(input())
                result_iterations = jacobi_method.solve_iterations(matrix, vector, x, iterations)
                if result_iterations is not None:
                    print("Wynik: Macierz x: ")
                    print(result_iterations)
                break
            else:
                print('Niepoprawny wybór. Wybierz jeszcze raz.')

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
