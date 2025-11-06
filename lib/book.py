#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count, author, total_pages,isbn=None):
        self.title = title
        self._page_count = page_count
        self.author = author
        self.total_pages = total_pages
        self.isbn = isbn

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self._page_count -= 1
        if self._page_count == 0:
            print("You've finished the book!")
            self._page_count = 0
            print("Book is now closed.")


