from core.search_helper import SearchHelper
from view.view_book import ViewBook
from view.input_book import InputBook

class MainApp():
    def __init__(self):
        self.books = []

if __name__ == "__main__":
    app = MainApp()
    app.run()

    def list_book(self):
        self.view = ViewBook ()
        self.viewbook = []

    def input_book(self):
        self.input = InputBook()
        self.input.input()
        InputBook.jumlah_book = 1


    def list_book(self):
        view = ViewBook(self.books)
        view.list()


    def add_book(self):
        add = InputBook()
        add.input()


    def search_book():
        cari = InputBook()
        cari.search()
        help = SearchHelper()
        help.search_title()
        liat = ViewBook(books=self)
        liat.list()