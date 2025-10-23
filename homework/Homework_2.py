class Person:
    def __init__(self, name, birth_date, who, job):
        self.name = name
        self.birth_date = birth_date
        self.who = who
        self.job = job

    def introduce(self):
        print(f"Привет меня зовут {self.name}. Я {self.who}, родился {self.birth_date}, работаю {self.job}.")

class Classmate(Person):
    def __init__(self, name, birth_date, who,  job, hobby):
         super().__init__(name, birth_date, who, job)
         self.hobby = hobby


    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, родился {self.birth_date}. Я {self.who}, работаю {self.job}, мой хобби{self.hobby}.")



class Friend(Person):
    def __init__(self, name, birth_date, who, job, hobby):
        super().__init__(name, birth_date, who, job)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет!  Меня зовут {self.name}, родился {self.birth_date}. Я {self.who}, работаю {self.job}, мой хобби — {self.hobby}.")

classmate = Classmate(name="Tom", birth_date="13.06.2006", who="друг Жери", job="программистом", hobby="футбол")
friend = Friend(name="Jeri",  birth_date="1.09.2005", who="знакомый Тома", job="айтишник", hobby="баскетбол")

classmate.introduce()
friend.introduce()



