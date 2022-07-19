text = input('Введите строку: ')
print('Развёрнутая последовательность между первым и последним h: ', end = '')
List = [i for count1, i in enumerate(text) if i != 'h']
List = [print(i, end = '') for i in List[::-1]]


