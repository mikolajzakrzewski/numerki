import os

import numpy as np
import matrix_operations as mo


def file_read(filename):
    # try:
    with open(filename, 'r') as file:
        num_unknowns = int(file.readline().strip())

        matrix_line = file.readline().strip().split()
        matrix = [list(map(float, matrix_line[i:i + num_unknowns])) for i in
                  range(0, len(matrix_line), num_unknowns)]

        vector = list(map(float, file.readline().strip().split()))
        vector = np.array(vector)
        matrix = np.array(matrix)
        return num_unknowns, matrix, vector

    # except FileNotFoundError:
    #     print("Pliku nie znaleziono.")
    #     return None
    # except ValueError:
    #     print("Błąd w danych w pliku")
    #     return None


def jacobian_iteration(matrix, b, x):
    t_matrix = mo.get_t_matrix(matrix)
    c_matrix = mo.get_c_matrix(matrix, b)
    t_and_x_multiplied = np.matmul(t_matrix, x)
    new_x = np.zeros((len(x), 1))
    for i in range(len(x)):
        new_x[i] = t_and_x_multiplied[i] + c_matrix[i]
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
        mo.display_matrix(matrix)

        print("Macierz D")
        diagonal_matrix = mo.get_diagonal_matrix(matrix)
        mo.display_matrix(diagonal_matrix)

        print("Macierz L")
        lower_triangular_matrix = mo.get_lower_triangular_matrix(matrix)
        mo.display_matrix(lower_triangular_matrix)

        print("Macierz U")
        upper_triangular_matrix = mo.get_upper_triangular_matrix(matrix)
        mo.display_matrix(upper_triangular_matrix)

        det = mo.get_determinant(matrix)
        print("Wyznacznik macierzy A:", det)

        cofactors_matrix = mo.get_cofactors_matrix(matrix)
        print("Macierz wyznaczników: ")
        print(cofactors_matrix)
        print("Adjoint matrix: ")
        print(mo.get_adjoint_matrix(cofactors_matrix))

        inverse_matrix = mo.get_inverse_matrix(matrix)
        print("Macierz odwrotna: ")
        print(inverse_matrix)

        t_matrix = mo.get_t_matrix(matrix)
        print("Macierz T:")
        print(t_matrix)

        x = np.zeros(len(vector))
        print(x)
        print(vector)
        x1 = jacobian_iteration(matrix, vector, x)

        for i in range(1000):
            x1 = jacobian_iteration(matrix, vector, x1)
        print(x1)

        cont = input("Czy chcesz kontynuować? (T/N): ")
        if cont.upper() != 'T':
            break


if __name__ == '__main__':
    main()
