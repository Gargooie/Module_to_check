List1 = []
List2 = []
for i in range(1, 4):
    List1.append(int(input('Введите ' + str(i) + '-е число для первого списка: ')))

for i in range(1, 8):
    List2.append(int(input('Введите ' + str(i) + '-е число для второго списка: ')))

print('\nПервый список: ', List1)
print('Второй список: ', List2)

List1.extend(List2)
ListEnd = []
for i in List1:
    ListEnd.append(i)


for i in List1:
    while True:
        if ListEnd.count(i) > 1:
            ListEnd.remove(i)
            break
        elif ListEnd.count(i) == 1:
            break


print('\nНовый первый список с уникальными элементами: ', ListEnd)
