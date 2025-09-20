#Зиненко Илья
def calc_10_16():
    try:
        n = int(input("Введите число: >> "))
        if n < 0:
            return "Введите положительное число!"
        else:
            return hex(n) # если 0x в начале не нужен, заменить на format(n, 'x')
    except:
        return "Введите целое число!"

# print(calc_10_16()) - ВЫЗОВ ФУНКЦИИ