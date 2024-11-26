# 1)Factorial
# def fact(n):
#     a=1
#     for i in range(1,n+1):
#         a=a*i
#     print(a)

# fact(5)

# 2)prime number checker

# def prime(n):
#     c=0
#     for i in range(2,n):
#         if n%i==0:
#             c+=1
#     if c==0:
#         print("prime")
#     else:
#         print("not prime")
            

# prime(int(input("Enter the number:-")))

# 3)Palindrome Checker:

# def pali_check(n):
#     if n==n[::-1]:
#         print("palindrom")
#     else:
#         print("not a palindrom")

# pali_check("ABCDCBA")

# 4)string reverse

# def rev_string(n):
#     print(n[::-1])
    
# rev_string("Tejas")

# 5)sum of square

# def sum_squr(n):
#     a=[]
#     for i in range(1,n+1):
#         c=i**2
#         a.append(c)
#     return a
# print(sum_squr(5))

# 6)Count Vowels in a String:

# def vowel(n):
#     a="aeiou"
#     c=0
#     for i in n:
#         if i in a:
#             c+=1
#     print(c)
# vowel("Tejas")

# 7)Fibonacci Sequence:

# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
# fib(10)

# 8)Unique Elements in a List:

# a=[1,2,3,2,4,2,3,5,3,6,4,7,6,8,7,9,8,8,10]
# def unique_element(a):
#     return list(set(a))
# print(unique_element(a))

# 9)Sorting a List Using Lambda:

# lst = [1, 4, 32, 5, 3, 6, 5, 7, 4]

# def sort_by_length(lst):
#     return sorted(lst, key=lambda x: len(str(x)))  

# print(sort_by_length(lst))


