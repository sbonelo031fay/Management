import pandas as pd

books = []
members = []

book_id = input("Please enter book ID:")
book_id = int(book_id)

title = input("Please enter book tile:")

author = input("Please enter the Author:")

status = input("Please enter book Status:")

books.append({
     "book_id": book_id,
     "title": title,
     "author": author,
     "status": status
})

print()
member_id = input("Please Enter member ID: ")
member_id = int(member_id)

name = input("Please enter the member's name: ")

members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
})

bks = pd.DataFrame(books)
mbrs = pd.DataFrame(members)

print(bks)
print(mbrs)