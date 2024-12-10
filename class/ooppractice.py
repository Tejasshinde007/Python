'''class Student:
    def __init__(self):
        self.name="Tejas"
        self.age=22
        self.grade="a+"
    
    def display_info(self):
        print(self.name,self.age,self.grade)

stud=Student()
stud.display_info()'''


'''class Rectangle:
    def __init__(self,length,width):
        self.length=int(length)
        self.width=int(width)
    
    def area(self):
        return f"area of rectangle is:{self.length*self.width}"

a=Rectangle(20,30)
print(a.area())'''


'''class Car:
    def __init__(self,name,brand,year):
        self.name=name 
        self.brand=brand
        self.year=year
    
    def update_year(self,new_year):
        self.year=new_year
        print(f"Updated year: {self.year}")

a=Car("BMW","M4 compition","2016")
a.update_year("2020")'''


'''class Person:
    name="Unknown"
    age=0
    def show_person(self):
        print(self.name,self.age)

a=Person()
a.show_person() '''   

'''class Bankaccount:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=float(balance)    
    
    def deposite(self,amount):
        self.balance+=amount
        print(f"amount{amount} is credited to {self.account_no}")
    
    def withdraw(self,amount):
        if self.balance  >=amount:
            self.balance-=amount
            print(f"the {amount} id debited from {self.account_no}")
        else:
            print("insufficient Balance")
    def status(self):
        print(self.balance)   

money=Bankaccount("112301",100)

money.deposite(2000) 

money.status() 

money.withdraw(230)   
money.status()'''




'''class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_checked_out=False
    
    def checkout(self):
        if self.is_checked_out:
            print(f"{self.title} is already checked out")
        else:
            self.is_checked_out=True
            print(f"{self.title} is now checked out")
    
    def return_book(self):
        if not self.is_checked_out:
            print(f"{self.title} is not checked out")
        else:
            self.is_checked_out=False
            print(f"{self.title} is now available")

class Library:
    def __init__(self):
        self.book=[]
    
    def add_book(self,book):
        self.book.append(book)
    
    def remove_book(self,isbn):
        book_to_remove=None
        for book in self.book:
            if book.isbn==isbn:
                book_to_remove=book
                break
        if book_to_remove:
            self.book.remove(book_to_remove)
            print(f"Book '{book_to_remove.title}' removed from the library.")
        else:
            print(f"No book found with ISBN: {isbn}")
    
    def list_book(self):
        if not self.book:
            print("Book is not available")
        else:
            print("Listing all the book")
            for book in self.book:
                status="Available"if not book.is_checked_out else "Checked out"
                print(f"{book.title}' by {book.author} (ISBN: {book.isbn}) - {status}")

library = Library()

book1=Book("Python Programming", "John Smith", "12345")

print(book1.title)
    
library.add_book(book1)
library.list_book()    '''





    