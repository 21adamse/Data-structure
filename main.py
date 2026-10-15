class LibraryBook():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True
    def borrowbooks(self):
        if self.is_available:
            print("You borrowed",self.title)
            self.is_available = False
        else:
            print("Sorry",self.title,"is already borrowed")
    def returnbooks(self):
        if not self.is_available:
            print("You returned",self.title)
            self.is_available = True
        else:
            print("You do not have",self.title)
book = LibraryBook("Harry Potter","J.K.Rowling")
book.borrowbooks()
book.borrowbooks()
book.returnbooks() 
book.returnbooks()
