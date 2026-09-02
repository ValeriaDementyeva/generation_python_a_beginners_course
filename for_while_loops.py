# любая цифра числа (num // 10 ** (n - i)) % 10
# n = len(str(num))
# num = int(input())                                # считываем число
# n = len(str(num))                                 # количество разрядов числа
# for i in range(1, n + 1):                         # проходим по всем разрядам числа от 1 до n
#     digit = num // 10 ** (n - i) % 10             # получаем i-ю цифру числа
#     ...                                           # обрабатываем i-ю цифру числа

for i in range(10):
    print('Привет')

for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)

print('Цикл завершен')

print("A")
print("B")

for i in range(5):
    print("C")
    print("D")

print("E")

print('A')
print('B')

for _ in range(5):
    print('C')

for _ in range(5):
    print('D')

print('E')

# Когда цикл впервые начинает работу, Python устанавливает значение переменной цикла i = 0.
# Каждый раз, когда мы повторяем тело цикла, Python увеличивает значение переменной на 1
for i in range(10):
    print(i)

for i in range(10):
    print(i, '-- Привет')

for i in range(10):
    print(i + 1, '-- Привет')

for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:  # используем остаток от деления на 10, для получения последней цифры
        print(i)

# все четные числа из промежутка [56;170]
for i in range(56, 171, 2):
    print(i)

for i in range(5, 0, -1):
    print(i, end=' ')
print('Взлетаем!!!')

counter = 0  # создаём переменную счётчика
for _ in range(10):
    num = int(input())
    if num > 10:  # при выполнении условия
        counter = counter + 1  # увеличиваем значение cчётчика

print('Было введено', counter, 'чисел, больших 10.')

counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.')

counter = 0
for i in range(1, 101):
    if i ** 2 % 10 == 4:
        counter = counter + 1

print(counter)

total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num

print('Сумма чисел больших 10 равна', total)

total = 0
for _ in range(10):
    num = int(input())
    total = total + num

average = total / 10
print('Среднее значение равно', average)

largest = 0
for _ in range(10):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)

largest = int(input())  # принимаем первое число за максимальное
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)  # smallest если наименьшее

# значения переменных x и поменяются местами
x = 5
y = 4
x, y = y, x

total = 1
num = 4

total += num  # total = total + num
total -= num
total *= num
total /= num
total //= num
total %= num

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')

# Фибоначчи
n = int(input())
a = 0
b = 1

for i in range(0, n):
    a, b = b, a + b
    print(a, end=' ')

num = int(input())
while num != -1:
    print('Квадрат вашего числа равен:', num * num)
    num = int(input())

text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()

print('Сумма чисел равна', total)

name = input()
while name != 'Валера' and name != 'Артур':
    print('Доступ запрещен')
    name = input()

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

total_m1 = h1 * 60 + m1
total_m2 = h2 * 60 + m2

while total_m1 <= total_m2:
    h1 = total_m1 // 60
    m1 = total_m1 % 60
    if h1 < 10 and m1 < 10:
        print("0", h1, ":", "0", m1, sep="")
    elif h1 < 10 and m1 > 10:
        print("0", h1, ":", m1, sep="")
    elif h1 > 10 and m1 < 10:
        print(h1, ":", "0", m1, sep="")
    else:
        print(h1, ":", m1, sep="")
    total_m1 += 1

num = 1576
has_seven = False  # сигнальная метка (флаг)

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')
#
# num = int(input())                                # считываем число
# while num != 0:                                   # проверяем, что цифры числа не закончились
#     last_digit = num % 10                         # получаем последнюю цифру числа
#     ...                                           # обрабатываем последнюю цифру числа
#     num = num // 10                               # удаляем последнюю цифру из числа


# num = int(input())                                # считываем число
# n = len(str(num))                                 # количество разрядов числа
# for i in range(1, n + 1):                         # проходим по всем разрядам числа от 1 до n
#     digit = num // 10 ** (n - i) % 10             # получаем i-ю цифру числа
#     ...                                           # обрабатываем i-ю цифру числа

num = int(input())
n = len(str(num))
count = 1

for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10
    if digit % 2 == 0:
        print(count, '-я', ' четная цифра равна ', digit, sep='')
        count += 1

if count == 1:
    print("Четных цифр в числе нет")

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break  # останавливаем цикл если встретили делитель числа

if flag:  # эквивалентно if flag == True:
    print('Число простое')
else:
    print('Число составное')

num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break  # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag:  # эквивалентно if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')

# то же самое, но с елс в цикле
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Цикл завершен.')

for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Цикл завершен.')

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Цикл завершен.')

# часы
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)

for i in range(8):
    for j in range(i + 1):
        print('*', end='')
    print()

total = 0
for x in range(1, 13):
    for y in range(1, 12):
        for z in range(1, 11):
            if 28 * x + 30 * y + 31 * z == 365:
                total += 1
                print('n =', x, 'k =', y, 'm =', z)
print('Общее количество натуральных решений =', total)

for bulls in range(11):  # быки по 10 рублей, максимум 10 штук (100/10)
    for cows in range(21):  # коровы по 5 рублей, максимум 20 штук (100/5)
        calves = 100 - bulls - cows  # оставшиеся головы - телята
        # Проверяем, что телят неотрицательное количество
        # и стоимость всех животных равна 100 рублям
        if calves >= 0 and bulls * 10 + cows * 5 + calves * 0.5 == 100:
            print(f"Быков: {bulls}, Коров: {cows}, Телят: {calves}")

n = int(input())
m = int(input())

found = False

for banana in range(1, n):
    for diamond in range(1, n):
        for deer in range(1, n):
            if banana + 3 * diamond + 2 * deer == m:
                print(f"{banana} + 3×{diamond} + 2×{deer} = {m}")
                found = True

if not found:
    print("При заданных n и m решений не существует.")
