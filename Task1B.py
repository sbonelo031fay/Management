import pandas as pd

books = []
members = []

def add_book():
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
    bks = pd.DataFrame(books)
    return bks

def add_member():#this is a function
    print()
    member_id = input("Please Enter member ID: ")
    member_id = int(member_id)

    name = input("Please enter the member's name: ")

    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
    })
    mbrs = pd.DataFrame(members)
    return mbrs

bks = add_book()
mbrs = add_member()

print(bks)
print()
print(mbrs)