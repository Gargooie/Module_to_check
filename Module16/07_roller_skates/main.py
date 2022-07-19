skate = int(input('Кол-во коньков: '))
sizeList = []
for i in range(1, skate + 1):
    sizeList.append(int(input('Размер ' + str(i) + '-й пары: ')))
print()
people = int(input('Кол-во людей: '))
sizeListPeople = []
for i in range(1, people + 1):
    sizeListPeople.append(int(input('Размер ноги ' + str(i) + '-го человека: ')))

count = 0
for i in sizeListPeople:
    if sizeList.count(i) != 0:
        count += 1
        sizeList.remove(i)

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count)