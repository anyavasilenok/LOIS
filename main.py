"""
Лабораторная работа 1 по ЛОИС
Вариант 3: Импликация Лукасевича
Выполнили студенты группы 021702:
        Василёнок Анна Александровна,
        Голяницкий Влвдислав Александрович,
        Расолько Савва Сергеевич
Дата выполнения: 20.11.2023
Источники:
Нечеткая логика: алгебраические основы и приложения. Блюмин С.Л., Шуйкова И.А., Сараев П.В.
Прикладные нечёткие системы. Тарэнта т.
"""

from gui import MainWindow
from functions import count_predicate, count_consequence

NOT_CORRECT_INPUT_PREMISE = "Неверный ввод посылки"
NOT_CORRECT_INPUT_CONSEQUENT = "Неверный ввод консеквента"
NOT_CORRECT_PREDICATE = "Неверный предикат"
NOT_SAME_LENGTH = "Посылки разной длины"

A = dict()
B = dict()
A_implication_B = dict()


# Преобразовать строку в словарь
def convert_in_dict(input_str):
    my_dict = {}
    input_str = input_str.replace("{", "").replace("}", "")
    for pair in input_str[0:-1].split(','):
        key, value = pair.split(':')
        key = key.strip()
        if key in my_dict:
            raise (Exception, )
        try:
            my_dict[key] = float(value)
        except (Exception, ):
            raise Exception
    return my_dict


# Обработка ввода (удаление пробелов, преобразование в словарь)
def process_input(text):
    formatted_input_str = text.replace(" ", "")
    my_set = convert_in_dict(formatted_input_str)
    return my_set


# Высчитать консеквент (интерфейс)
def count_consequent_gui():
    global A, B, A_implication_B
    try:
        text_C = mw.output_c.get("1.0", "end")
        C = process_input(text_C)

        try:
            if len(A) != len(C):
                raise Exception

            try:
                try:
                    text = str(count_consequence(C, A_implication_B, B)).replace("'", "").replace('"', '')
                except (Exception,):
                    text = NOT_CORRECT_PREDICATE

            except (Exception, ):
                text = NOT_CORRECT_INPUT_CONSEQUENT

        except (Exception, ):
            text = NOT_SAME_LENGTH

    except (Exception, ):
        text = NOT_CORRECT_INPUT_PREMISE
    mw.output_e.delete("1.0", "end")
    mw.output_e.insert("1.0", text)


# Высчитать предикат (интерфейс)
def count_predicate_gui():
    global A, B, A_implication_B
    try:
        text_A = mw.output_a.get("1.0", "end")
        A = process_input(text_A)
        try:
            text_B = mw.output_b.get("1.0", "end")
            B = process_input(text_B)

            A_implication_B = count_predicate(A, B)
            text = str(A_implication_B).replace("'", "").replace('"', '')

        except (Exception,):
            text = NOT_CORRECT_INPUT_CONSEQUENT

    except (Exception, ):
        text = NOT_CORRECT_INPUT_PREMISE

    mw.output_a_implication_b.delete("1.0", "end")
    mw.output_a_implication_b.insert("1.0", text)
    print(A, B)


def delete_text(widget):
    widget.delete("1.0", "end")


if __name__ == "__main__":
    mw = MainWindow()
    mw.canvas.focus_set()
    mw.button_count_consequent.bind("<Button-1>", lambda event: count_consequent_gui())
    mw.button_count_predicate.bind("<Button-1>", lambda event: count_predicate_gui())
    mw.output_a.bind("<KeyPress-Delete>", lambda event: delete_text(mw.output_a))
    mw.output_b.bind("<KeyPress-Delete>", lambda event: delete_text(mw.output_b))
    mw.output_c.bind("<KeyPress-Delete>", lambda event: delete_text(mw.output_c))
    mw.output_a_implication_b.bind("<KeyPress-Delete>", lambda event: delete_text(mw.output_a_implication_b))
    mw.output_e.bind("<KeyPress-Delete>", lambda event: delete_text(mw.output_e))
    mw.window.mainloop()
