def simpson(a, b, function):
    h = (b - a) / 2
    result = h / 3 * (function.evaluate(a) +
                      4 * function.evaluate(a + h) +
                      function.evaluate(b))
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
    weights = [
        [0.853553, 0.146447, 0, 0, 0],
        [0.711093, 0.278518, 0.0103893, 0, 0],
        [0.603154, 0.357419, 0.0388879, 0.000539295, 0],
        [0.521756, 0.398667, 0.0759424, 0.00361176, 0.00002337]
    ]

    nodes = [
        [0.585786, 3.41421, 0, 0, 0],
        [0.415775, 2.29428, 6.28995, 0, 0],
        [0.322548, 1.74576, 4.53662, 9.39507, 0],
        [0.26356, 1.4134, 3.59643, 7.08581, 12.6408]
    ]

    result = 0
    # TODO: calculate result
    return result
