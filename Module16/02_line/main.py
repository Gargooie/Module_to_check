class1 = list(range(160, 177, 2))
class2= list(range(162, 181, 3))
class1.extend(class2)
class1.sort()

print('Отсортированный список учеников: ', class1)