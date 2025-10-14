# Абстракции
# git checkout -b lesson4
#абстракный=== дочерный класс ?
# абстакный нечего
# дочерный = реализация и происходит


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
     pass


class Dog(Animal):
    def make_sound(self):
      print("гав гав")

puppy = Dog()


