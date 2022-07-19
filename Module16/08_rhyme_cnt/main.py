
def data_in():
    people = int(input('Кол-во человек: '))
    number = int(input('Какое число в считалке? '))
    print('Значит, выбывает каждый ' + str(number) + '-й человек')
    List = list(range(1, people + 1))
    return List, number, people

def logic(List, number, people):
    Stop = 0
    for i in range(people - 1):
        print('\nТекущий круг людей: ', List)
        start = Stop %  len(List)
        Stop = (start + number - 1) % len(List)
        print('Начало счёта с номера ', List[start])
        print('Выбывает человек под номером ', List[Stop])
        List.remove(List[Stop])
    return List[start]

def visual(num):
    print('\nОстался человек под номером ', num)




peopleList, number, people = data_in()
num = logic(peopleList, number, people)
visual(num)