#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    num = int(input("Введите номер четверти: "))
    if num < 1 or num > 4:
        print("номер должен быть от 1 до 4")
    else: break

if num == 1:
    print("x > 0 and y > 0")
elif num == 2:
    print("x < 0 and y > 0")
elif num == 3:
    print("x < 0 and y < 0")
elif num == 4:
    print("x > 0 and y < 0")