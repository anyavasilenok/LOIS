from functions import main

NOTNUMERIC = "Введите численное значение!"
NOTCORRECT = "Неверный ввод!"
NOTEQUAL = "Можества различной длины!"
NOTLIMITED = "Переменные множества должны лежать в промежутке [0, 1]"


def consist_of_numbers(lst):
    for value in lst:
        try:
            float(value)
        except ValueError:
            return False
    return True


def check(my_list):
    for i in my_list:
        if not 0 <= i <= 1:
            return False
    return True


if __name__ == "__main__":
    while True:
        choice = input("1 - ввести значения\n2 - выход\n")
        if choice == "1":
            while True:
                A = input("A: ").split()
                if consist_of_numbers(A):
                    A = list(map(float, A))
                    if not check(A):
                        print(NOTLIMITED)
                    else:
                        break
                else:
                    print(NOTNUMERIC)
            while True:
                B = input("B: ").split()
                if consist_of_numbers(B):
                    if len(A) == len(B):
                        B = list(map(float, B))
                        if not check(B):
                            print(NOTLIMITED)
                        else:
                            break
                    else:
                        print(NOTEQUAL)
                else:
                    print(NOTNUMERIC)
            result = main(A, B)
            print("A ~> B:", *result)
        elif choice == "2":
            break
        else:
            print(NOTCORRECT)

