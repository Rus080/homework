# Задача "Developer - не только разработчик"


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


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
            #print(self.name, 'поднимаемся на этаж', range(self.number_of_floors))


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(6)
h2.go_to(10)

