
text = input('Введите текст: ')

symbols = ['А', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'И', 'Ю', 'Я','а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']

List = [x for i in text for x in symbols if i == x]
print('\nСписок гласных букв:', List)
print('Длина списка: ', len(List))