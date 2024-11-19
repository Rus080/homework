my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Исходные данные:', my_list)
i=0
n=[]
while i < len(my_list):
    if my_list[i] > 0:
        n.append(my_list[i]) #n.append()
        i += 1
    elif my_list[i] == 0 or my_list[i] < 0:
        pass
        i += 1
        continue
print('Вывод на консоль:', n)
