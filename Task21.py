# Туровский Дмитрий Романович
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

from Utils import clear
    
class Menu():
    def number_ops(self): #11
        from Task11 import menu_numbers
        try:
            return menu_numbers()
        except:
            print("Упс! Что то пошло не так")
            input()
            return
    
    def string_ops(self): #16
        from Task16 import menu_strings
        try:
            return menu_strings()
        except:
            print("Упс! Что то пошло не так")
            input()
            return
    
    def long_ops(self): # 20
        from Task20 import menu_long
        try:
            return menu_long()
        except:
            print("Упс! Что то пошло не так")
            input()
            return
    
    def team(self): 
        team = [' Ilya\n', 'zzqqat\n', 'Sranko0\n', 'rdrygs999\n', 'tdimon7\n', 'Kayaru_376\n', 'why6not9\n', 'IvanGusev123']
        print(*team[::], flush= True)
        return
    
    def loading(self):
        return

    def output(self):
        clear()
        print('_' * 8, "LMSC", '_' * 8, flush= True)

        print("1. Калькулятор чисел", flush= True)
        print("2. Калькулятор строк", flush= True)
        print("3. Длинная арифметика", flush= True)
        print("4. Команда разработчиков", flush= True)
        print("esc - выход", flush= True)

        print('_' * 22, flush= True)
        return
        


def main():
    menu = Menu()
    
    # Start
    menu.loading()
    menu.output()
    
    while(1):
        try:
            key = input()
            if key == "esc":
                clear()
                break
        except:
            key = ''
        
        match key:
            case "0":
                menu.output()
            case "1":
                clear()
                menu.number_ops()
                menu.output()
            case "2":
                clear()
                menu.string_ops()
                menu.output()
            case "3":
                clear()
                menu.long_ops()
                menu.output()
            case "4":
                clear()
                menu.team()
                try:
                    input()
                except:
                    continue
                menu.output()
            case _:
                menu.output()

        
if __name__ == "__main__":
    main()