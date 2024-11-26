###############   Tuple    ###########################
# tuple is collection of comma seperated values and it is immutable and it is heterogeneous type of data
# a=(1,2,4,3.0,"tejas")
# print(type(a))


#accessing tuple element using indexing

# a=(1,2,4,3.0,"tejas")
# print(a[1])

#accessing tuple element using slicing
# a=(1,2,4,3.0,"tejas")
# print(a[1:3])

#accessing tuple element using for loop
# a=(1,2,4,3.0,"tejas")
# for i in a:
#     print(i)

#accessing tuple element using while loop
# a=(1,2,4,3.0,"tejas")
# i=0
# while i < len(a):
#     print(a[i])
#     i+=1

#print number of count in tuple without using count function
# a=(1,2,4,2,5,4,4)
# b=4
# c=0
# for i in a:
#     if b==i:
#         c+=1
# print(c)
        

#print the sum of the tuple
# a=(1,2,3,4,5,6,7,8,9,10)
# sum=0
# for i in a:
#     sum+=i
# print(sum)

#################  fuctions   ##########    
#Sorted():-
# t=(40,10,30,20)
# t1=sorted(t)
# print(t1)

# #cmp():
# it compares the element of both tuples.
# if both tuples are equal the teturn 0
# if the frst tuple is less than second tuple then it returns -1
# if the frst tuple is greater than second tuple then it returns +1

#cmp is not available in python 3 version

# #tuple packing
# a=10
# b=20
# c=30
# tuple=a,b,c
# print(tuple,type(tuple))

# #tuple unpacking for unpacking we need to be packed

# a,b,c=tuple
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))


#tuple comprehension is not applicable in python it create generator output



