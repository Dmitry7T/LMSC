#Гордеев Артём
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


if __name__ == "__main__":
    str_stat()