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


import re

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
        for key_a, value_a in A.items():
            # tem
            key_list = A_implication_B.keys()
            key_values = []
            for key in key_list:
                if re.match(key_a, key):
                    key_values.append(t_norma(value_a, A_implication_B.get(key)))
            predicate.update({key_a: min(key_values)})
        print(predicate)
        return predicate
    else:
        return not_correct
