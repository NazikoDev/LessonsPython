class User:
  #переменные класса
   total_users = 0

   def __init__(self, name, email):
      self.name = name
      self.email = email
      User.total_users += 1

   def test(self):
      print(self.name)

   @classmethod
   def get_total_user(cls):
      return cls.total_users

   @classmethod
   def create_user(cls, name, email):
      if not cls.validate_email(email):
          raise ValueError("Invalid email")
      user = cls(name, email)
      return user

   @staticmethod
   def validate_email(email):
      if "@" in email:
          return True
      return False

print(f"{User.total_users=}")
user_1 = User("nazik", "nazik@gmail.com")
user_2 = User("gulnazik", "gulnazik@gmail.com")
print(f"{User.total_users=}")
user_1.test()
print(User.get_total_user())
print(user_1.total_users)

try:
   usr = User.create_user(name="nazik", email="n")
except ValueError as e:
   print("Ошибка:", e)


print(User.validate_email("mail@mail.com"))


