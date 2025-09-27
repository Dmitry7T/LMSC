# Гусев Иван
def dec2other():
    while True:
        num = input("Меню:\n"
                    "1. Перевод 10СИ -> 2СИ\n"
                    "2. Перевод 10СИ -> 16CИ\n"
                    "3. Перевод 10СИ -> 8СИ\n"
                    "4. Выход\n")
        match num:
            case "1":
                print(calc_10_2())
            case "2":
                print(calc_10_16())
            case "3":
                print(calc_10_8())
            case "4":
                break
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

dec2other()