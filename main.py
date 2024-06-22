from book import book

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    publish_date = input("Enter book publication date: ")
    isbn = input("Enter book ISBN: ")

    library[isbn] = book(title, author, isbn, publish_date)
    library[isbn].get_status()

def checkout_book(library, checked_out):
    isbn = input("Enter ISBN of the book to borrow: ")
    user = input("Enter user name: ")
    if isbn in library and library[isbn].borrow_book():
        checked_out[isbn] = user
        print(f"'{library[isbn].get_title()}' checked out with {user}.")
    else:
        print("Book checked-out or is not in library.")

def checkin_book(library, checked_out):
    isbn = input("Enter ISBN of the book to return: ")
    if isbn in library and isbn in checked_out:
        library[isbn].return_book()
        del checked_out[isbn]
        print(f"Book '{library[isbn].get_title()}' checked-in.")
    else:
        print("Invalid ISBN or book is checked-in.")
    
def main():
    print("\nWelcome to the Library Management System!")
    library = {} #available books
    checked_out = {} #borrowed books
    while True:
        print("\nLibrary Management System Main Menu:")
        print("\n1. Add Book to Library\n2. Check-out Book\n3. Check-in Book\n4. Quit")
        choice = input("Enter selection: ")
        try:
            if choice == '1':
                add_book(library)
            elif choice == '2':
                checkout_book(library, checked_out)
            elif choice == '3':
                checkin_book(library, checked_out)
            elif choice == '4':
                break
            else:
                print('Invalid choice.')
        except Exception as e:
            print(f'Error: {e}.')

main()