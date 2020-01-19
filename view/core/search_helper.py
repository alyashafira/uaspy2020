class SearchHelper():
    def __init__(self, books = []):
        self.books = books

    def search_title(self, title):
        result = []
        for book in self.books:
            if title.lower() in book.title.lower():
                result.append(book)

        return result

    def search_author(self, author):
        result = []
        for book in self.books:
            if author.lower() in book.author.name.lower():
                result.append(book)

        return result