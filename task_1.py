# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

day_num = int(input("enter a number of day: "))
if day_num > 0 and day_num < 6:
    print("weekday")
elif day_num >= 6 and day_num < 8:
    print("day off")
else: print("there is no such day")