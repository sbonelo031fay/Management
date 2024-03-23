import pandas as pd

books = pd.DataFrame(columns = ["book_id", "title", "author", "status", "borrowed_books"])
members = pd.DataFrame(columns = ["membe_id", "name", "borrowed_books"])

#function for new book
def add_book(book_id, title, author, status, borrowed_books):
    new_book = {"book_id": book_id, "title": title, "author": author, "status": status, "borrowed_books": [borrowed_books]}
    books.loc[len(books)] = new_book

#function for new member
def add_member(member_id, name):#this is a function
    new_member = {"member_id": member_id, "name": name}
    members.loc[len(members)] = new_member


add_book(1, "Python", "Jacob", "Avail", 0)

add_member(11, "Jane")

print(books)
print(members)

    





