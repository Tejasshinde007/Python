# for(i=1;i<n;i+2) cpp
# for i in range(1,n,2) py

'''
*
**
***
****
*****
'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
    

'''
*****
****
***
**
*
'''

# for i in range(1,6):
#     for j in range(1,6-i):
#         print("*",end=" ")
#     print()

'''    
*****
 ****
  ***
   **
    *
'''
# n=6
# for i in range(1,n):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for k in range(1,n-i+1):
#         print("*",end=" ")
#     print()

'''
2
4 6
8 12 14
16 18 20 22
'''
# n=7
# a=2
# for i in range(2,n):
#     for j in range(2,i):
#         print(a,end=" ")
#         a+=2
#     print()

''' 
a 
b c 
d e f 
g h i j
''' 
# a=97
# for i in range(97,102):
#     for j in range(97,i):
#         print(chr(a),end=" ")
#         a+=1
#     print()


'''
a 
b b 
c c c 
d d d d 
e e e e e 
'''

# for i in range(97,102):
#     for j in range(97,i+1):
#         print(chr(i),end=" ")
#     print()

'''
    *
   **
  ***
 ****
*****
'''
# n=6
# for i in range(1,n):
#     for j in range(1,n-i):
#         print(" ",end=" ")
#     for k in range(1,i):
#         print("*",end=" ")
#     print()


#Factorial Program
# f=1
# n=int(input("Enter the number:-"))
# for i in range(1,n+1):
#     f*=i
# print(n,"!:",f)



# diamond pattern 

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''
 
# n=5
# for i in range(1,n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()



#prime number

# num=int(input("Enter the number:-"))
# c=0
# for i in range(2,num):
#     if num%i==0:
#         c+=1
# if(c==0):
#     print("Prime number")
# else:
#     print("not a prime number")
    
    
#amstrong number

# n=int(input("enter the number:-"))
# b=n
# y=len(str(n))
# d=0
# while b>0:
#     c=b%10
#     c=c**y
#     d+=c
#     b=b//10
# if d==n:
#     print("it is armstrong")
# else:
#     print("it is not armstrong")


