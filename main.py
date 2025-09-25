# Туровский Дмитрий Романович
# Task21
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

import keyboard
import os
    
class Menu():
    def number_ops(self): #11
        return
    
    def string_ops(self): #16
        from Task16 import menu_strings
        return menu_strings()
    
    def long_ops(): # 20
        return
    
    def team(self): 
        team = ['Ilya', 'zzqqat', 'Sranko0', 'rdrygs999', 'tdimon7', 'Kayaru_376', 'why6not9', 'IvanGusev123']
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
        
    def clear(self):
        if sys.platform.startswith('win'):
            os.system('cls')
        else:
            os.system('clear')



def main():
    menu = Menu()
    
    # Start
    menu.loading()
    menu.output()
    
    while(1):
        key = input()
        if key == "esc":
            break
        
        match key:
            case "0":
                menu.clear()
                menu.output()
            case "1":
                menu.clear()
                menu.number_ops()
            case "2":
                menu.clear()
                menu.string_ops()
                menu.clear()
                menu.output()
            case "3":
                menu.clear()
                menu.long_ops()
            case "4":
                menu.clear()
                menu.team()
        
if __name__ == "__main__":
    main()