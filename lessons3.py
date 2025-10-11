# ООП-объектно ориентированные программирование
# сигнатура функции
# git log - показывает список commit
# git switch main-переключить, git branch-если забыли ,
# dev -

# Полимарфизм
# родитель, суперкласс
class Car:
    # инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

# дочерний класс, наследник
class Bus(Car):
    def __init__(self, model, color, seats):
        super().__init__(model, color)
        self.seats = seats

    def drive_to_location(self, location):
        # super().drive_to_location(location)
        print(f"Bus {self.model} is driving to {location}")

    def test_bus(self):
        print(f"Bus test bus {self.color}")

class Truck(Car):
    pass


car_honda = Car(model='Honda', color='White')
bus_1 = Bus(model="Mercedes", color="green", seats=30)
bus_1.drive_to_location(location="Bishkek")
car_honda.drive_to_location(location="Karakol")

vehicles = [car_honda, bus_1]

for v in vehicles:
    v.drive_to_location(location="Bishkek")


class Car:
    # инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.__fined = False
        self.__max_speed = 0

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")
        self.__test_car()

    def __test_car(self):
        print(self.model, self.__fined)

    # геттер
    @property
    def fined(self):
        return self.__fined

    # сеттер
    @fined.setter
    def fined(self, value):
        self.__fined = value

    # сеттер
    def set_max_speed(self, value):
        if value <= 0:
            raise ValueError("max_speed must be positive")
        self.__max_speed = value

    # геттер
    def get_max_speed(self):
        return self.__max_speed

car_honda = Car(model='Honda', color='White')
# следующие 2 строки вызовут ошибку, так как идет обращение к приватным атрибутам/методам
# print(car_honda.__fined)
# car_honda.__test_car()
car_honda.drive_to_location("Bishkek")
car_honda.__fined = 1

car_honda.drive_to_location("Bishkek")
print(car_honda._Car__fined)

print(car_honda.fined)
car_honda.fined = True
print(car_honda.fined)

# car_honda.set_max_speed(-1)
print(car_honda.get_max_speed())









