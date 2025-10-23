# dunder methods
class Money:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):                                            #__магический метод
        return f"Money amount={self.amount}"

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

#ge - greater than строгое сравнение :>
#ge - greater than or equal , больше или равно:>=
#lt - less than, строго меньше:<
#le - less than or equal: <=
    def __gt__(self, other):
        if self.amount > other.amount:
            return True
        return False



money_naziko = Money(amount=1000)
money_nz = Money(amount=2000)

print(money_naziko)
print(money_nz)

print(money_naziko == money_nz)
print(money_naziko > money_nz)
print(money_nz > money_naziko)