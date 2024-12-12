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



h1 = House('"ЖК Горский"', 18)
h2 = House('"Домик в деревне"', 2)

h1.go_to(5)
h2.go_to(10)