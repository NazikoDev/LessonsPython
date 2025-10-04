class people:

    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def lives_to_location(self, location):
        print(f"people{self.name} is lives to {location}")


# создание объектов
Sponge_Bob = people(name="Sponge_Bob", birth_date="14.07.2006", occupation="cook", higher_education=False)
Mr_Krabs = people(name="Mr_Krabs", birth_date="30.10.2002", occupation="Менеджер", higher_education=False)
Sandy = people(name="Sandy", birth_date="17.10.2004", occupation="изобретательница",higher_education=True)

print(Sponge_Bob)
print(f" имя: {Sponge_Bob.name}, день рождение: {Sponge_Bob.birth_date}, профессия: {Sponge_Bob.occupation}, высшее оброзование: {False}")
print(Mr_Krabs)
print(f"имя: {Mr_Krabs.name}, день рождение: {Mr_Krabs.birth_date}, профессия: {Mr_Krabs.occupation}, высшее оброзование: {False}")
print(Sandy)
print(f"имя: {Sandy.name}, день рождение: {Sandy.birth_date}, профессия: {Sandy.occupation}, высшее оброзование: {True}\n")

Sponge_Bob.lives_to_location("under water")
Mr_Krabs.lives_to_location("under water")
Sandy.lives_to_location("under water")