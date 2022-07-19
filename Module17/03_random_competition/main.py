import random
comandFirst = [round(random.uniform(5, 10), 2) for _ in range(20)]
comandSecond = [round(random.uniform(5, 10), 2) for _ in range(20)]

List = [comandFirst[i] if comandFirst[i] - comandSecond[i] > 0 else comandSecond[i] for i in range(20)]

print('Первая команда: ', comandFirst)
print('Вторая команда: ', comandSecond)
print('Победители тура: ', List)