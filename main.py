# print('Podaj imie')
# name = input()
# print('Siema  ' + name)
#
# print('Podaj a')
# a = int(input())
# print('Podaj b')
# b = int(input())
# sum = int(a + b)
# print(float(sum))
#
# suma = 0
# zakres = int(input())
# for i in range(0, zakres):
#     liczba = int(input())
#     suma += liczba
#     print(f"suma: {suma}")
#
# print(sum([int(x) for x in (input("podaj liczby oddzielnie:").split())]))
#
# print(sum(range(8, 81)))
#
# print(range(80, 8, -2))
#
# import datetime
#
# date = datetime.datetime.now()
# print(date)
# x = int(input("ROK"))
# y = int(input("miesiac"))
# z = int(input("dzień"))
#
# date1 = datetime.date(2024, 2, 28)
# date2 = datetime.date(x, y, z)
#
# a = date1 - date2
# print(a)
#
def add(arg1, arg2):
    print(arg1 + arg2)

def div(arg1, arg2):
    if arg2 == 0:
        print("Blad")
    else:
        print(arg1 / arg2)

def mul(arg1, arg2):
    print(arg1 * arg2)

def min(arg1, arg2):
    print(arg1 - arg2)

def start():
    x = int(input("podaj liczbe a: "))
    y = int(input("podaj liczbe b: "))

    while True:
        choice = int(input("podaj dzialanie: 1-dodawanie, 2-dzielenie, 3-mnozenie, 4-odejmowanie 5-wyjscie "))
        if choice == 1:
            add(x, y)
        elif choice == 2:
            div(x, y)
        elif choice == 3:
            mul(x, y)
        elif choice == 4:
            min(x, y)
        else:
            print("koniec")
            break

start()