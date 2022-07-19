def data_in():
    List = []
    numbers = int(input('Кол-во чисел: '))
    for _ in range(numbers):
        List.append(int(input('Число: ')))
    return List

def logic(List):
    List2 = []
    count = 0
    if List[-1] == List[-2]:
        start = len(List) - 3
        for i in range(start, 0, -1):
            count += 1
            List2.append(List[i])
        List2.append(List[0])
        count += 1
    elif List[-1] != List[-2]:
        start = len(List) - 2
        for i in range(start, 0, -1):
            count += 1
            List2.append(List[i])
        List2.append(List[0])
        count += 1
    return List2, count

def visual(List1, List2, count):
    print('\nПоследовательность: ', List1)
    print('Нужно приписать чисел: ', count)
    print('Сами числа: ', List2)



numList = data_in()
ListEnd, count = logic(numList)
visual(numList, ListEnd, count)
