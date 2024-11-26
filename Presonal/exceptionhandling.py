# a=input("Enter the number:-")
# print(f"Multiplication of the {a} is:")

# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
    
# print("some line of code")
# print("End of program")

# here if we put some unwanted stuff it will give an error and the workking of the program will stop 
# for such find of cases we use exception handling let's see

# a=input("Enter the number:-")
# print(f"Multiplication of the {a} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")

# except:
#     print("Invalid Input!")  # here we can also customize error

# Output:- Enter the number:-harry
# Multiplication of the harry is:
# Invalid Input!
# some line of code
# End of program

# except Exception as e:
#     print(e)

# Output:-Enter the number:-teha
# Multiplication of the teha is:
# invalid literal for int() with base 10: 'teha'
# some line of code
# End of program
# print("some line of code")
# print("End of program")


# here this will give error but it won't affect the code means code wont stop and run remaining code




# there are many types errors in the program
# and we put multiple except in the code

# try:
#     num=int(input("enter the number:-"))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Index Error")

# Output:-enter the number:-hhd 
# Number entered is not an integer.




# Finally :- why to use it wont affect the code normally it affect the when it is in function

# Example:-

# def fun1():
#     try:
#         l=[1,2,3,4,5]
#         i=int(input("Enter the number:"))
#         print(l[i])
#         return 1
#     except:
#         print("some error")
#         return 0
# #     Enter the number:hs
# #     some error
# #     0
#     # print("i am always printed")  #it will wont print bcz we dont use finally
#     finally:
#         print("I am always printed")
#     # Enter the number:hhd
#     # some error
#     # I am always printed
#     # 0
    
#     # and this is the difference
# x=fun1()
# print(x)



# custome error
# we can give custome error by raise keyword and it will stop the program where the error occurs

# a=int(input("Enter the values between 5 and 9:"))

# if(a<5 and a>9):
#     raise ValueError("Value shound be between 5 and 9")

