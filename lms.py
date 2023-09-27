
class a_library():
    def __init__(self,list_of_books):
        self.books=list_of_books
        self.data={}

    def display(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(book)
    
    def add(self,bookname):
        print(f"Thank you for adding a book into this library.\nNew book {bookname} is added to library:")
        self.books.append(bookname)

    def borrow(self,bookname,name):
        if bookname in self.books:
            self.data[bookname]=name
            print(f"The book {bookname} has been issued to {name}.\nPlease keep it safe and return the book within 30 days: ")
            self.books.remove(bookname)
        else:
            print(f"Sorry {bookname} is not available or has been issued to someone.\nPlease wait until book is available: ")

    def returnbook(self,bookname):
        if bookname in self.data:
            print(f"This book is borrowed by {self.data[bookname]}")
            r=input("If you want to return the press: Y\n otherwise press any key to skip:\n-->")
            if r =="y":
                del self.data[bookname]
                print("Thank you for returning the book.\nHope you like it:")
                self.books.append(bookname)
            else:
                pass
        else:
            print("This book is not given by our library.\nIf you want to give this book please add this book:")
            
def main():
    lib = a_library(["harry potter","python","java","machine language","oop","dc_comics","marvels"])
    welcome ='''\n  =====Welcome to the Library=====
    Please Choose an opyion:
    1. List all available books
    2. Add new book to the Library
    3. Borrow a book
    4. Return a book
    5. Exit the Library
    '''
    while (True):
        print(welcome)
        a=int(input("Enter your choice\n-->"))
        if a==1:
            lib.display()
        elif a==2:
            n=input("Enter book name you want to add:\n-->")
            lib.add(n)
        elif a==3:
            b=input("Enter book name you want to borrow:\n-->")
            c=input("Enter your name:\n-->")
            lib.borrow(b,c)
        elif a==4:
            r=input("Enter book name you want to return:\n-->")
            lib.returnbook(r)
        elif a==5:
            print("Thanks for chosing our library:")
            exit()
        else:
            print("Invalid Choice:")

main()