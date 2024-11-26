##############   Python Class Variables   ##############

class Car:
    # Class variable
    name="BMW"
    # Cobstructor
    def __init__(self,model,owner):
        # instance variable
        self.model=model
        self.owner=owner
    # # Instance method
    def fullname(self):
        return f"Car company is {Car.name} and the model of it is {self.model} and it's Owner is {self.owner}"


''' Accessing the class variable '''
mycar=Car.name
print(mycar)


''' Accessing the Method '''
# Create object
car=Car("M4","Tejas")
print(car.model)
print(car.owner)

print(car.fullname()) 

''' Modify Object'''
car.model="Aventador"
print(car.model)

'''Modify Class Variables'''

Car.name="Lamborgini"
print(Car.name)     # if we Modify Class Variables using the class variable it makes permentely changes

''' Modify class variable using object reference'''

car.name="Ferrari"
print(car.name)      #  if we modify class variable using object reference it is the temerory changes not permenent 

'''Class Variable Vs. Instance Variable'''

'''Instance variables: The instance variable’s value varies from object to object. Objects do not share instance variables. 
 Every object has its copy of the instance attribute.'''

'''Class Variables: A class variable is a variable that is declared inside of a class but outside of any instance method or init() method. 
 Class variables are shared by all instances of a class.'''

print(Car.name,car.model,car.owner)





























