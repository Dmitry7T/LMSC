#Зиненко Илья
def str_simple():
    operation = input("Введите строку с операцией: ")
    if operation == "+":
        string1 = input("Введите первую строку: ")
        string2 = input("Введите вторую строку: ")
        return string1 + string2
    elif operation == "*":
        string1 = input("Введите строку: ")

        try:
            num = int(input("Введите число, на которое нужно умножить строку: "))
            if num > 0:
                return string1 * num
            else:
                return "Введите целое и положительное число"
        except:
            return "Введите целое и положительное число"
    else:
        return "Выбрана неверная операция!"

# print(str_simple()) - вызов функции