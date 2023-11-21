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
Прикладные нечёткие системы. Тарэнтэ Т.
"""

from gui import MainWindow
from functions import count_predicate, count_consequence
import ast

NOT_CORRECT_INPUT_PREMISE = "Неверный ввод посылки"
NOT_CORRECT_INPUT_CONSEQUENT = "Неверный ввод консеквента"
NOT_CORRECT_PREDICATE = "Неверный предикат"


def count_consequent_gui():
    try:
        text_C = mw.output_c.get("1.0", "end")
        # Добавим кавычки к ключам словаря, т.к. ключи тоже должны быть строками
        formatted_input_str = text_C.replace("{", "{'").replace(":", "':").replace(", ", ", '")
        # Преобразуем отформатированную строку в словарь
        C = ast.literal_eval(formatted_input_str)
        try:
            text_A_implication_B = mw.output_a_implication_b.get("1.0", "end")
            # Добавим кавычки к ключам словаря, т.к. ключи тоже должны быть строками
            formatted_input_str = text_A_implication_B.replace("{", "{'").replace(":", "':").replace(", ", ", '")
            # Преобразуем отформатированную строку в словарь
            A_implication_B = ast.literal_eval(formatted_input_str)
            text = count_consequence(C, A_implication_B)
        except (Exception, ):
            text = NOT_CORRECT_PREDICATE
    except (Exception, ):
        text = NOT_CORRECT_INPUT_PREMISE
    mw.output_e.delete("1.0", "end")
    mw.output_e.insert("1.0", text)


def count_predicate_gui():
    try:
        text_A = mw.output_a.get("1.0", "end")
        # Добавим кавычки к ключам словаря, т.к. ключи тоже должны быть строками
        formatted_input_str = text_A.replace("{", "{'").replace(":", "':").replace(", ", ", '")
        # Преобразуем отформатированную строку в словарь
        A = ast.literal_eval(formatted_input_str)
        try:
            text_B = mw.output_b.get("1.0", "end")
            # Добавим кавычки к ключам словаря, т.к. ключи тоже должны быть строками
            formatted_input_str = text_B.replace("{", "{'").replace(":", "':").replace(", ", ", '")
            # Преобразуем отформатированную строку в словарь
            B = ast.literal_eval(formatted_input_str)
            text = str(count_predicate(A, B)).replace("'", "").replace('"', '')
        except (Exception,):
            text = NOT_CORRECT_INPUT_CONSEQUENT
    except (Exception, ):
        text = NOT_CORRECT_INPUT_PREMISE
    mw.output_a_implication_b.delete("1.0", "end")
    mw.output_a_implication_b.insert("1.0", text)


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
