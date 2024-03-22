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
            matrix = np.array(matrix)
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


def get_cofactors_matrix(matrix):
    cofactors_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            multiplier = -1
            for k in range(i + j + 1):
                multiplier *= -1

            reduced_matrix = np.delete(np.delete(matrix, i, 0), j, 1)
            if len(reduced_matrix) == 2:
                cofactor = multiplier * get_2x2_determinant(reduced_matrix)
                cofactors_matrix[i][j] = cofactor
            elif len(reduced_matrix) == 3:
                cofactor = multiplier * get_3x3_determinant(reduced_matrix)
                cofactors_matrix[i][j] = cofactor

    return cofactors_matrix


def get_2x2_determinant(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return determinant


def get_3x3_determinant(matrix):
    determinant = 0
    for i in range(len(matrix)):
        multiplier = matrix[0][i]
        reduced_matrix = np.delete(np.delete(matrix, 0, 0), i, 1)
        if i % 2 == 0:
            determinant += multiplier * get_2x2_determinant(reduced_matrix)
        else:
            determinant -= multiplier * get_2x2_determinant(reduced_matrix)

    return determinant


def get_4x4_determinant(matrix):
    determinant = 0
    for i in range(len(matrix)):
        multiplier = matrix[0][i]
        reduced_matrix = np.delete(np.delete(matrix, 0, 0), i, 1)
        if i % 2 == 2:
            determinant += multiplier * get_3x3_determinant(reduced_matrix)
        else:
            determinant -= multiplier * get_3x3_determinant(reduced_matrix)

    return determinant


def get_adjoint_matrix(matrix):
    cofactors_matrix = get_cofactors_matrix(matrix)
    adjoint_matrix = np.transpose(cofactors_matrix)
    return adjoint_matrix


def get_inverse_matrix(matrix):
    inverse_matrix = np.zeros((len(matrix), len(matrix)))
    adjoint_matrix = get_adjoint_matrix(matrix)
    if len(matrix) == 2:
        det = get_2x2_determinant(matrix)
    elif len(matrix) == 3:
        det = get_3x3_determinant(matrix)
    elif len(matrix) == 4:
        det = get_4x4_determinant(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            inverse_matrix[i][j] = adjoint_matrix[i][j] / det

    return inverse_matrix


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


def get_t_matrix(matrix):
    inverse_diagonal_matrix = get_inverse_matrix(get_diagonal_matrix(matrix))
    lower_triangular_matrix = get_lower_triangular_matrix(matrix)
    upper_triangular_matrix = get_upper_triangular_matrix(matrix)
    lower_triangular_matrix_plus_upper_triangular_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            lower_triangular_matrix_plus_upper_triangular_matrix[i][j] = (
                    lower_triangular_matrix[i][j] + upper_triangular_matrix[i][j]
            )
    t_matrix = np.matmul(inverse_diagonal_matrix, lower_triangular_matrix_plus_upper_triangular_matrix)
    return t_matrix


def get_c_matrix(matrix, b):
    inverse_diagonal_matrix = get_inverse_matrix(matrix)
    c_matrix = np.matmul(inverse_diagonal_matrix, b)
    return c_matrix


def jacobian_iteration(matrix, b, x):
    t_matrix = get_t_matrix(matrix)
    c_matrix = get_c_matrix(matrix, b)
    t_and_x_multiplied = np.matmul(t_matrix, x)
    new_x = np.zeros((len(x), 0))
    for i in range(len(x)):
        new_x[i][0] = t_and_x_multiplied[i][0] + c_matrix[i][0]
    return new_x


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

        # determinant = det_matrix(matrix, num_unknowns)
        # print("Wyznacznik macierzy A:", determinant)

        cofactors_matrix = get_cofactors_matrix(matrix)
        print("Macierz wyznaczników: ")
        print(cofactors_matrix)
        print("Adjoint matrix: ")
        print(get_adjoint_matrix(cofactors_matrix))

        inverse_matrix = get_inverse_matrix(matrix)
        print("Macierz odwrotna: ")
        print(inverse_matrix)

        t_matrix = get_t_matrix(matrix)
        print("Macierz T:")
        print(t_matrix)

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
