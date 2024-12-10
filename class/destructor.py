# Destructor is basically delete 

class Disc:
    def __init__(self,name):
        self.name=name
        print("Tejas calling ")
    
    def show(self):
        return self.name
    
    def __del__(self):   # it will call only if we are deleting the object(but in the vs code it is printing if we dont call the del it is the problem of vs code in idle it work properly)
        print("Calling Destructor")
        
obj=Disc("tejas")
print(obj.show())

# here we are deleting the object by del
del obj

print(obj.show())  # it give error bcz we have deleted the obj

