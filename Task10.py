#Оруджев Амир
def check_brackets():
    formula = input("Введите строку с формулой: ")
    
    balance = 0
    
    for char in formula:
        if char == '{':
            balance += 1
        elif char == '}':
            balance -= 1
            if balance < 0:
                print("НЕТ")
                return
    
    print("ДА" if balance == 0 else "НЕТ")

check_brackets()