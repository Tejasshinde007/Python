##############################   LOOPS IN PYTHON   #########################

#1)WHILE LOOP:-The while loop statement repeatatly execut a code block while a perticular condition is true

# i=1
# while i<=5:
#     print("hii",i)
#     i+=1


#print num from 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1

#print num form 5 to 1
# i=5
# while i>=1:
#     print(i)
#     i-=1


#multiplication table
# i=1
# n=int(input("Enter the number:-"))
# while i<=10:
#     print(n*i)
#     i+=1


#print the number using the following list

# num=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<=len(num)-1:
#     print(num[i])
#     i+=1


############ search the number x in the tuple using the loop ##########

# num=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter thr number:-"))
# i=0
# while i < len(num):
#     if(num[i]==x):
#         print("found at index",i)
#     else:
#         print("Founding..")
#     i+=1


##########  Keyword in while loop  ###########


#1)Break:-we can use break inside the loop execution based on the some condition


#EX:-

# n=7
# for i in range(1,10):
#     if i==n:
#         print("we found 7 and we break loop",i)  #loop is break bcz we found 7 so we break loop by break
#         break
#     print(i)
    


#2)Continue:-we can use continue statement to skip current iteration and continue next iteration


#EX:-

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

#3)PASS:-Pass is a keyword in python ,pass is a empty statement,pass is null statement,i you want to define empty block then we should go for the pass

#EX:-

# for i in range(5):
#     pass 


#4)Del:- after using the variable,it is highly recommended to delete that variable if it is no longer required,
#           so that corresponding is into the garbage collection,we can delete variable ussing the del 



############################   FOR LOOP   ###########################


# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:         
#     print(i)

# list=[1,2,3,4,5,6,7,8,9,10]
# n=5
# a=0
# for i in list:
#     if i==n:
#         print("number found",a)
#         break
#     a+=1

# WAP TO find the sum of the numbers
# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

#WAP program to find out the first n number factorial

# n=5
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)



#### Reversed the loop  ####

# num=[20,30,40,50]
# for i in reversed(num):
#     print(i)
    
# #OUTPUT
# 50
# 40
# 30
# 20






