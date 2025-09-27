# Быстров Артем
from Utils import clear
def long_sub():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    for i in range(len(num1)):
        if (ord(num1[i]) >= 48 and ord(num1[i]) <= 57) and ord(num1[i]) != 45:
            pass
        else:
            return "Введите целые положительные числа"
    for i in range(len(num2)):
        if (ord(num2[i]) >= 48 and ord(num2[i]) <= 57) and ord(num2[i]) != 45:
            pass
        else:
            return "Введите целые положительные числа"
    digits1 = list(map(int, num1))
    digits2 = list(map(int, num2))

    def compare_lists(a, b):
        if len(a) != len(b):
            return len(a) - len(b)
        for x, y in zip(a, b):
            if x != y:
                return x - y
        return 0

    cmp = compare_lists(digits1, digits2)
    negative = False
    if cmp < 0:
        digits1, digits2 = digits2, digits1
        negative = True
    max_len = max(len(digits1), len(digits2))
    digits1 = [0] * (max_len - len(digits1)) + digits1
    digits2 = [0] * (max_len - len(digits2)) + digits2
    result = []
    sdwig = 0
    for i in range(max_len - 1, -1, -1):
        diff = digits1[i] - digits2[i] - sdwig
        if diff < 0:
            diff += 10
            sdwig = 1
        else:
            sdwig = 0
        result.append(diff)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    result.reverse()
    res_str = ''.join(map(str, result))
    if negative:
        res_str = '-' + res_str
    return res_str

# print(long_sub()) - ВЫЗОВ ФУНКЦИИ

def long_add():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    for i in range(len(num1)):
        if (ord(num1[i]) >= 48 and ord(num1[i]) <= 57) and ord(num1[i]) != 45:
            pass
        else:
            return "Введите целые положительные числа"
    for i in range(len(num2)):
        if (ord(num2[i]) >= 48 and ord(num2[i]) <= 57) and ord(num2[i]) != 45:
            pass
        else:
            return "Введите целые положительные числа"
    digits1 = list(map(int, num1))
    digits2 = list(map(int, num2))
    max_len = max(len(digits1), len(digits2))
    digits1 = [0] * (max_len - len(digits1)) + digits1
    digits2 = [0] * (max_len - len(digits2)) + digits2
    result = []
    perebros = 0
    for i in range(max_len - 1, -1, -1):
        s = digits1[i] + digits2[i] + perebros
        result.append(s % 10)
        perebros = s // 10
    if perebros:
        result.append(perebros)
    result.reverse()
    return ''.join(map(str, result))

# print(long_add()) - ВЫЗОВ ФУНКЦИИ

def menu_long():
    while True:
        n = input("Меню:\n"
            "1. Сложение\n"
            "2. Вычитание\n"
            "3. Умножение\n"
            "0. Выход\n")
        clear()
        match n:
            case '0':
                return
            case '1':
                print(long_add_op())
                input()
                clear()
            case '2':
                print(long_sub_op())
                input()
                clear()
            case '3':
                print(long_mul_op())
                input()
                clear()

def long_add_op():
    return long_add()
def long_sub_op():
    return long_sub()
def long_mul_op():     
    from Task19 import long_multiply
    return long_multiply()