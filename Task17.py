# Зиненко Илья
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