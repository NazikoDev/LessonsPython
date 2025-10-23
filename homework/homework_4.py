class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class ElectricCar(Vehicle):
    def electro_start(self):
        print("Electro car starting")

class Tesla(Car, Vehicle):
    def start(self):
        super().start()
        print("Tesla starting")

tesla = Tesla()
tesla.start()





