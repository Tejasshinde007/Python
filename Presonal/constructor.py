##########################   Constructors in python   ###############
# What is Constructor in Python?
# In object-oriented programming, A constructor is a special method used to create and initialize an object of a class. 
# This method is defined in the class.
# The constructor is executed automatically at the time of object creation.

''' Example: Create a Constructor in Python  '''

# class Student:
#     def __init__(self,name):
#         print("Inside constructor")
#         self.name=name
#         print("all variable initialized")
        
#     def show(self):
#         print("Hello,my name is:-",self.name)
    
# my_name=Student("Tejas")
# print(my_name.name)

# # Accessing the function
# my_name.show()


''' Types of constructor '''
# 1)Default Constructor
# 2)non-parameterized Constructor
# 3)parameterized Constructor

''' 1) Default Constructor  '''

# class Employee():
#     def display(self):
#         print("Inside Display")

# emp=Employee()
# emp.display()

'''2) Non-Parameterized Consructor'''

# class Car:
#     def __init__(self):
#         self.name="BMW"
#         self.model="M4 Compitation"
#     def show(self):
#         print("My favourite Car is",self.name,"and my fav. model is",self.model)

# my_car=Car()
# print(my_car.name)
# print(my_car.model)

# my_car.show()


'''3)Parameterized Constructor'''

# class Student:
#     def __init__(self,name,surname):
#         self.name=name
#         self.surname=surname
    
#     def show(self):
#         print("My name is",self.name,self.surname)

# stud_name=Student("Tejas","Shinde")
# print(stud_name.name)
# print(stud_name.surname)

# stud_name.show()



'''Constructor With Default Values'''

# class Student:
#     # constructor with default values age and classroom
#     def __init__(self, name, age=12, classroom=7):
#         self.name = name
#         self.age = age
#         self.classroom = classroom

#     # display Student
#     def show(self):
#         print(self.name, self.age, self.classroom)

# # creating object of the Student class
# emma = Student('Emma')
# emma.show()

# kelly = Student('Kelly', 13)
# kelly.show()


'''Constructor Overloading'''

'''Python does not support constructor overloading. If we define multiple constructors then, the interpreter will considers only 
the last constructor and throws an error if the sequence of the arguments doesn't match as per the last constructor.'''

# class Student:
#     # one argument constructor
#     def __init__(self, name):
#         print("One arguments constructor")
#         self.name = name

#     # two argument constructor
#     def __init__(self, name, age):
#         print("Two arguments constructor")
#         self.name = name
#         self.age = age

# # creating first object
# emma = Student('Emma')          # it will give error it does not matches with 2 constructor

# # creating Second object
# kelly = Student('Kelly', 13)

# Output:-TypeError: Student.__init__() missing 1 required positional argument: 'age'



'''                       Constructor Chaining                        '''

'''Constructor chaining is the process of calling one constructor from another constructor.'''
'''Using the super() method we can invoke the parent class constructor from a child class.'''

# class Car:
#     def __init__(self,name):
#         print("inside Car")
#         self.name=name
    
# class Brand(Car):
#     def __init__(self,name,brand):
#         print("inside Brand")
#         super().__init__(name)
#         self.brand=brand
        
# class Model(Brand):
#     def __init__(self, name, brand,model):
#         print("inside Model")
#         super().__init__(name, brand)
#         self.model=model

# my_car=Model("4 wheel","BMW","M4 compition")
# print(f"Car:={my_car.name},Brand={my_car.brand},Model={my_car.model}")


'''Problem: Bookstore Inventory System'''

# class Product:
#     def __init__(self,product_id,name,price):
#         self.product_id=product_id
#         self.name=name
#         self.price=price
# class Book(Product):
#     def __init__(self,product_id,name,price,author,ISBN):
#         super().__init__(product_id,name,price)
#         self.author=author
#         self.ISBN=ISBN

# book=Book("B001","PYTHON","29.99","John Deo","1234567890")

# print("Product_ID:",book.product_id)
# print("Name:",book.name)
# print("Price:",book.price)
# print("Author:",book.author)
# print("ISBN",book.ISBN)  


'''Counting the Number of objects of a Class'''

# class Employee:
#     count=0
#     def __init__(self):
#         Employee.count=Employee.count+1
        
# e1=Employee()
# e2=Employee()
# e3=Employee()
# e4=Employee()
      
# print("Number of Employees:",Employee.count)

















