# Гусев Иван
def calc_10_8():
    try:
        n = int(input("Введите число: >> "))
        if n < 0:
            return "Введите положительное число!"
        else:
            return format(n, 'o')
    except:
        return "Введите целое число!"

print(calc_10_8())