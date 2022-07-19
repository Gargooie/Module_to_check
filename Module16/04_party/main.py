guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']



while True:
    print('\nСейчас на вечеринке ' + str(len(guests)) + ' человек:', guests)
    text = input('Гость пришёл или ушёл? ')
    if text == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя: ')
    if text == 'пришёл':
        if len(guests) < 6:
            guests.append(name)
            print('Привет,' + name + '!')
        elif len(guests) == 6:
            print('Прости, ' + name + ', но мест нет.')
    elif text == 'ушёл':
        guests.remove(name)
        print('Пока,' + name + '!')
