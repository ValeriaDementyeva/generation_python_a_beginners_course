# answer = input('Какой язык программирования мы изучаем?')
#
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')
# else:
#     print('Не совсем так!')
#
# num1 = int(input())
# num2 = int(input())
#
# if num1 < num2:
#     print(num1, 'меньше чем', num2)
# if num1 > num2:
#     print(num1, 'больше чем', num2)
#
# if num1 == num2:
#     print(num1, 'равно', num2)
# if num1 != num2:
#     print(num1, 'не равно', num2)
#
# age = int(input())
# if 3 <= age <= 6:
#     print('Вы ребёнок')
#
# if a == b == c:
#     print('числа равны')
# else:
#     print('числа не равны')
#
# num = int(input())
#
# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа
#
# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')
#
# num1, num2, num3 = int(input()), int(input()), int(input())
#
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
#
# print(counter)
from unittest import result

# pas1, pas2 = input(), input()
#
# if pas1 == pas2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# true = 1, false = 0
# a = int(input())
# b = int(input())
# c = int(input())
# print(a * (a>0) + b*(b>0) + c*(c>0))
#
# num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
# result = num1
#
# if result > num2:
#     result = num2
# if result > num3:
#     result = num3
# if result > num4:
#     result = num4
# print(result)

# Оператор and
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# Оператор or
city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# Оператор not позволяет инвертировать (заменить на противоположный) результат логического выражения
age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# if age >= 7 and age <= 9: полностью эквивалентен коду: if 7 <= age <= 9:
num = int(input())
if 100 <= num <= 999:  # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')

num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')

# Заключительный блок else в операторе if-elif-else является необязательным
traffic_light_signal = input('Введите сигнал светофора: ')

if traffic_light_signal == 'красный':
    print('Стой!')
elif traffic_light_signal == 'желтый':
    print('Приготовься...')
elif traffic_light_signal == 'зеленый':
    print('Иди!')

grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# Находим левую границу пересечения (максимум из левых границ)
left = a1 if a1 > a2 else a2

# Находим правую границу пересечения (минимум из правых границ)
right = b1 if b1 < b2 else b2

if left < right:
    # Пересечение - отрезок
    print(left, right)
elif left == right:
    # Пересечение - точка
    print(left)
else:
    # Пересечение - пустое множество
    print("пустое множество")
