#Оруджев Амир
def calc_logic():
    print("Выберите операцию:")
    print("1 - AND")
    print("2 - OR") 
    print("3 - NOT")
    
    operation = int(input("Введите номер операции (1-3): "))
    
    if operation == 1:  # AND
        a = int(input("Введите первое значение (0-False, 1-True): "))
        b = int(input("Введите второе значение (0-False, 1-True): "))
        result = a and b
        print(f"Результат {a} AND {b} = {int(result)}")
        
    elif operation == 2:  # OR
        a = int(input("Введите первое значение (0-False, 1-True): "))
        b = int(input("Введите второе значение (0-False, 1-True): "))
        result = a or b
        print(f"Результат {a} OR {b} = {int(result)}")
        
    elif operation == 3:  # NOT
        a = int(input("Введите значение (0-False, 1-True): "))
        result = not a
        print(f"Результат NOT {a} = {int(result)}")
        
    else:
        print("Ошибка: введите число от 1 до 3")

# Вызов функции
calc_logic()