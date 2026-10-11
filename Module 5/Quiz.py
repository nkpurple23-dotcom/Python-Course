books=["matilda","harry potter"," the jungle book"]
print(books)
book=input("What book do you want to borrow? ")
class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        self.is_borrowed=True
        print("You have borrowed", self.title)
    def return_book(self):
        self.is_borrowed=False
        print("You have returned", self.title)
if book=="harry potter":
    jk=Book("Harry Potter","JK Rowling")
    jk.borrow()
    jk.return_book()
elif book=="matilda":
    hn=Book("Matilda","Henry")
    hn.borrow()
    hn.return_book()
elif book=="jungle book":
    kt=Book("The Jungle Book","Kate")
    kt.borrow()
    kt.return_book()