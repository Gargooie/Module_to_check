import random

N = int(input('Количество чисел в списке: '))
List = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия: ', List)
List = [(List.append(res) if res == 0 else res) for res in List if res != 0]
print('Список после сжатия: ', List)


