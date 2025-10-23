class Car:
    #инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to_location(self, location):
        print(f"Car {self.model} is diving to {location}")

#создание объектов
car_honda = Car(model='Honda', color='White')
car_subaru = Car(model='subaru', color='red')

print(car_honda)
print(f"Car model: {car_honda.model}, color: {car_honda.color}")
print(car_subaru)
print(f"Car model: {car_subaru.model}, color: {car_subaru.color}")

car_honda.drive_to_location("Karakol")

print(type("AAAAA"))
print(type(123))
print(type(car_honda))











