class ViewBook():
    def __init__(self, books = []):
        self.books = books

    def list(self):
        while True:
            self.clear()
            print("=================================================================================")
            print("| ID |              TITLE               |     AUTHOR      |   PRICE    | COPIES |")
            print("=================================================================================")
            if len(self.books) == 0:
                print("|                                  Data Empty                                   |")

            idx = 0
            for book in self.books:
                idx+=1
                print("| {}  {}".format(idx, book.toRow()))
            print("=================================================================================")

            key = input("Detail [ID], [B]ack to menu: ")
            if key.lower() == "b":
                break
            elif key.isnumeric():
                self.detail(int(key.lower()) - 1)

    def detail(self, id):
        self.clear()
        if id < len(self.books):
            self.books[id].displayInfo()
        wait = input("Press enter to continue")

    def clear(self):
        import subprocess as sp
        import platform

        # Clear command as function of OS
        if platform.system().lower() == "windows":
            sp.call('cls', shell=True)
        else:
            sp.call('export TERM=xterm', shell=True)
            sp.call('clear', shell=True)