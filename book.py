class book:
    def __init__(self, title, author, isbn, publish_date):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publish_date = publish_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_status(self):
        return self.__is_available
    
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False
    
    def return_book(self):
        self.__is_available = True
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publish_date(self):
        return self.__publish_date


class Nonfiction(book):
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

class Fiction(book):
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category