#-1.инкапсуляция
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.__age = age

    def get_age(self):
        return self.__age

# p = Person()
# p.set_age(25)
# print(p.get_age()) # Вывод: 25
# p.set_age(-5) # Должна быть ошибка или предупреждение

# #2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def introduse(self):
        print(f"hi! I am an animal {self.name}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

        def speak(self):
            return "Meow"

# dog = Dog("Buddy")
# cat = Cat("Kitty")
# print(dog.name, dog.speak()) # Вывод: Buddy Woof
# print(cat.name, cat.speak()) # Вывод: Kitty Meow

#3. Полиморфизм

class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()


# Пример:
# car = Car()
# bike = Bicycle()
# print(move(car))  # Car is driving
# print(move(bike))  # Bicycle is pedaling


# 4. Абстракция
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Пример:
# rect = Rectangle(10, 5)
# circle = Circle(7)
# print(rect.area())     # 50
# print(circle.area())   # 153.938...
