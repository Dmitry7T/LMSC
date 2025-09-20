#Задирака Григорий
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
