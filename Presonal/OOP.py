# Class:-Class is a blueprint or code template for object creation.

# Object: An object is an instance of a class. It is a collection of attributes (variables) and methods. We use the object of a class to perform actions.

# class Car:
#     def __init__(self,brand,model):
#         data members (instance variables)
#         self.brand=brand
#         self.model=model

# <object-name> = <class-name>(<arguments>)    # Syntax of class

# my_car=Car("BMW","M4 Compition")
# print(my_car.brand)
# print(my_car.model)

# new_car=Car("Mercedese","Mayback")
# print(new_car.brand)



# Adding the functionality to the code

# Class method and self
# problem: add a method to the class Car and print the full name of the car(brand and model)


# class Car:
#     def __init__(self,barnd,model):
#         self.brand=barnd
#         self.model=model

#     Behavior (instance methods)
#     def full_name(self):
#         return f"{self.brand} {self.model}"

# my_car=Car("BMW","M4_compition")
# # for accessing the individual name
# print(my_car.brand)
# print(my_car.model)

# # For accessing the functionality

# print(my_car.full_name())




'''Create a student class that takes name and marks of 3 subjects as argument in constructor.
Then create a method to print the average'''

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("The Student:",self.name,"Gets an average of:",sum/3)

# s1=Student("Tejas",[90,88,70])
# s1.get_avg()