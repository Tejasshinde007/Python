# def cal_sum(a,b):
#     return a+b
# print(cal_sum(1,2))

# default argument:

# def cal_sum(a=1,b=2):
#     sum=a+b
#     return sum
# print(cal_sum())  # here the output will be 3 bcz of default parameter

# WAP to print length of the list without usig length function
# a=[1,2,3,4,"tejas","shinde"]

# def len_list(list):
#     c=0
#     for i in a:
#         c+=1
#     print(c)
# len_list(a)

# WAF to find the factorial of n

# def fact_n(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f)
# fact_n(5)

#WAF to convert the USD to INR

# def usd_inr(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"USD","=",inr_val,"INR")
# usd_inr(5)

# WAF take input from user and print it is even or odd
# 1) we can take input from user from this way
# a=int(input("Enter the number:-"))
# def guss(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")

# guss(a)
# 2) we can take input from from this way
# def guss(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")

# guss(a=int(input("Enter the number:-")))


# s="howyoucow"

# def dup(s):
#     e=""
#     c=""
#     for i in s:
#         if i not in e:
#             e=e+i
#         else:
#             c=c+i
             
#     print(e,end=" ")
#     print(c)
        
# dup(s)

