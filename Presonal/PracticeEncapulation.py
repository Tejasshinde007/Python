# Problem: Book Library Management System

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.__price=price
    
    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        if price<0:
            print("Price cannot be negative. Setting price to 0.")
            self.__price = 0
        else:
            self.__price=price
            
book=Book("Python Programming", "John Doe", 29.99)
print(book.get_price())

book.set_price(-1)
print(book.get_price())