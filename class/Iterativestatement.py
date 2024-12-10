#itrative statements

#1)for loop :- i)range(start,end,steps):-

# print(range(11))

# for variable in range(n):
    #body of for loop

# for i in range(1,11,1):
#     print(i)

# print("we use here set step 2")
# for i in range(0,11,2):
#     print(i)

#WAP to print even number between 0 to 100

# for i in range(0,101,1):
#     if i%2!=0:
#         print(i)
        
#WAP to check given number is prime or not

# a=int(input("Enter the number:-"))
# for i in range(2,a-1):
#     if a%a==0 and a%1==0:
#         print("prime number")
#     else:
#         print("not a prime")

#WAP a program to print count of even nmber 0 to 100

# count=0
# for i in range(1,101):
#     if i%2==0:
#         count+=+1

# print(count)


#WAP to check given number is prime or not

# num=int(input("Enter the number:-"))
# c=0
# for i in range(1,num+1):
#     if num%i==0:
#         c+=1
# if c>2:
#     print("not prime number")
# else:
#     print("prime number")

###### OR  ##########

# num=int(input("Enter the number:-"))
# c=0
# for i in range(2,num):
#     if num%i==0:

#         c+=1
# if c==0:
#     print("prime number")
# else:
#     print("not prime number")


######### OR  for time complixity  #########
# num=int(input("Enter the number:-"))
# c=0
# for i in range(2,num//2+1):
#     if num%i==0:
#         c+=1
# if c==0:
#     print("prime number")
# else:
#     print("not prime number")

#While loop in python:- The while loop statement repeatatly execut a code block while a perticular condition is true
#number of iteration is unknown
#Syntax:-

#while condition/expression:
                    #while loop code/block of while loop
                    #increment/decreament

# i=100
# while i>=1:
#     print(i)
#     i-=1

#WAP TO print even number within 0 to 100 using while loop

# i=0
# while i<=100:
#     if i%2==0:
#         print(i)
#     i+=1
    
#WAP TO print odd number within 0 to 100 using while loop

# i=0
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i+=1    


#WAP take input from user 10 times and print it
# i=1
# while i<=10:
#     a=int(input("Enter the number:-"))
#     i+=1

#WAP to print goodafternoon 10 times in 2 lines
# for i in range(0,10):
#     print("Good Afternoon")

# i=0    
# while i<=10:
#     print("Good afternoon")
#     i+=1
    







