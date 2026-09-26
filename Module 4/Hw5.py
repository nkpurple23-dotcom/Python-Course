books=["harry potter","matilda","wonder","the jungle book","charlie"]
copy_counts=[2,0,1,6,3]
library={book:count for book, count in zip(books,copy_counts)}
available_books=[book for book in books if library[book]>0]
borrow=input("What book do you want to borrow? ")
