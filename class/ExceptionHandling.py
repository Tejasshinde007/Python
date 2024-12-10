# 1)Syntax error:
# The error which occurs because of invalid syntax are called syntax error 

# 2)Runtime error :
# it is exception

# Syntax:
# try:
#     //risky Code 
# except:
#     //handle error
#    # executed when exception occured in the try block


try:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print(a/b)
    
except ZeroDivisionError:
    # except block execute when any exception occurs in try block
    print("sorry we cant divide by zero")

except TypeError:
    print("please enter  number only")

except ValueError:
    print("Please enter number only")

else:
    print("no exception in the try block")

finally:
    # This will always executed
    # after and except block
    print("Its finally")


# else block with try-except-finally

# else block will be executed if and only if there are no Exception inside try block 


'''try:
    Risky Code 
    
except:
    will be executed if exception inside try block
    
else:
    will be executed if there is no exception inside try block

finally:
    will be executed whether Exception raised or not raised and handled or not handled'''









