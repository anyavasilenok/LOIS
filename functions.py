"""
Лабораторная работа 1 по ЛОИС
Вариант 3: Импликация Лукасевича
Выполнили студенты группы 021702:
        Василёнок Анна Александровна,
        Голяницкий Влвдислав Александрович,
        Рассолько Савва Сергеевич
Дата выполнения: 20.11.2023
Источники:
Нечеткая логика: алгебраические основы и приложения. Блюмин С.Л., Шуйкова И.А., Сараев П.В.
Прикладные нечёткие системы. Тарэнта т.
"""


import numpy as np

NOT_NUMERIC = "Введите численное значение!"
NOT_LIMITED = "Переменные множества должны лежать в промежутке [0, 1]"
NOT_CORRECT = "Переменные множества некорректны"


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


def check_if_correct(A):
    if consist_of_numbers(A):
        if not check_if_limited(A):
            return NOT_LIMITED
    else:
        return NOT_NUMERIC
    return False


def count_predicate(A, B):
    not_correct = check_if_correct(A) or check_if_correct(B)
    if not not_correct:
        predicate = dict()
        for key_a, value_a in A.items():
            for key_b, value_b in B.items():
                predicate.update({f"{key_a}{key_b}": implication(value_a, value_b)})
        return predicate
    else:
        return not_correct


def count_consequence(A, A_implication_B, B):
    not_correct = check_if_correct(A) or check_if_correct(A_implication_B) or check_if_correct(B)
    predicate = dict()
    if not not_correct:
        values_a_b = list(A_implication_B.values())
        values_a = list(A.values())
        size_a = len(A.values())
        size_a_b = len(A_implication_B.values())
        matrix = np.array(values_a_b).reshape(size_a, int(size_a_b/size_a))
        print("1:", matrix)
        for i in range(size_a):
            for j in range(int(size_a_b/size_a)):
                matrix[i][j] = t_norma(matrix[i][j], values_a[i])
        result = []
        print("2:", matrix)
        for i in range(int(size_a_b/size_a)):
            result.append(supremum([matrix[j][i] for j in range(size_a)]))
        keys_b = list(B.keys())
        [predicate.update({f"{keys_b[i]}": result[i]}) for i in range(len(result))]

        return predicate
    else:
        return not_correct

# {x1: 0.9, x2: 0.8}
# {y1: 0.5, y2: 0.7, y3: 0.6}
