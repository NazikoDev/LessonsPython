
class Contact:
    id = 0

    def __init__(self, phone_number:str, name:str):
        self.phone_number = phone_number
        self.name = name
        Contact.id += 1

    def __str__(self):
        return f"name={self.name}; number{self.phone_number}"

    @staticmethod
    def validate_phone_number(phone_number: str):
        if len(phone_number) == 10 and phone_number [0] == "0":
            int (phone_number)
            return True
        elif "+" in phone_number:
            raise ValueError("Программа без кода страны работает")
        else:
            raise ValueError("Неверный номер тел")


class ContactList:
    all_contacts = {}

    def __init__(self):
        pass

    def add_contact(self, phone_number: str, name: str):
        try:
             Contact.validate_phone_number(phone_number)
             ContactList.all_contacts[Contact.id] = str(Contact(phone_number, name))
        except ValueError:
             return "Неверный номер тел"

    def remove_contact(self, contact_id: int):
        try:
            del ContactList.all_contacts[contact_id]
        except:
            print("такого контакта нет")


# user1 = Contact("+996555555550", "nazik")
# print(user1.validate_phone_number(user1.phone_number))
#
# contact_list = ContactList()
# print(contact_list.add_contact("0777777777", "sendi"))
# print(contact_list.add_contact("0555555555", "liza"))
# print(contact_list.add_contact("0222222222", "lana"))
# print(ContactList.all_contacts)
# print(Contact.id)
# contact_list.remove_contact(contact_id=1)
# print(contact_list.add_contact("0333333333", "fil"))
# print(Contact.id)



