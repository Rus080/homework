my_dict = {'alex': 2001, 'den': 2005, 'mark': 2003}
print('my_dict:', my_dict)
print('чью дату рождения ищем?')
find = input()
print('Год рождения', '"', find, '"', ':', my_dict.get(find, 'данные отсутствуют'))
my_dict.update({'max': 1999,
                'mila': 2019})
print('new my_dict = ', my_dict)
print('Год рождения', '"', find, '"', ':', my_dict.get(find, 'данные отсутствуют'))
a = my_dict.pop('mark')
print(my_dict, ' - MARK deleted')
print('MARK = ', a)

my_set = {1, 1, 2, 3, 5, 4, 5, 4, 8, 'yes', 'yes', 1, 2}
print('set:', my_set)
my_set.add(7)
my_set.add('no')
print('Modified set:', my_set, '+"7" and "no"')
my_set.discard(2)
print('Modified set:', my_set, '- "2"')
