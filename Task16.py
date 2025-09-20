#Быстров Артём
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
    
def str_showcenter():
    print("Введите строку:")
    s = input()
    space_ = (80 - len(s)) // 2
    return ' ' * space_ + s

def str_words():
    print("Введите строку:")
    s = input()
    h = s.split()
    l1 = len(h)
    h = set(h)
    l2 = len(h)
    return l1, l2    

def str_stat():
   
    # Ввод строки от пользователя
    s = input("Введите строку: ")
    
    # Инициализация счетчиков
    length = len(s)
    digits = 0
    upper = 0
    lower = 0
    whitespace = 0
    
    # Анализ каждого символа в строке
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            whitespace += 1
    
    # Вывод результатов
    print(f"Длина строки: {length}")
    print(f"Количество цифр: {digits}")
    print(f"Количество символов в верхнем регистре: {upper}")
    print(f"Количество символов в нижнем регистре: {lower}")
    print(f"Количество пробельных символов: {whitespace}")

def menu_strings():
    while True:
        num = input("Меню:\n"
              "1. Простые операции со строками\n"
              "2. Строки по центру экрана\n"
              "3. Количество слов и уникальных слов\n"
              "4. Статистика по символам строки\n"
              "5. Выход\n")
        match num:
            case "5":
                return
            case "1":
                print(str_simple_ops())
            case "2":
                print(str_showcenter_op())
            case "3":
                print(*str_words_op())
            case "4":
                print(str_stat_op())

def str_simple_ops():
    return str_simple()
def str_showcenter_op():
    return str_showcenter()
def str_words_op():
    return str_words()
def str_stat_op():
    return str_stat()