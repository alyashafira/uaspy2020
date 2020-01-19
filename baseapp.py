from view.view_book import ViewBook
from view.input_book import InputBook
from core.search_helper import SearchHelper
class BaseApp:
    def run(self):
        while True:
            key = self.__menu()
            if key == "4":
                break
            elif key == "3":
                self.search_book()
            elif key == "2":
                self.add_book()
            elif key == "1":
                self.list_book()
            else:
                print("Pilihan tidak ada.")

    def list_book(self):
        ViewBook.list(self)
    def add_book(self):
        InputBook.input(self)
    def search_book(self):
        InputBook.search(self)
        a = ViewBook(self.books)
        a.list()
    def __menu(self):
        self.clear()

        print("===========================================")
        print("|         PROGRAM KATALOG PUBLIKASI       |")
        print("===========================================")
        print("| 1) Daftar Buku                          |")
        print("| 2) Tambah Buku                          |")
        print("| 3) Cari Buku                            |")
        print("| 4) Keluar Program                       |")
        print("===========================================")
        key = input("Pilih menu (1-4): ")
        return key

    def clear(self):
        import subprocess as sp
        import platform

        # Clear command as function of OS
        if platform.system().lower() == "windows":
            sp.call('cls', shell=True)
        else:
            sp.call('export TERM=xterm', shell=True)
            sp.call('clear', shell=True)