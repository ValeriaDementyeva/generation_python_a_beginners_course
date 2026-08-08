a = int(input())

r = "красный"
b = "черный"

if a < 0 or a > 36:
    print("ошибка ввода")
elif a == 0:
    print("зеленый")
elif (a >= 1 and a <= 10) and a % 2 == 0:
    print(b)
elif (a >= 1 and a <= 10) and a % 2 != 0:
    print(r)
elif (a >= 11 and a <= 18) and a % 2 == 0:
    print(r)
elif (a >= 11 and a <= 18) and a % 2 != 0:
    print(b)
elif (a >= 19 and a <= 28) and a % 2 == 0:
    print(b)
elif (a >= 19 and a <= 28) and a % 2 != 0:
    print(r)
elif (a >= 29 and a <= 36) and a % 2 == 0:
    print(r)
elif (a >= 29 and a <= 36) and a % 2 != 0:
    print(b)
