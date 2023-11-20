def implication(a, b):
    return min(1, 1 - a + b)


def t_norma(a, b):
    return max(0, a + b - 1)


def supremum(a):
    return max(a)


def main(A, B):
    size = len(A)
    matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(implication(A[i], B[j]))
        matrix.append(line)
    print("1: ", matrix)
    for i in range(size):
        for j in range(size):
            matrix[i][j] = t_norma(matrix[i][j], A[i])
    result = []
    print("2: ", matrix)
    for i in range(size):
        result.append(supremum([matrix[j][i] for j in range(size)]))
    return result
