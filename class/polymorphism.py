# Ploymorphism:-Ability ot take many forms

# Method overriding:same method but differen classes
'''class A:
    def show(self):
        print("Class A")
        
class B(A):
    def show(self):
        print("Class B")

obj=B()
obj.show()'''

# method overloading : same method name with differen parameters


'''def show(a,b):
    return a+b 

def show(a,b,c):
    return a+b+c'''

# print(show(10,20))   #it will give error  #it will not consider the latest method will be consider (means 3 argument method will be consider)
# print(show(10,20,30)) # it will not give bcz it is lates one 