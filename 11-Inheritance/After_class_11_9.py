class Book():
    def __init__(self, title, autor, year, genre):
        self.title = title
        self.autor = autor
        self.year = year
        self.genre = genre
        
class Paper_book(Book):
    def __init__(self, title, autor, year, genre, pages):
        super().__init__(title, autor, year, genre)
        self.pages = pages
        
    def present(self):
        a = f"Paper book\nTitle:\t{self.title}\nAutor:\t{self.autor}\nYear:\t{self.year}\nGenre:\t{self.genre}\nPages:\t{self.pages}"
        print(a)
        
        
class e_book(Book):
    def __init__(self, title, autor, year, genre, file):
        super().__init__(title, autor, year, genre)
        self.file = file
        
    def present(self):
        a = f"E-book\nTitle:\t{self.title}\nAutor:\t{self.autor}\nYear:\t{self.year}\nGenre:\t{self.genre}\nFile:\t{self.file}"
        print(a)    
        
pb1 = Paper_book("Atlas of the Heart", "Brené Brown", "2021", "self-help book", "336")
pb1.present()
eb1 = e_book("Atlas of the Heart", "Brené Brown", "2021", "self-help book", "pdf")
eb1.present()
    