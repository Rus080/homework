# Задача "Счетчик вызовов"

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    a = list()
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    string = tuple(a)
    count_calls()
    return string


def is_contains(a, b):
    c = 'none'
    for i in b:
        if a.lower() in i.lower():
            c = True
        else:
            c = False
        continue
    count_calls()
    return c


print(string_info('alex'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
