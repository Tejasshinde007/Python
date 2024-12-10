######################        FUNCTIONS     ###############################

# Function is a block of code define with a name 

# def:-is used to return Value
# return:-it returns output value form function

# Syntax:-
# def function_name(parameters):   #parameters are input of the function also called as arguments 
#     '''doc string'''
#     return value


# user define function types
# 1 non parameterized function 
# 2 parameterized function

# 1 non parameterized function 

# we can call function using function name

# def fun():
#     return "Hello this is my first non parameterize function"   # return store the value in it 

# print(fun())


# def fun1():
#     print("Hello this is my second non parameterize function")  #print display the value

# fun1()

# # 2 parameterized function

# def addition(a,b):
#     return a+b
# print(addition(4,3))

# print(addition(10,30))


# def sub(a,b):
#     return a-b
# print(sub(20,10))


# def multi(a,b):
#     return a*b
# print(multi(20,10))


# WAP a given function to check the given num is even or odd

# def evenodd(num):
#     if num%2==0:
#         return "even" 
#     else:
#         return "odd"
    
# print(evenodd(10))

# WAP to find factorial
# def fact(num):
#         f=1
#         for i in range(1,num+1):
#             f=f*i
#         return f
            
# print(fact(5))


# 3) Default argument

# def wish(name="Tejas"):
#     print("Hello",name,"how are you")
# wish("Nalge")   #Here we have pass the parameter and the default paramete "Tejas" will not taken bcz we have pass the parameter 
# wish()

# 4) variable length argument

# def sum(*n):              # *n means it is tuple and we give multiple inputs
#     t=0
#     for n1 in n:
#         t=t+n1
#     print("The sum=",t)

# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30,40)








