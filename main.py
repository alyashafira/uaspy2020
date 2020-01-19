from core.baseapp import BaseApp
from core.search_helper import SearchHelper
from data_model.author import Author
from data_model.book import Book
from data_model.publication import Publication
from view.input_book import InputBook
from view.view_book import ViewBook


class MainApp(BaseApp):
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()