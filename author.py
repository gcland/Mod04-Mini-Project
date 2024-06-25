class Author:
    def __init__(self, auth_name, biography):
        self.auth_name = auth_name
        self.biography = biography

    def get_auth_name(self):
        return self.auth_name

    def get_biography(self):
        print(f"{self.auth_name} Biography:")
        for book in self.biography:
            print(book)