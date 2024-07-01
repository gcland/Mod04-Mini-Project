from book import Book
from book import NonFiction
from book import Fiction
from author import Author
from user import User

def add_author(auth_name, authors):   
        biography = []
        authors[auth_name] = Author(auth_name, biography)
        authors[auth_name].add_biography(auth_name)
        print(f"{auth_name} and biography added to Library Management System. ")
        authors[auth_name].get_biography()

def view_author(authors, auth_name):
    authors[auth_name].get_biography()
    try:
        choice = input("Add to author's biography? (yes/no) ")
        if choice == 'yes':
            authors[auth_name].add_biography(auth_name)
    except Exception as e:
            print(f"Error: {e}.")

def display_all_authors(authors):  
    for author in authors:
        print(author)
    try:
        choice = input("View an author's biography? (yes/no) ")
        if choice == 'yes':
            auth_name = input("Enter author name to view biography: ")
            view_author(authors, auth_name)
    except Exception as e:
            print(f"Error: {e}.")

def add_book(library):
    b = 0
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    publish_date = input("Enter book publication date: ")
    for a in library:
        b+=1
    isbn = b+1
    print(f"'{title}' ISBN: {isbn}.")
    genre_ask = input("Add genre details to this book? (yes/no) ")
    if genre_ask.lower() == "yes":
        fict = input("Is this book fiction or nonfiction? ")
        category = input("Enter genre of book: ")
        description = input("Enter a description of the book: ")
        if fict.lower() == 'fiction':
            library[isbn] = Fiction(title, author, isbn, publish_date, category, description)
            library[isbn].get_genrebook_details()
        elif fict.lower() == 'nonfiction':
            library[isbn] = NonFiction(title, author, isbn, publish_date, category, description)
            library[isbn].get_genrebook_details()
        else:
            print("Invalid selection.")
    else:   
        library[isbn] = Book(title, author, isbn, publish_date)
        library[isbn].get_status()

def book_search(library):
    try:
        choice = input("Search book by title or by ISBN? ")
        if choice.lower() == 'isbn':
            isbn = int(input("Input book ISBN: "))
            library[isbn].get_book_details()
        if choice.lower() == "title":
            title = input("Input book title: ")
            for isbn in library:
                if title == library[isbn].get_title():
                    library[isbn].get_book_details()
    except Exception as e:
        print(f"Error: {e}.")

def display_all_books(library, isbn, checked_out):
    int(isbn)
    print(f"\nTitle: {library[isbn].get_title()} by {library[isbn].get_author()}")
    print(f"Publish date: {library[isbn].get_publish_date()}")
    print(f"ISBN: {library[isbn].get_isbn()}")
    if library[isbn].get_status() == True:
        print(f"Availability: Checked-in")
    else:
        print(f"Availability: Checked-out with {checked_out[isbn]}")    

def view_genre(library):
   for isbn in library:
        try:
            library[isbn].get_genrebook_details()
        except:
            library[isbn].get_book_details()

def checkout_book(library, checked_out, users):
    isbn = int(input("Enter ISBN of the book to borrow: "))
    library_ID = int(input("Enter library ID: "))
    # user_name = input("Enter user name: ")
    # for library_ID in users:
    #     if user_name == users[library_ID].get_user_name():
    #         users[library_ID].get_library_ID()
    if isbn in library and library[isbn].borrow_book() and library_ID in users:
        users[library_ID].borrow_book(library[isbn].get_title())
        user_name = users[library_ID].get_user_name()
        checked_out[isbn] = user_name
        print(f"'{library[isbn].get_title()}' checked out with {user_name}.")
    else:
        print("Book checked-out, is not in library, or user ID incorrect.")

def checkin_book(library, checked_out, users):
    isbn = int(input("Enter ISBN of the book to return: "))
    if isbn in library and isbn in checked_out:
        library[isbn].return_book()
        del checked_out[isbn]
        for library_ID in users:
            if library[isbn].get_title() in users[library_ID].get_borrowed_books():
                users[library_ID].return_book(library[isbn].get_title())
        print(f"Book '{library[isbn].get_title()}' checked-in.")
    else:
        print("Invalid ISBN or book is checked-in.")

