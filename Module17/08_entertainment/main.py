import random
N = int(input('Количество палок: '))
ListN = ['I' for i in range(1, N + 1)]
K = int(input('Количество бросков: '))

for res in range(1, K + 1):
    print()
    i = random.randrange(1, N + 1)
    Left_i = random.randrange(1, i + 1)
    Right_i = random.randrange(i, N + 1)
    print('Бросок ' + str(res) + '. Сбиты палки с номера ' + str(Left_i) +
'\nпо номер ' + str(Right_i) + '.')
    for i in range(Left_i - 1, Right_i):
        ListN[i] = '.'
print('Результат: ', end = '')
ListN = [print(i, end = '') for i in ListN]