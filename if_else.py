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

# Оператор not
age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
