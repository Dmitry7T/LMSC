#Гордеев Артём
def calc_simple():
    
    try:
        # Ввод данных от пользователя
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        
        # Выполнение операции в зависимости от введенного символа
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
            result = a / b
        else:
            print("Ошибка: неверная операция! Доступные операции: +, -, *, /")
            return
        
        # Вывод результата
        print(f"Результат: {a} {operation} {b} = {result}")
        
    except ValueError:
        print("Ошибка: введите целые числа!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    calc_simple()