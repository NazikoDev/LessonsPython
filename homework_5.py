class Distance:
    def __init__(self, value, unit: str):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"value={self.value} unit={self.unit}"

    def __add__(self, other):
        if self.unit == other.unit:
            new_distance = Distance(value=self.value + other.value, unit=self.unit)
            return new_distance
        else:
            return "Единицы измерения должны быть ровны"


    def __sub__(self, other):
        if self.unit == other.unit and self.value - other.value>0:
            new_distance = Distance(value=self.value - other.value, unit=self.unit)
            return new_distance
        else:
            return "Единицы измерения должны быть ровны, их разница не может быть меньше 0"


    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False


    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False

    def __ge__(self, other):
        if self.value >= self.value:
            return True
        return False

    def __lt__(self, other):
        if self.value < self.value:
            return True
        return False

    def __le__(self, other):
        if self.value <= self.value:
            return True
        return False


d1 = Distance(value=100, unit="м")
d2 = Distance(value=12, unit="м")

print(d1)
print(d2)

print(d1 == d2)
print(d1 > d2)
print(d2 > d1)
print(d1 - d2)
print(d2 - d1)