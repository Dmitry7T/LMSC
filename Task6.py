#Зиненко Илья
def calc_10_2():
    try:
        n = int(input("Введите число: >> "))
        if n < 0:
            return "Введите положительное число!"
        else:
            return format(n, 'b')
    except:
        return "Введите целое число!"

# print(calc_10_2()) - ВЫЗОВ ФУНКЦИИ