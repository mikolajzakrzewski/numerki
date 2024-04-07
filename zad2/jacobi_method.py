import numpy as np
import matrix_operations as mo


def check_convergence(matrix):
    for i in range(len(matrix)):
        sum_column = 0
        for j in range(len(matrix[0])):
            if j != i:
                sum_column += abs(matrix[i][j])

        if sum_column >= abs(matrix[i][i]):
            return False

    return True


def check_matrix(matrix, b):
    solvable = True
    solutions_number = mo.check_solutions_number(matrix, b)
    if solutions_number == 0:
        print("Układ jest sprzeczny.")
        solvable = False
    elif solutions_number == float('inf'):
        print("Układ jest nieoznaczony")
        solvable = False

    if not check_convergence(matrix):
        print("Układ nie spełnia warunków zbieżności metody Jacobiego.")
        solvable = False

    return solvable


def iteration(matrix, b, x):
    t_matrix = mo.get_t_matrix(matrix)
    c_matrix = mo.get_c_matrix(matrix, b)
    t_and_x_multiplied = np.matmul(t_matrix, x)
    new_x = np.zeros((len(x), 1))
    for i in range(len(x)):
        new_x[i] = t_and_x_multiplied[i] + c_matrix[i]
    return new_x


def solve_iterations(matrix, b, x, iterations):
    if not check_matrix(matrix, b):
        return None

    x_i = x
    for i in range(iterations):
        x_i = iteration(matrix, b, x_i)

    return x_i


def solve_precision(matrix, b, x, precision):
    if not check_matrix(matrix, b):
        return None

    x_i = x
    x_i_1 = iteration(matrix, b, x_i)
    while abs(np.sum(x_i_1) - np.sum(x_i)) > precision:
        x_i = x_i_1
        x_i_1 = iteration(matrix, b, x_i)

    return x_i_1
