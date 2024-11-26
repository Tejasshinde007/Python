#############################     STATIC METHODS   ##############################
'''Methos that dont use self parameters(Work at class level)'''


class Student:
    @staticmethod     # This is Decorator
    def college():
        print("hello")
        
s1=Student()
s1.college()

''''What's a Static Method?
Think of a static method as a function that belongs to a class but doesn't need an instance (an object) of that class to work.
It's like a helper or a tool that you can use without needing all the usual things in the class.'''

'''Why Would We Use a Static Method?
Imagine you have a class, let's say Calculator. Normally, you might make a calculator object to do math with it. 
But what if you just want to add two numbers without keeping track of anything else? 
That's where a static method comes in handy—it lets you do that calculation directly without creating a new Calculator object each time.'''

# EX:-

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

result=Calculator.add(2,3)   # Here we don't need to create object we just call the function
print(result)

# problems

class Geometryhelper:
    @staticmethod
    def area_of_circle(a):
        pi=3.14
        return a*pi
    
    @staticmethod
    def area_of_triangle(width,height):
        print("Area:",width*height)

print(Geometryhelper.area_of_circle(24))

Geometryhelper.area_of_triangle(20,30)

