class library:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def add_book(self, title, author):
        self.title = title
        self.author =author
        print(f"The book '{self.title}' from '{self.author}' saved to memory!")

    def remove_book(self):
        del self.title

    def search(self):
        if title in self.title :
            print("YUP, found it!")
        elif title in self.title :
           print("Seems here you cant find what you been looking for.")

    def show():
        print(library.title) 
    
b1 = library("b1", "a1")
library.search(b1)

            