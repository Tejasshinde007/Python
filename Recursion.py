# Recursion Function:-Function call itself called as fecursive function
# Advantages 
# 1) we can reduce length of the code and improve readability
# 2) we can solve complex problem very easily

# ex:fact(3)=3*fact(2)
#            3*2*fact(1)
#            3*2*1*fact(0)
#            3*2*1*1


# WAP to print factorial

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         result=n*fact(n-1)
#     return result

# print(fact(4))
# print(fact(5)) 
            


# Anonymous(means nameless) Function:
#          sometimes we can declare a function ny name,such type of nameless functions are called anonymous function or lambda function

# Syntax:=   lambda argument_list(Parameters) : expression


# WAF to write a square of number

# def squr(n):
#     return n**2
# print(squr(11))

# squr=lambda n : n**2
# print(squr(5))


# Add 2 numbers

# add=lambda x,y : x+y
# print(add(2,5))

# greater number
# def greter(x,y,z):
#     if(x>y and x>z):
#         return x
#     elif y>z:
#         return y
#     else:
#         return z

# print(greter(4,3,2))

# Using lambda
# g=lambda a,b,c : a if a>b and a>c else b if b>c else c    # in lambda while applying if else it dosent take elif
# print(g(2,1,4))


# Fibonacci Series

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# t=10
# print(fib(t))


# Sum of Array Elements

# a = [1, 2, 3, 4, 5]

# def sum_array(arr, n):
#     if n == 0:
#         return 0
#     else:
#         return arr[n - 1] + sum_array(arr, n - 1)

# print(sum_array(a, len(a)))

# Sum of Digits

# def sum_digit(n):
#     if n==0:
#         return 0
#     else:
#         return n%10 + sum_digit(n//10)
    
# print(sum_digit(1011))


# Cube of number using lambda function

# a=lambda x:x**3
# print(a(4))


