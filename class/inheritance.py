# Inheritance :-The process of inheriting the properties of the parent class into a child class is called inheritance.


'''class A:
    def hello(sself):
        print("Calling class A show method")
        
    def hey(self):
        print("Calling hey method of A")

class B(A):
    def bee(self):
        print("Calling Bee of Class B")
        
obj=B()
obj.hello()
obj.hey()
obj.bee()
'''
# Single inheritance
'''class Car:
    def Super_Sports(self):
        print("Super Sports : BMW")
    
    def Comfort(self):
        print("Comfortable Car : Mayback")
class Vehical(Car):
    def Family(self):
        print("Family Car : XUV 3XO")
    
    def Boys(self):
        print("Boys Car : Thar")

My_car=Vehical()
My_car.Super_Sports()
My_car.Boys()
My_car.Family()
My_car.Comfort()'''


# Multilevel inheritance: a child class is derived from child class

'''class A:
    def show(self):
        print("Calling Show")

class B(A):
    def bee(self):
        print("Calling bee")

class C(B):
    def see(self):
        print("Calling See")

class D(C):
    def display(self):
        print("calling display")

obj=D()    # here we have to create object for child class bcz it have the properties of parent class
obj.show()
obj.display()
obj.bee()
obj.see()'''

# multiple inheritance:a single child class which is derived from multiple parent class

'''class X:
    def show(self):
        print("Calling Show")

class Y:
    def display(self):
        print("Calling display")

class Z(X,Y):
    def see(self):
        print("Calling See")

obj=Z()
obj.display()
obj.show()
obj.see()'''

# hierarchical inheritance: single parent and multiole child

'''class A:
    def show(self):
        print("Calling A")

class B(A):
    def see(self):
        print("Calling B")
        
class C(A):
    def display(self):
        print("calling C")

obj=B()
obj.show()
obj.see()

obj1=C()
obj1.show()
obj1.display()'''


# Hybrid inheritance:it the combination of two or more typle of inheritance

'''class A:
    def show(self):
        print("Calling A")

class B(A):
    def see(self):
        print("Calling B")

class C(A):
    def display(self):
        print("Clling C")

class D(B,C):
    def hello(self):
        print("Clling D")

obj=D()
obj.show()
obj.see()
obj.display()
obj.hello()'''




















