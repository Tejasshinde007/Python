# Class method

class Person:
    course="Full Stack in Pyhton"    # class variable
    def __init__(self,name):
        self.name=name   # instance Variable
        
        print(self.name)
    
    @classmethod
    def display(cls):
        return cls.course

obj=Person("Tejas")

print(Person.display())