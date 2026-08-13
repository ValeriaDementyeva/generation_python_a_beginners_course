# numm = int(input())  # преобразование считанной строки в целое число
# nn = int('12345')  # преобразование строки в целое число
#
# a = 13
# b = 7
#
# total = a + b
# diff = a - b
# prod = a * b
# div1 = a / b
# div2 = a // b
# mod = a % b
# exp = a ** b
#
# print(a, '+', b, '=', total)
# print(a, '-', b, '=', diff)
# print(a, '*', b, '=', prod)
# print(a, '/', b, '=', div1)
# print(a, '//', b, '=', div2)
# print(a, '%', b, '=', mod)
# print(a, '**', b, '=', exp)
#
# atom = 10 ** 80  # количество атомов во вселенной
# print('Количество атомов =', atom)
#
# num1 = 25_000_000
# num2 = 25000000
#
# print(num1)
# print(num2)
#
# num = float(input())  # преобразование считанной строки в число с плавающей точкой
# n = float('1.2345')  # преобразование строки к числу с плавающей точкой
# a = 13.5
# b = 2.0
#
# total = a + b
# diff = a - b
# prod = a * b
# div = a / b
# exp = a ** b
#
# print(a, '+', b, '=', total)
# print(a, '-', b, '=', diff)
# print(a, '*', b, '=', prod)
# print(a, '/', b, '=', div)
# print(a, '**', b, '=', exp)

# a = 13.5
# b = 2.0
# int_div = a // b
# mod = a % b
#
# print(a, '//', b, '=', int_div)
# print(a, '%', b, '=', mod)
#
# # преобразование чисел с точкой в целое производится с округлением в сторону нуля int(1.7) = 1, int(-1.7) = -1
# num1 = 17.89
# num2 = -13.56
# num3 = int(num1)
# num4 = int(num2)
#
# print(num3)
# print(num4)
#
# num1 = int(1.5)
# num2 = int(6)
#
# print(num1 + num2)
#
# a = max(3, 8, -3, 12, 9)
# b = min(3, 8.5, -3.2, 12, 9)
# c = max(3.14, 2.17, 9.8)
# print(a)
# print(b)
# print(c)
#
# print(abs(1 - 4))
# print(abs(-7))
# print(abs(0))
# print(abs(-17.67))
#
# s1 = ''  # пустая строка
# s2 = ' '  # строка, состоящая из одного символа пробела
#
# s1 = 'abcdef'
# length1 = len(s1)  # считаем длину строки из переменной s1
# length2 = len('Python rocks!')  # считаем длину строкового литерала
# print(length1)
# print(length2)
#
# num1 = 1777  # целое число
# num2 = 17.77  # число с плавающей точкой
# s1 = str(num1)  # преобразовали целое число в строку '1777'
# s2 = str(num2)  # преобразовали число с плавающей точкой в строку '17.77'
#
# s1 = 'ab' + 'bc'
# s2 = 'bc' + 'ab'
# s3 = s1 + s2 + '!!'
# print(s1)
# print(s2)
# print(s3)
#
# print('a', 'b', 'c', sep='*', end='!')
# print()  # переход на новую строку
# print('a' + '*' + 'b' + '*' + 'c' + '!')
#
# s = 'Hi' * 4
# print(s)
#
# print('-' * 75)
#
# text = '''Python is an interpreted, high-level, general-purpose programming language.
# Created by Guido van Rossum and first released in 1991, Python design
# philosophy emphasizes code readability with its notable use of significant whitespace.'''
#
# print('C++ sucks.' * 0 == '')
#
# s = 'https://pygen.ru/'
# if 'a' in s:
#     print('Введенная строка содержит символ а')
# else:
#     print('Введенная строка не содержит символ а')
#
# s = input()
# if '.' not in s:
#     print('Введенная строка не содержит символа точки')
#
# if len(s) == 1 and s in 'aeiou':
#     print('YES')
#
# s = 'Sigma'
# print('a' in s)
# print('z' in s)
#
# print('ab' in 'abc')
# print('ac' in 'abc')
#
# s = 'Alpha'
# print('p' in s)
# print('P' in s)
#
# s1 = 'Зеландия'
# s2 = 'Новая Зеландия'
# if s1 in s2:
#     print('Строка', s1, 'является подстрокой для строки', s2)
# else:
#     print('Строка', s1, 'не является подстрокой для строки', s2)

# import math  # все импорты должны быть в самом начале файла, это пример использования библиотек
#
# num1 = math.sqrt(2)  # вычисление квадратного корня из двух
# num2 = math.ceil(3.8)  # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

# Можно убрать явный вызов через точку (math.sqrt) подключив по другому, но лучше явно или конкретныефункции
from math import *

num1 = sqrt(40)  # вычисление корня квадратного из двух
num2 = ceil(3.8)  # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

# Импорт конкретоной функции из всей библиотеки
from math import sqrt, ceil

# извлечение квадратного корня можно по формуле n ** 0.5
