# Задача 2. Генерация
N = int(input('Введите длину списка: '))
print(3 % 5)

List =[(1 if i % 2 == 0 else  i % 5) for i in range(N)]
print(List)