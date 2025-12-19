class Library:
    
    books = [] #All books we have
    borrowed_books = []

    def __init__(self): #I think we dont need this, Anyway!
        self.name : str
        self.author: str
        self.year: int

    def Hand_adding(self, name, author, year): #Here is  Where we make a new object in line in class and add it to the boosk list up there.
        book = {
            "Name": name,
            "Author": author,
            "Year": year,
            "Available": True
        }
        self.books.append(book)

    def inputer(self):
        self.name = input("Enter the book's name: ")
        self.author = input("Enter the book's author: ")
        self.year = int(input("Enter the year of the book: "))
    
    def menu(self): #Main Function.
        flag = 666 #Its just a random number, in case to start the while I just needed something as starter.
        Menu = "\nWhat do you wanna do?\n(1.add a book)\n(2.see all books)\n(3.see unborrowed books)\n(4.borrow a book)\n(5.return a book)\n(6.see borrowed books)\n(0.leave): "
        while flag != 0:
            flag = (input(Menu))
            try:
                flag = int(flag)
            except:
                print("You entered a wrong thing, please try only numbers!")
                self.menu()
                break
            if flag ==666:
                pass
            elif flag == 1:
                self.add_book()
            elif flag == 2:
                self.show_books()
            elif flag == 3:
                self.show_unborrowed_books()
            elif flag == 4:
                Book().borrow()
            elif flag == 5:
                Book().return_borrow()  
            elif flag == 6:
                self.show_borrowed_books()
            elif flag == 0:
                print("Thanks for using our library!")
            else:
                print("Seems you Entered wrong number!")
                self.menu()


    def add_book(self): #Does same thing as Hand_add but it's kind of automatic.
        self.inputer()
        book = {
            "Name": self.name,
            "Author": self.author,
            "Year": self.year,
            "Available": True
        }
        self.books.append(book)
        print()

    def show_books(self):
        if len(self.books) == 0: #Checks the number of books
            print("We dont have anything to show you!")
        else:
            print("All books:")
            print("book's name, Author's name, Year, Status\n")
            for book in self.books:
                print(f"{book["Name"]} | {book["Author"]} | {book["Year"]} | {"Available" if book["Available"] else "Unavailable"}")       
        print()

    def show_unborrowed_books(self):
        if len(self.borrowed_books) == len(self.books): #A little bit weird but If we borrow all our books the number of both lists(books and borrowed_books) will be equal so its some how make sense 
            print("Its weird but we dont have any books :(")
        else:
            print("Available books: ")
            print("book's name, Author's name, Year, Status\n")
            for book in self.books:
                if book["Available"] == True: #Checks for only Available books
                    print(f"{book["Name"]} | {book["Author"]} | {book["Year"]} | Available")       
        print()        

    def show_borrowed_books(self):
        if len(self.borrowed_books) == 0:
            print("We did not borrowed anything yet!")
        else:
            print("Unavailable books: ")
            print("book's name, Author's name, Year, Status\n")
            for book in self.borrowed_books:
                print(f"{book["Name"]} | {book["Author"]} | {book["Year"]} | Unavailable") 
        print()
        
class Book(Library):
    def __init__(self):
        pass

    def borrow(self):
        name = input("Please Enter the name of the book: ")
        for book in self.books:
            if book["Name"] == name:
                if book["Available"] == True:
                    book["Available"] = False
                    self.borrowed_books.append(book)
                    print(f"Done\n{name} is borrowed.")
                else:
                    print("It seems it has already been borrowed.")
                return None 
        print(f"We dont have {name}")
    
    def return_borrow(self):
        name = input("Please Enter the name of the book: ")
        for book in self.borrowed_books:
            if book["Name"] == name:
                book["Available"] = True
                self.borrowed_books.remove(book)
                print(f"Done\n{name} has returned to library.")
                return None
        print(f"It seems we didnt borrowed you the `{name}`")
        print("If you think there is an issue, Please report it to manager!") 


#These are only for testing!
# Library().Hand_adding("slavery", "Nigga", 1898)
# Library().Hand_adding("How to become rich", "White", 2020)
Library().menu()


