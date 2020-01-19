class Author:
    def __init__(self, name=""):
        self.name = name
        self.gender = ""
        self.address = ""
        self.phone = 0

    def toString(self):
        return "Name: {0}, Address: {1}".format(self.name, self.address)