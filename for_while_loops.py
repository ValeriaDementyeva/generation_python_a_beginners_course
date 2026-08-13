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
