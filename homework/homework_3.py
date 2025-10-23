import datetime

class Person:
    def __init__(self, name, birth_date, who, job, ):
        self.name = name
        self.__birth_date = birth_date
        self.who = who
        self.job = job


    def introduce(self):
        print(f"Привет меня зовут {self.name}, родился {self.__birth_date}, мне {self.age}. Я {self.who}, работаю {self.job}.")

    def age(self, birth_date):
        birth = datetime.datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.datetime.today()

        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, родился {self.__birth_date}, мне {self.age()} лет. Я {self.who}, работаю {self.job}.")

class Classmate(Person):
    def __init__(self, name, birth_date, who,  job, hobby):
         super().__init__(name, birth_date, who, job)
         self.__birth_date = birth_date
         self.hobby = hobby



    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, родился {self.__birth_date}. Я {self.who}, работаю {self.job}, мой хобби - {self.hobby}.")



class Friend(Person):
    def __init__(self, name, birth_date, who, job, hobby):
        super().__init__(name, birth_date, who, job)
        self.__birth_date = birth_date
        self.hobby = hobby

    def introduce(self):
        print(f"Привет!  Меня зовут {self.name}, родился {self.__birth_date}, мне {self.name}. "
              f"Я {self.who}, работаю {self.job}, мой хобби — {self.hobby}.")

classmate = Classmate(name="Tom", birth_date="13.06.2006", who="друг Жери", job="программистом", hobby="футбол")
friend = Friend(name="Jeri",  birth_date="1.09.2005", who="знакомый Тома", job="айтишник", hobby="баскетбол")

classmate.introduce()
friend.introduce()

print(f"Возраст Tome: {classmate.age("13.06.2006")} лет")
print(f"Возраст Jeri: {friend.age("1.09.2005")} лет")
