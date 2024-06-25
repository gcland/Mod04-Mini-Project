from book import book
from author import Author

def add_author():
    auth_name = input("Enter author name: ")
    biography = []
    while True:
        bio_add = input(f"Enter book by {auth_name} to add to biography ('end' to finish.): ")
        if bio_add.lower() == "end":
            break
        else:
            biography.append(bio_add)
    author = Author(auth_name, biography)
    print(f"{auth_name} and biography added to Library Management System. ")
    author.get_auth_name()
    author.get_biography()



def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    publish_date = input("Enter book publication date: ")
    isbn = input("Enter book ISBN: ")

    library[isbn] = book(title, author, isbn, publish_date)
    library[isbn].get_status()

def display_all_books(library, isbn, checked_out):
    print(f"Title: {library[isbn].get_title()} by {library[isbn].get_author()}")
    print(f"Publish date: {library[isbn].get_publish_date()}")
    print(f"ISBN: {library[isbn].get_isbn()}")
    if library[isbn].get_status() == True:
        print(f"Status: Checked-in")
    else:
        print(f"Status: Checked-out with {checked_out[isbn]}")
    

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
                            add_author()
                        elif choice =='2':
                            # view_author()
                            pass
                        elif choice == '3':
                            # display_all_authors()
                            pass
                        elif choice =='4':
                            break
                    except Exception as e:
                        print(f"Error: {e}.")
            if choice_main == '2':
                while True:
                    print("\nBook Operations Menu:")
                    print("1. Add a book\n2. Check-out a book\n3. Check-in a book\n4. Search for a book\n5. Genre Operations\n6. Display all books\n7. Return")
                    choice = input("Enter selection: ")
                    try: 
                        if choice == '1':
                            add_book(library)
                        elif choice =='2':
                            checkout_book(library, checked_out)
                        elif choice == '3':
                            checkin_book(library, checked_out)
                        elif choice =='4':
                            # book_search(library)
                            pass
                        elif choice == '5':
                            while True:
                                print("\nGenre Operations Menu:")
                                print("1. Add a new genre\n2. View genre details\n3. Display all genres\n4. Return")
                                choice_genre = input("Enter selection: ")
                                try: 
                                    if choice_genre == '1':
                                        # add_genre(library)
                                        pass
                                    elif choice_genre =='2':
                                        # view_genre(library)
                                        pass
                                    elif choice_genre == '3':
                                        # display_genres
                                        pass
                                    elif choice_genre == '4':
                                        break
                                except Exception as e:
                                    print(f"Error: {e}.")
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
                    print("1. Add a new user\n2. View user details\n3. Display all users\n4. Return")
                    choice = input("Enter selection: ")
                    try: 
                        if choice == '1':
                            #add_user()
                            pass
                        elif choice =='2':
                            #view_user()
                            pass
                        elif choice == '3':
                            #display_users()
                            pass
                        elif choice =='4':
                            break
                    except Exception as e:
                        print(f"Error: {e}.")
            elif choice_main == '4':
                break
        except Exception as e:
            print(f'Error: {e}.')

main()