#################################    Encapulation    ###########################
# Encapulation is the process of d=binding the data into single unit

''' Access modidfiers in python:-'''

'''Access modifiers limit access to the variables and methods of a class.'''

# 1)Public Member:- access anywhere from outside of class

'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def show(self):
        print("Name:",self.name,"Salary:",self.salary)

emp1=Employee("Tejas","1,20,000")
emp1.show()'''


# 2)Private Member:- Accessible only within the class
# (To define a private variable add two underscores as a prefix at the start of a variable name.)

''' EG. self.__salary=salary'''

'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary    # private class
    
    # def show(self):
    #     print("Name:",self.name,"Salary:",self.__salary)

emp1=Employee("Tejas","1,20,000")
# emp1.show()
print("Salary:",emp1.__salary)''' # here it will give an error bcz we cannot acces the private class outside of the class



# For accesing the private class:-

'''Access Private member outside of a class ""using an instance method""'''

'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary    # private class
    
    # Instance method
    def show(self):
        print("Name:",self.name,"Salary:",self.__salary)

emp1=Employee("Tejas","1,20,000")
# print("Salary:",emp1.__salary)

emp1.show() '''  # it will not give error bcz we acces by instance method


# Name Mangling to access private members
# Syntax:- (_classname__dataMember)

'''We can directly access private and protected variables from outside of a class through name mangling. 
The name mangling is created on an identifier by adding two leading underscores and one trailing underscore,
like this _classname__dataMember, where classname is the current class, and data member is the private variable name'''


'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary    # private class


emp1=Employee("Tejas","1,20,000")

print("Salary:",emp1._Employee__salary)'''  # access the private member using mangling 



# 3)Protected Members:- Protected members are accessible within the class and also available to its sub-classes.

'''To define a protected member, prefix the member name with a single underscore _.

Protected data members are used when you implement inheritance and want to allow data members access to only child classes.'''

'''class Company:
    def __init__(self,project):
        self._project=project    #  Protected class

    def pro(self):
        print("Project is:",self._project)
class Employee(Company):
    def __init__(self, project,name):
        super().__init__(project)
        self.name=name
    
    def show(self):
        print("Employee name:",self.name)
        
        print("Working on a project:",self._project)

emp1=Employee("Python full stack","Tejas")
emp1.show()

comp = Company("Python full stack")
comp.pro()'''



# Getters and Setters in Python

'''To implement proper encapsulation in Python, we need to use setters and getters. 
The primary purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
Use the getter method to access data members and the setter methods to modify the data members'''

'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        
    def get_age(self):     # By getter method we can access the data member
        return self.__age
    
    def set_age(self,age):  # By setter emthod we can modify the data member
        self.__age=age

stude=Student("Tejas",22)

print("Name:",stude.name,"Age:",stude.get_age())

stude.set_age(23)

print("Name:",stude.name,"Age:",stude.get_age())'''






