class Person:

    def __init__(self, name, birth_date, who, job):
        self.name = name
        self.birth_date = birth_date
        self.who = who
        self.job = job

    def live_to_location(self, location):
        print(f"person {self.name} is live to {location}")

class Classmate(Person):

    def __init__(self, name, birth_date, who,  job, hobby,hao, born, work):
         super().__init__(name, birth_date, who, job)
         self.hobby = hobby,
         self.hao = hao
         self.born=born
         self.work=work

    def live_to_location(self, location):
        super().live_to_location(location)
        print(f"classmate {self.name}, is live to {self.location}")

    def test_classmate(self):
        print(f"classmate test classmate {self.name}, classmate {self.birth_date}, "
      f"classmate{self.who}, classmate{self.job}, classamate{self.hobby}")

class Friend(Person):

    def __init__(self, name, birth_date, who, job, hobby, hao, born, work):
        super().__init__(name, birth_date, who,  job)
        self.hobby = hobby,
        self.hao = hao
        self.born=born
        self.work=work
    def live_to_location(self, location):
        super().live_to_location(location)
        print(f"friend {self.name}, is live to {self.location}")


classmate = Classmate(hao="Привет меня зовут",name="Tom ,", born="родился", birth_date="13.06.2006", who=", друг Жери", work=", работаю", job="программистом", hobby="футбол")
print(classmate.hao,classmate.name, classmate.born, classmate.birth_date, classmate.who, classmate.work, classmate.job, classmate.hobby)
friend = Friend(hao="Привет меня зовут",name="Jeri ,", born="родился",  birth_date="1.09.2005", who=", знакомый Тома", work=", работаю", hobby="баскетбол", job="айтишником")
print(friend.hao, friend.name, friend.born, friend.birth_date, friend.who, friend.work, friend.job, friend.hobby)