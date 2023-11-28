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

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("835x396")
        self.window.configure(bg="#7CBBC3")

        self.canvas = Canvas(
            self.window,
            bg="#7CBBC3",
            height=396,
            width=835,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        # Вывод посылки А
        self.output_a = Text(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15)
        )
        self.output_a.place(
            x=115.0,
            y=26.0,
            width=557.0,
            height=34.0,
        )

        # Вывод консеквента В
        self.output_b = Text(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15)
        )
        self.output_b.place(
            x=115.0,
            y=80.0,
            width=557.0,
            height=34.0,
        )

        # Вывод A ~> B
        self.output_a_implication_b = Text(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15)
        )
        self.output_a_implication_b.place(
            x=115.0,
            y=134.0,
            width=701.0,
            height=34.0,
        )

        self.canvas.create_text(
            19.0,
            29.0,
            anchor="nw",
            text="A:",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            19.0,
            137.0,
            anchor="nw",
            text="A ~> B:",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            19.0,
            84.0,
            anchor="nw",
            text="B:",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            188.0,
            835.0,
            396.0,
            fill="#457B82",
            outline=""
        )

        # Кнопка вычислить предикат
        self.button_image_count_predicate = PhotoImage(file="pictures\\count_predicate.png")
        self.button_count_predicate = Button(
            image=self.button_image_count_predicate,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_count_predicate.place(
            x=685.0,
            y=21.0,
            width=136.0,
            height=100.0
        )

        # Кнопка вычислить консеквент Е
        self.button_image_count_consequent = PhotoImage(file="pictures/count_consequent.png")
        self.button_count_consequent = Button(
            image=self.button_image_count_consequent,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_count_consequent.place(
            x=115.0,
            y=252.0,
            width=701.0,
            height=57.0
        )

        # Вывод посылки C
        self.output_c = Text(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15)
        )
        self.output_c.place(
            x=115.0,
            y=210.0,
            width=701.0,
            height=34.0,
        )

        # Вывод консеквента E
        self.output_e = Text(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15)
        )
        self.output_e.place(
            x=115.0,
            y=319.0,
            width=701.0,
            height=34.0,
        )

        self.canvas.create_text(
            19.0,
            213.0,
            anchor="nw",
            text="C:",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            19.0,
            321.0,
            anchor="nw",
            text="E:",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.window.resizable(False, False)
