print('Введите первое число :')
First = input()
print('Введите второе число :')
second = input()
print('Введите третье число :')
third = input()
if First == second and second == third:
    print('Все числа равны между собой = 3')
elif First == second or second == third or First == third:
    print('2 из 3 введённых чисел равны между собой = 2')
elif First != second or second != third or First != third:
    print('Равных чисел среди введенных нет = 0')

#print(First, second, third)