def add_user(users, user_name):
    borrowed_books = []
    i = 0
    for user in users:
        i+=1
    library_ID = i+1
    users[library_ID] = User(user_name, library_ID, borrowed_books)
    print(f"New user: '{users[library_ID].get_user_name()}' added to Library Management System!")
    print(f"Library ID: {users[library_ID].get_library_ID()}.")

def view_user(users): 
    try:
        choice = input("\nSearch book by user name or by library ID? ")
        if choice.lower() == 'library id' or choice.lower() == 'id':
            library_ID = int(input("Input library ID: "))
            users[library_ID].get_user_details()
        if choice.lower() == "user name" or choice.lower() == "name":
            user_name = input("Input user name: ")
            for library_ID in users:
                if user_name == users[library_ID].get_user_name():
                    users[library_ID].get_user_details()

    except Exception as e:
        print(f"Error: {e}.")

def display_users(users):
    for user in users:
        print()
        users[user].get_user_details()

def main():
    print("\nWelcome to the Library Management System!")
    library = {} #books
    checked_out = {} #borrowed books
    authors = {} 
    users = {}
    while True:
        print("\nLibrary Management System Main Menu:")
        print("\n1. Author Operations\n2. Book Operations\n3. User Operations\n4. Quit")
        choice_main = input("Enter selection: ")
        try:
            if choice_main == '1':
                while True:
                    print("\nAuthor Operations Menu:")
                    print("1. Add a new author\n2. View author details\n3. Display all authors\n4. Return")
                    choice = input("Enter selection: ")
                    try: 
                        if choice == '1':
                            auth_name = input("Enter author name: ")
                            if auth_name in authors:
                                print(f"{auth_name} is already in the Library Management System.")
                            else:
                                add_author(auth_name, authors)
                        elif choice == '2':
                            auth_name = input("Enter author name to view biography: ")
                            view_author(authors, auth_name)
                            pass
                        elif choice == '3':
                            display_all_authors(authors)
                            pass
                        elif choice =='4':
                            break
                    except Exception as e:
                        print(f"Error: {e}.")
            if choice_main == '2':
                while True:
                    print("\nBook Operations Menu:")
                    print("1. Add a book\n2. Check-out a book\n3. Check-in a book\n4. Search for a book\n5. View genre details of all books\n6. Display all books\n7. Return")
                    choice = input("Enter selection: ")
                    try: 
                        if choice == '1':
                            add_book(library)
                        elif choice =='2':
                            checkout_book(library, checked_out, users)
                        elif choice == '3':
                            checkin_book(library, checked_out, users)
                        elif choice =='4':
                            book_search(library)
                        elif choice == '5':
                            view_genre(library)
                        elif choice == '6':
                            for isbn in library:
                                display_all_books(library, isbn, checked_out)
                        elif choice == '7':
                            break
                    except Exception as e:
                        print(f"Error: {e}.")
            elif choice_main == '3':
                while True:
                    print("\nUser Operations Menu:")
                    print("1. Add a new user\n2. Search for user and details\n3. Display all users and details\n4. Return")
                    choice = input("Enter selection: ")
                    try: 
                        if choice == '1':
                            user_name = input("Enter user name: ")
                            if user_name in users:
                                print(f"{user_name} already exists within Library Management System!")
                            else:
                                add_user(users, user_name)
                        elif choice =='2':
                            view_user(users)
                        elif choice == '3':
                            display_users(users)
                        elif choice =='4':
                            break
                    except Exception as e:
                        print(f"Error: {e}.")
            elif choice_main == '4':
                break
        except Exception as e:
            print(f'Error: {e}.')
        finally:
            print("Thank you for using the Library Management System!")
main()