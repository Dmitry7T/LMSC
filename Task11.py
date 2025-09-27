# Гусев Иван
import math
from Utils import clear

def menu_numbers():
    while True:
        num = input("Меню:\n"
                    "1. Простые операции\n"
                    "2. Расширенные операции\n"
                    "3. Тригонометрические действия с градусами\n"
                    "4. Тригонометрические действия с радианами\n"
                    "5. Логические операции\n"
                    "6. Перевод чисел в различные СС\n"
                    "7. Проверка скобок\n"
                    "0. Выход\n")
        clear()
        match num:
            case "1":
                calc_simple()
                input()
                clear()
            case "2":
                calc_extended()
                input()
                clear()
            case "3":
                calc_degrees()
                input()
                clear()
            case "4":
                calc_radians()
                input()
                clear()
            case "5":
                calc_logic()
                input()
                clear()
            case "6":
                dec2other()
                clear()
            case "7":
                check_brackets()
                input()
                clear()
            case "0":
                return

def calc_simple():
    try:
        # Ввод данных от пользователя
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        # Выполнение операции в зависимости от введенного символа
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
            result = a / b
        else:
            print("Ошибка: неверная операция! Доступные операции: +, -, *, /")
            return

        # Вывод результата
        print(f"Результат: {a} {operation} {b} = {result}")

    except ValueError:
        print("Ошибка: введите целые числа!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def calc_extended():
    op = int(input("Введите номер операции (1 - возведение в степень, 2 - остаток от деления, 3 - нахождение корня): "))
    if op == 1:
        base = float(input("Введите первое число: "))
        power = float(input("Введите второе число: "))
        result = base ** power
        print(result)
    elif op == 2:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if b == 0:
            print("Ошибка: деление на ноль")
        else:
            print(a % b)
    elif op == 3:
        num = float(input("Введите число: "))
        if num < 0:
            print("Ошибка: корень из отрицательного числа")
        else:
            print(num ** 0.5)
    else:
        print("Ошибка: неверный ввод операции")


def calc_logic():
    print("Выберите операцию:")
    print("1 - AND")
    print("2 - OR")
    print("3 - NOT")

    operation = int(input("Введите номер операции (1-3): "))

    if operation == 1:  # AND
        a = int(input("Введите первое значение (0-False, 1-True): "))
        b = int(input("Введите второе значение (0-False, 1-True): "))
        result = a and b
        print(f"Результат {a} AND {b} = {int(result)}")

    elif operation == 2:  # OR
        a = int(input("Введите первое значение (0-False, 1-True): "))
        b = int(input("Введите второе значение (0-False, 1-True): "))
        result = a or b
        print(f"Результат {a} OR {b} = {int(result)}")

    elif operation == 3:  # NOT
        a = int(input("Введите значение (0-False, 1-True): "))
        result = not a
        print(f"Результат NOT {a} = {int(result)}")

    else:
        print("Ошибка: введите число от 1 до 3")

def dec2other():
    while True:
        num = input("Меню:\n"
                    "1. Перевод 10СИ -> 2СИ\n"
                    "2. Перевод 10СИ -> 16CИ\n"
                    "3. Перевод 10СИ -> 8СИ\n"
                    "0. Выход\n")
        match num:
            case "1":
                print(calc_10_2())
            case "2":
                print(calc_10_16())
            case "3":
                print(calc_10_8())
            case "0":
                return
            case _:
                print("чего прости")
                

def calc_10_2():
    try:
        n = int(input("Введите число: >> "))
        if n < 0:
            return "Введите положительное число!"
        else:
            return format(n, 'b')
    except:
        return "Введите целое число!"

def calc_10_16():
    try:
        n = int(input("Введите число: >> "))
        if n < 0:
            return "Введите положительное число!"
        else:
            return format(n, 'x')
    except:
        return "Введите целое число!"

def calc_10_8():
    try:
        n = int(input("Введите число: >> "))
        if n < 0:
            return "Введите положительное число!"
        else:
            return format(n, 'o')
    except:
        return "Введите целое число!"

def check_brackets():
    formula = input("Введите строку с формулой: ")

    balance = 0

    for char in formula:
        if char == '{':
            balance += 1
        elif char == '}':
            balance -= 1
            if balance < 0:
                print("НЕТ")
                return

    print("ДА" if balance == 0 else "НЕТ")

def calc_degrees():
    print("Номер отвечает за действие, которое будет выполнено")
    print("1 - синус, 2 - косинус")
    x = int(input("Введите номер действия: "))
    deg = int(input("Введите угол в градусах: "))
    if x == 1:
        print(math.sin(deg))
    elif x == 2:
        print(math.cos(deg))
    else:
        print("чего прости")

def calc_radians():
    print("Номер отвечает за действие, которое будет выполнено")
    print("1 - синус, 2 - косинус")
    x = int(input("Введите номер действия: "))
    deg = float(input("Введите угол в радианах: "))
    if x == 1:
        print(math.sin(deg))
    elif x == 2:
        print(math.cos(deg))
    else:
        print("чего прости")
