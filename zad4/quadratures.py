import numpy as np


def simpson(a, b, function):
    h = (b - a) / 2
    result = h / 3 * (function.evaluate(a) * np.exp(-a) +
                      4 * function.evaluate(a + h) * np.exp(-(a + h)) +
                      function.evaluate(b) * np.exp(-b))
    return result


def composite_simpson(a, b, function, n):
    result = 0
    h = (b - a) / n
    for i in range(n):
        x = a + i * h
        x_1 = a + (i + 1) * h
        result += simpson(x, x_1, function)

    return result


def gauss_laguerre(n, function):
    weights = []
    nodes = []
    with open('laguerre.txt', 'r') as f:
        i = 2
        j = 0
        temp_weights = []
        temp_nodes = []
        for line in f:
            if line.startswith('n') or line.strip() == '':
                continue

            else:
                values = line.strip().split()
                temp_weights.append(float(values[0]))
                temp_nodes.append(float(values[1]))
                j += 1
                if j == i:
                    weights.append(temp_weights.copy())
                    temp_weights.clear()
                    nodes.append(temp_nodes.copy())
                    temp_nodes.clear()
                    i += 1
                    j = 0

    result = 0
    for i in range(n + 2):
        result += weights[n][i] * function.evaluate(nodes[n][i])

    return result
