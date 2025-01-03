# Задача "Developer - не только разработчик"


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to (self, new_floor):
        print(f'{self.name}, количество этажей в доме: {self.number_of_floors}')
        new_floor = int(new_floor)
        n=1
        while n != new_floor+1:
            if new_floor <= 1 or new_floor > self.number_of_floors:
                print(new_floor, '- Такого этажа не существует')
                break
            print(n)
            n += 1


# Задача "Магические здания"
    def __len__(self):
        return self.number_of_floors

    def __str__(self): # - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        #return self.number_of_floors


# Задача "Нужно больше этажей"
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def  __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def  __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def  __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def  __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError('Разные типы переменных')
        return House(self.name, self.number_of_floors + other)

    def __radd__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError('Разные типы переменных')
        return House(self.name, self.number_of_floors + other)

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError('Разные типы переменных')
        return House(self.name, self.number_of_floors + other)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
#h1.go_to(6)
#h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)

h1 += 10 # __iadd__
print(h1)

h2 = 36 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__