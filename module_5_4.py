# Задача "История строительства


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args:
            cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors,):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):  # - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        # return self.number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h1
print(House.houses_history)
print(h2,h3, sep='\n') # sep='\n' вывод результата в столбик


