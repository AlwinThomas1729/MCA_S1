class Publisher:
    def __init__(self, n):
        self.name = n

    def display(self):
        print("Publisher Name: ", self.name)

class Book(Publisher):
    def __init__(self, n, t, a):
        super().__init__(n)
        self.title = t
        self.author = a

    def display(self):
        super().display()
        print("Book Title: ", self.title)
        print("Book Author: ", self.author)

class Python(Book):
    def __init__(self, n, t, a, p, np):
        super().__init__(n, t, a)
        self.price = p
        self.no_page = np

    def display(self):
        super().display()
        print("Book Price: ", self.price)
        print("Number of pages: ", self.no_page)

python_book = Python(n="ABC", t="Python Programming", a="Me", p=200, np=10)
python_book.display()