# Encapulation:- process of binding data members and methods into single unit
# class is the example of encapulation

# Access modifiers:

# 1)Public Member:within and outside of class

'''class Public:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        return self.name

obj=Public("tejas")
print(obj.name)   # accessing outside of class
print(obj.show())'''




# 2)Private:-only in class and we cannot access outside method [self.__name=name]

'''class Private:
    def __init__(self,name):
        self.__name=name   # private Data member
    
    def show(self):
        return self.__name
    
    
    

obj=Private("tejas")

# print(obj.name)   # we cannot access outside of class

print(obj.show())
print("My name is:",obj.show())
print("my name is:",obj._Private__name)'''   # access the private variable using mangling method




# 3)Protected:-[self._name=name]

'''class Protected:
    def __init__(self,name,age):
        self._name=name 
        self.age=age
    
    def show(self):
        return self._name

class Sub(Protected):
    def hi(self):
        return self._name

obj=Sub("Tejas",21)

print(obj.hi())
print(obj.show())
print(obj.age)
'''

# Getter and Setter

'''class Protected:
    def __init__(self,name,age):
        self._name=name 
        self.age=age
    
    def show(self):   # getter method
        return self._name
    
    def set_name(self):  #setter method
        self._name="Ashu"
        return self._name

class Sub(Protected):
    def hi(self):
        return self._name

obj=Sub("Tejas",21)

print(obj.hi())
print(obj.set_name())
print(obj.show())
print(obj.age)'''






