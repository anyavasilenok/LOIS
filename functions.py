"""
Лабораторная работа 1 по ЛОИС
Вариант 3: Импликация Лукасевича
Выполнили студенты группы 021702:
        Василёнок Анна Александровна,
        Голяницкий Влвдислав Александрович,
        Рассолько Савва Сергеевич
Дата выполнения: 20.11.2023
Источники:
"""


import numpy as np

NOT_NUMERIC = "Введите численное значение!"
NOT_LIMITED = "Переменные множества должны лежать в промежутке [0, 1]"


def implication(a, b):
    return min(1, 1 - a + b)


def t_norma(a, b):
    return max(0, a + b - 1)


def supremum(a):
    return max(a)


def consist_of_numbers(my_dict):
    for value in my_dict.values():
        try:
            float(value)
        except ValueError:
            return False
    return True


# лежат ли числа из словаря в промежутке [0, 1]
def check_if_limited(my_dict):
    for i in my_dict.values():
        if not 0 <= i <= 1:
            return False
    return True


def check_if_correct(A, B):
    if consist_of_numbers(A):
        if not check_if_limited(A):
            return NOT_LIMITED
    else:
        return NOT_NUMERIC

    if consist_of_numbers(B):
        if not check_if_limited(B):
            return NOT_LIMITED
    else:
        return NOT_NUMERIC
    return False


def count_predicate(A, B):
    not_correct = check_if_correct(A, B)
    if not not_correct:
        predicate = dict()
        for key_a, value_a in A.items():
            for key_b, value_b in B.items():
                predicate.update({f"{key_a}{key_b}": implication(value_a, value_b)})
        return predicate
    else:
        return not_correct


def count_consequence(A, A_implication_B: dict):
    not_correct = check_if_correct(A, A_implication_B)
    predicate = dict()
    if not not_correct:
        values_a_b = list(A_implication_B.values())
        values_a = list(A.values())
        size_a = len(A.values())
        size_a_b = len(A_implication_B.values())
        matrix = np.array(values_a_b).reshape(size_a, int(size_a_b/size_a))
        print(matrix)
        for i in range(size_a):
            for j in range(int(size_a_b/size_a)):
                matrix[i][j] = t_norma(matrix[i][j], values_a[i])
        result = []
        print("2: ", matrix)
        for i in range(int(size_a_b/size_a)):
            result.append(supremum([matrix[j][i] for j in range(size_a)]))
        return result
    else:
        return not_correct


    # for i in range(size):
    #     for j in range(size):
    #         matrix[i][j] = t_norma(matrix[i][j], A[i])
    # not_correct = check_if_correct(A, A_implication_B)
    # predicate = dict()
    # my_list = []
    # if not not_correct:
    #     values_a = A.values()
    #     values_a_b = A_implication_B.values()
    #     for i in range(len(A.values())):
    #         my_list.append(values_a[i] * values_a_b[i])
    #     return my_list
    # else:
    #     return not_correct

    # not_correct = check_if_correct(A, A_implication_B)
    # predicate = dict()
    # if not not_correct:
    #     for key_a, value_a in A.items():
    #         # tem
    #         key_list = A_implication_B.keys()
    #         key_values = []
    #         for key in key_list:
    #             if re.match(key_a, key):
    #                 key_values.append(t_norma(value_a, A_implication_B.get(key)))
    #         predicate.update({key_a: min(key_values)})
    #     print(predicate)
    #     return predicate
    # else:
    #     return not_correct


# {x1: 0.9, x2: 0.8}
# {y1: 0.5, y2: 0.7, y3: 0.6}
