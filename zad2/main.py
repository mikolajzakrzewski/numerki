import os

import numpy as np


def display_matrix(matrix):
    for row in matrix:
        print(row)


def file_read(filename):
    try:
        with open(filename, 'r') as file:
            num_unknowns = int(file.readline().strip())

            matrix_line = file.readline().strip().split()
            matrix = [list(map(float, matrix_line[i:i + num_unknowns])) for i in
                      range(0, len(matrix_line), num_unknowns)]

            vector = list(map(float, file.readline().strip().split()))

            return num_unknowns, matrix, vector

    except FileNotFoundError:
        print("pliku nie znaleziono.")
        return None
    except ValueError:
        print("blad w danych w pliku")
        return None


def det_matrix(matrix, n):
    what_return = 0
    if n == 1:
        return matrix[0][0]
    else:
        for i in range(n):
            pomocnicza = [row[:i] + row[i + 1:] for row in matrix[1:]]
            if i % 2 == 0:
                what_return += matrix[0][i] * det_matrix(pomocnicza, n - 1)
            else:
                what_return -= matrix[0][i] * det_matrix(pomocnicza, n - 1)
        return what_return


def get_diagonal_matrix(matrix):
    diagonal_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        diagonal_matrix[i][i] = matrix[i][i]

    return diagonal_matrix


def get_lower_triangular_matrix(matrix):
    lower_triangular_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(1, len(matrix)):
        for j in range(0, i):
            lower_triangular_matrix[i][j] = matrix[i][j]

    return lower_triangular_matrix


def get_upper_triangular_matrix(matrix):
    upper_triangular_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix) - 1):
        for j in range(1 + i, len(matrix)):
            upper_triangular_matrix[i][j] = matrix[i][j]

    return upper_triangular_matrix


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

        print("Wymiar macierzy n: ", num_unknowns)

        print("Macierz A: ")
        display_matrix(matrix)

        print("Macierz D")
        diagonal_matrix = get_diagonal_matrix(matrix)
        display_matrix(diagonal_matrix)

        print("Macierz L")
        lower_triangular_matrix = get_lower_triangular_matrix(matrix)
        display_matrix(lower_triangular_matrix)

        print("Macierz U")
        upper_triangular_matrix = get_upper_triangular_matrix(matrix)
        display_matrix(upper_triangular_matrix)

        determinant = det_matrix(matrix, num_unknowns)
        print("Wyznacznik macierzy A:", determinant)

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
