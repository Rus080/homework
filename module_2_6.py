numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []

while True:  #Ввод первой переменной
    n = int(input('Введите число для первой вставки: '))
    if n not in range(3,21):
        print("Повторите ввод числа в интервале от 3 до 20")
        continue
    else:
        print('Число из первой вставки =', n)
        break

for i in range(1, len(numbers)):
    for j in range(i, len(numbers)):
        if (i + j) % n == 0 or n % (i + j) == 0:
            if (i + j) > n or i == j or i == numbers[-1]:
                continue
            result.append(i)
            result.append(j)
print ('Пароль второй вставки: ', *result)


