class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей. Поднимаемся на {new_floor} этаж.')
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor} - Такого этажа не существует!')
        else :
            for floor in range (int(new_floor)):
                print(floor + 1)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)



# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))


