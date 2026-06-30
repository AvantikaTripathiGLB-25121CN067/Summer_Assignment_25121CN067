books=[]

def add_book(book_id,title,author):

    """Adds a new book record."""
    book={
        'id':book_id,
        'title':title,
        'author':author
    }

    books.append(book)
    print(f"Added: {title}")

def remove_book(book_id):

    """Removes a book by its ID."""
    global books
    books= [b for b in books if b ['id'] !=book_id ]
     
    print(f"Removed book with ID: {book_id}")

def display_books():

    """Displays all books in library."""
    print("\n--- Current Book List---")

    if not books:
        print("Library is currently empty.")
    else:
        for b in books:

           print(f"ID:{b['id']}   Title:{b['title']}    Author:{b['author']}")
    print("-------\n")

add_book(101,"A Suitable Boy","Vikram Seth")
add_book(102,"The Guide","R.K. Narayan")
add_book(103,"Midnight's Children","Salman Rushide")

display_books()

remove_book(101)
display_books()

    



