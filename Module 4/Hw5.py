books=["harry potter","matilda","wonder","the jungle book","charlie"]
copy_counts=[2,0,1,6,3]
library={book:count for book, count in zip(books,copy_counts)}
available_books=[book for book in books if library[book]>0]
borrow=input("What book do you want to borrow? ")
if borrow not in library or library[borrow]==0:
    print(borrow,"is not available")
    exit()
late_fees=[4,2,6,3,7]
extra_fees=int(input("Enter extra library fee: "))
updated_fees=list((map(lambda fee: fee+extra_fees,late_fees)))
print(f"""---Summary---
Chosen Book: {borrow}
Updated fee: {updated_fees}
Book Index: {books.index(borrow)}
Book Count: {library[borrow]-1}
""")