# Туровский Дмитрий Романович
# Task21
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

from Utils import clear
    
class Menu():
    def number_ops(self): #11
        return
    
    def string_ops(self): #16
        from Task16 import menu_strings
        return menu_strings()
    
    def long_ops(self): # 20
        clear()
        return
    
    def team(self): 
        team = [' Ilya\n', 'zzqqat\n', 'Sranko0\n', 'rdrygs999\n', 'tdimon7\n', 'Kayaru_376\n', 'why6not9\n', 'IvanGusev123']
        print(*team[::], flush= True)
        return
    
    def loading(self):
        return

    def output(self):
        print('_' * 8, "LMSC", '_' * 8, flush= True)

        print("1. Калькулятор чисел", flush= True)
        print("2. Калькулятор строк", flush= True)
        print("3. Длинная арифметика", flush= True)
        print("4. Команда разработчиков", flush= True)

        print('_' * 22, flush= True)
        return
        


def main():
    menu = Menu()
    
    # Start
    menu.loading()
    menu.output()
    
    while(1):
        key = input()
        if key == "esc":
            clear()
            break
        
        match key:
            case "0":
                clear()
                menu.output()
            case "1":
                clear()
                menu.number_ops()
            case "2":
                clear()
                menu.string_ops()
                clear()
                menu.output()
            case "3":
                clear()
                menu.long_ops()
            case "4":
                clear()
                menu.team()
        
if __name__ == "__main__":
    main()