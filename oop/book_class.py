class Book:
    def __init__(self, title : str, author : str, year : int):
        self.book_title = title
        self.book_author = author
        self.book_year = year

    def __del__(self):
        print(f"Deleting {self.book_title}")
    
    def __str__(self):
        print (f"{self.book_title} by {self.book_author}, published in {self.book_year}")

    def __repr__(self):
        print(f"Book('{self.book_title}', '{self.book_author}', {self.book_year})")