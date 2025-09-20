#гусев иван
import math

def calc_radians():
    print("Номер отвечает за действие, которое будет выполнено")
    print("1 - синус, 2 - косинус")
    x = int(input("Введите номер действия: "))
    deg = float(input("Введите угол в радианах: "))
    if x == 1:
        print(math.sin(deg))
    elif x == 2:
        print(math.cos(deg))
    else:
        print("чего прости")



if __name__ == "__main__":
    calc_radians()