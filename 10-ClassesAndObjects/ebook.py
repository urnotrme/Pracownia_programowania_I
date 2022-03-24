class Ebook():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.cpage = 0
        self.open = False
        
    def book_open(self):
        self.open = True
        
    def book_close(self):
        self.open = True
        
    def next_page(self):
        if self.book_open == True:
            if self.cpage<self.pages:
                self.cpage +=1
        else:
            print("Book is closed")
            
    def pre_page(self):
        if self.cpage>2:
            self.cpage -=1