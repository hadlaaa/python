class Publisher:
    def __init__(self):
        self.pid = input("Enter Publisher ID: ")
        self.pname = input("Enter Publisher Name: ")

    def display(self):
        print("Publisher ID:", self.pid)
        print("Publisher Name:", self.pname)


class Book(Publisher):
    def __init__(self):
        super().__init__()
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Author Name: ")

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self):
        super().__init__()
        self.price = float(input("Enter Price: "))
        self.pages = int(input("Enter Number of Pages: "))

    def display(self):
        super().display()
        print("Price:", self.price)
        print("No. of Pages:", self.pages)


p = Python()
print("\n--- Python Book Details ---")
p.display()
