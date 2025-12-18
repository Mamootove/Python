class Library:
    
    books = []
    borrowed_books = []

    def __init__(self):
        pass

    def add_book(self, name, author, year):
        book = {
            "Name": name,
            "Author": author,
            "Year": year,
            "Available": True
        }
        self.books.append(book)

    def show_books(self):
        print("book's name, Author's name, Year, Status")
        for book in self.books:
            print(f"{book["Name"]} | {book["Author"]} | {book["Year"]} | {"Available" if book["Available"] else "Unavailable"}")       
        print()
    def show_borrowed_books(self):
        print("book's name, Author's name, Status")
        for book in self.borrowed_books:
            print(f"{book["Name"]} | {book["Author"]} | {book["Year"]} | {"Available" if book["Available"] else "Unavailable"}")       
        print()        

    
        
class Book(Library):
    def __init__(self):
        pass

    def borrow(self, name):
        for book in self.books:
            if book["Name"] == name:
                if book["Available"] == True:
                    book["Available"] = False
                    self.borrowed_books.append(book)
                    print(f"Done\n{name} is borrowed.\n")
                else:
                    print("It seems it has already been borrowed.\n")
                return None 
        print(f"We dont have {name}")
    
    
    def return_borrow(self, name):
        for book in self.borrowed_books:
            if book["Name"] == name:
                book["Available"] = True
                self.borrowed_books.remove(book)
                print(f"Done\n{name} has returned to library.")
            else:
                print(f"It seems we didnt borrowed you the '{name}'")
                print("If you think there is an issue, Please report it to manager!") 






book1 = Library().add_book("slavery", "Nigga", 1898)
book2 = Library().add_book("How to become rich", "White", 2020)
book3 = Library().add_book("Being a silver man", "silver", 1940)


Book().borrow("How to become rich")

Book().borrow("slavery")


Library().show_borrowed_books()
Library().show_books()