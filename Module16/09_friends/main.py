
def data_in():
    friends = int(input('Кол-во друзей: '))
    credit = int(input('Долговых расписок: '))
    List = list(range(1, friends + 1))

    return List, credit

def logic(credit, List):
    ListAll = []
    ListMoney = []

    for i in range(1, credit + 1):
        print('\n', i, '-я расписка')
        creditMan = int(input('Кому: '))
        debitMan =  int(input('От кого: '))
        money = int(input('Сколько: '))
        ListAll.append(creditMan)
        ListAll.append(-money)
        ListAll.append(debitMan)
        ListAll.append(money)

    for people in List:
        summ = 0
        while True:
            if ListAll.count(people) > 0:
                value = ListAll[ListAll.index(people) + 1]
                summ += value
                ListAll.remove(people)
                ListAll.remove(value)
            elif ListAll.count(people) == 0:
                summ += 0
                break
        ListMoney.append(summ)
    return ListMoney

def visual(List1, List2):
    print('\nБаланс друзей:')
    for i in List1:
        index = List1.index(i)
        print(str(i) + ': ' + str(List2[index]))

ListFriends, credit = data_in()
ListEnd = logic(credit, ListFriends)
visual(ListFriends, ListEnd)