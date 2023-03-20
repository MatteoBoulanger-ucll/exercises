class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @currency.setter
    def currency(self, value):
        self.__currency = value

    def __add__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies")
        else:
            return Money(self.__amount + other.__amount, self.__currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies")
        else:
            return Money(self.__amount - other.__amount, self.__currency)

    def __mul__(self, value):
        return Money(self.__amount * value, self.__currency)
