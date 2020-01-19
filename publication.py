class Publication:
    def __init__(self, title="", price=0, copies=0):
        self.__title = title
        self.__price = price
        self.__copies = copies

    def sellCopy(self, sell):
        if self.__copies > sell:
            self.__copies -= sell

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, copy):
        self.__copies = copy

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        self.__title = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val
