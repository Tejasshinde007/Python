########################  INHERITANCE   ########################

'''The process of inheriting the properties of the parent class into a child class is called inheritance. 
The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.'''


# Problem : Create an ElectricCar class that inherite from the Car class and has an additional attribute

# class Car:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#     def full_name(self):
#         print(self.name,self.model)

# class ElectricCar(Car):
#     def __init__(self,name,model,battery):
#         super().__init__(name,model)
#         self.battery=battery
        
# my_car=ElectricCar("BMW","M4_Compition","200Kwh")
# print(my_car.name)
# print(my_car.model)
# print(my_car.battery)

# my_car.full_name()   # here we have the access of the function in class Car as well


#####################    Types Of Inheritance   ##########################
# In Python, based upon the number of child and parent classes involved, there are five types of inheritance. 
# The type of inheritance are listed below:

''' 1)Single inheritance'''

'''In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.'''

# # Base class
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')

# # Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')

# # Create object of Car
# car = Car()

# # access Vehicle's info using car object
# car.Vehicle_info()
# car.car_info()




''' 2)Multiple Inheritance '''

'''In multiple inheritance, one child class can inherit from multiple parent classes. 
So here is one child class and multiple parent classes.'''




# 3)Multilevel inheritance
# 4)Hierarchical Inheritance
# 5)Hybrid Inheritance

































