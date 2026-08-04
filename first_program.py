print("Hello World!")
print('Я', 'учусь', 'программировать', 'на', 'Python!')

print('Какой хороший день!')
# Команда print() с пустым списком аргументов просто вставляет новую пустую строку.
print()
print('Работать мне не лень!')
print('В тексте есть "двойные" кавычки')
print("В тексте есть 'одинарные' кавычки")
print("I'm", 'the', "BAD", 'guy')
print("Hello, it's me!")
print('Hello, it\'s me!')
print("Здравствуй, мир!")
print("4", "8", "15", "16", "23", "42")
print("4", "\n8", "\n15", "\n16", "\n23", "\n42")
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

print("Как тебя зовут?")
print("Привет,", input())

variable_name = input()
print("Вы ввели текст:", variable_name)

name = 'Алеша'
city = "Тула"
print('Меня зовут', name, '.', city, '- мой город!')

print('Как тебя зовут?')

name = input()
print('Привет,', name)

name = 'Timur'
print('Привет,', name)

name1 = 'Тимур'
name2 = name1
name1 = 'Гвидо'
print(name1)
print(name2)

# сначала тут печатается строка 'Как тебя зовут', а потом принимается на вход имя
name = input('Как тебя зовут?')

first = input()
second = input()
print('I am', first, 'and', second)

name_1 = input()  # принимаем имя первого человека
print('Привет,', name_1, '!')  # делаем первый вывод

name_2 = input()  # принимаем имя второго человека
print('Здравствуйте,', name_2, '.')  # делаем второй вывод

# sep (separator – разделитель), По умолчанию этот параметр равен символу пробела
print('aa', 'bb', 'cc', sep='*')

minus = '-'
print('aa', 'bb', 'cc', sep=minus)

# По умолчанию параметр end равен символу перевода строки (\n).
print("A great man doesn't seek to lead.")
print("He's called to it. And he answers.")
print("A great man doesn't seek to lead.", end='\n')
print("He's called to it. And he answers.", end='\n')

# Если перевод строки делать не нужно или требуется указать специальное окончание для вывода,
# то следует явно указать значение для параметра end (можем указать через переменную, как и с параметром sep).
# По завершении печати первой команды print() вставлен символ - вместо символа перевода строки \n
minus = '-'
print('a', 'b', 'c', end=minus)
print('second line')

print('a', '\n', 'b', '\n', 'c', sep='*', end='#')

arg1 = 'Hello'
sep1 = '_-_'
end2 = '+++'
print(arg1, 'everyone', sep=sep1, end='! ')
print('How', 'are', 'you', 'in', '2024?', sep='     ', end=end2)

# Чтобы убрать все дополнительные выводимые символы,
# можно установить параметры sep и end команды print() как пустые строки ('').
print('a', 'b', 'c', sep='', end='')
print('d', 'e', 'f', sep='')

print('Python', end='\n\n\n')

name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)

name1 = 'Timur'
name2 = 'Gvido'
name1, name2 = name2, name1

a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Порядок выполнения операций как в математике.
num1 = 2 + 3 * 4
num2 = (2 + 3) * 4

print(num1)
print(num2)

# Чтобы преобразовать строку к целому числу, используем команду int()
s = '1992'
year = int(s)

print(year)

num1 = int(input())
num2 = int(input())

print(num1 + num2)

# чтобы преобразовать целое число в строку, мы используем команду str()
num = 17
s = str(num)

num1 = -6  # унарный минус
num2 = 17 - 7  # бинарный минус

# результат операции деления / всегда будет числом с плавающей точкой
print(4 / 2)
print(1 / 1)

a = int(input())
b = int(input())

c = 3 * ((a + b) * (a + b) * (a + b)) + (275 * (b * b)) - (127 * (a * a)) - 41
print(c)
