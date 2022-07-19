def code(ListText, ListSymbols):
    List = []
    for count1, i in enumerate(ListText):
        for count2, u in enumerate(ListSymbols):
            if i == u:
                List.append(ListSymbols[(count2 + step) % len(ListSymbols)])
            elif i == '!' or i == '?' or i == '.' or i == ',' or i == ' ':
                List.append(i)
                break
    return List

symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))

ListSymbols = [i for i in symbols]
ListText = [i for i in text]
print('Зашифрованное сообщение: ', end = '')
ListCode = code(ListText, ListSymbols)
ListCode  = [print(i, end = '') for i in ListCode]
