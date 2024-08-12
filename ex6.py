# lecture 64 
# Create library management 

class Library:
    def __init__(self , noBo):
        self.noBooks = 0
        self.books = []


    def adBooks(self , books):
      self.books.append(books)
      self.noBooks = len(self.books)

    def showInfo(self):
       print(f"The library has {self.noBooks} books.")  


l1 = Library()
l1.addBook("harry potter1")
l1.addBook("harry potter2")
l1.showInfo()



     
