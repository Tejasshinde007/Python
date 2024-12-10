##############    SET     ################
# If we want to represent a group of unique values as a single entity then we should go for the set
# Duplicate are not allowed 
# insertion order is not preserved but we can sort the element
# indexing and slicing are not allowed for the set
# heterogeneous elements are allowed
# set object are mutable i.e. once we create set object we can perform any changes in that object based on the requirement
# we cam represent set element within thecurly braces and with comma seperation 
# we can apply mathematical oprerations like union,intersection,difference,etc on set object


# s={1,4,3,5,6,72,5,7}
# print(s,type(s))


# a={}
# print(type(a))     #output will show dictionary 

#to define empty set 
# b=set()
# print(type(b))


#Accessing set elements 

# indexing and slicing are not allowed for the set

#using for loop
# a={1,2,4,3,5,7}
# for i in a:
#     print(i)

#using while loop we cannot access set bcz of indexing

#important function of set
#len():-
# s={1,4,3,5,6,72,5,7}
# print(len(s))

#add():-
# s={1,4,3,5,6,72,5,7}
# s.add("tejas")
# print(s)

#remove():- here if we remove the value not present in the set then it will give keyerror
# s={1,4,3,5,6,72,5,7}
# s.remove(4)
# print(s)

#discard():- here if we remove the value not present in the set then it will not give error
# s={1,4,3,5,6,72,5,7}
# s.discard(50)
# print(s)

#update():-individual object are not allowed we should update by list,set,set
# s={1,4,3,5,6,72,5,7}
# s.update([20,30,40])
# print(s)

#copy():-returns copy of the set.  it is a clone object
# s={1,4,3,5,6,72,5,7}
# a=s.copy()
# print(a)

#pop():-it remove and return some ramdom element
# s={1,4,3,5,6,72,5,7}
# print(s.pop())

# Mathematical perations on the set:

#1.union():-it used to return all element presents sets
# x={1,2,3,4,5}
# y={4,5,6,7,8}
# print(x.union(y))
# #OR
# print(x|y)

#2.Intersection():-returns common elements for both sets
# x={1,2,3,4,5}
# y={4,5,6,7,8}
# print(x.intersection(y))
# #OR
# print(x&y)

#3.Difference():-returns the element present in x but not in y
# x={1,2,3,4,5}
# y={4,5,6,7,8}
# print(x.difference(y))
# #OR
# print(x-y)

#4.symmetric_difference():-Returns elements present in either x or y but not in both
# x.symmetric_difference(y) or x^y
# x={10,20,30,40} 
# y={30,40,50,60} 
# print(x.symmetric_difference(y)) #10, 50, 20, 60) 
# print(x^y) #{10, 50, 20, 60)

# Set Comprehension:-it is possible
#find even number
# s={1,2,3,4,5,6,7,8,9,10}
# b={i for i in s if i%2==0}
# print(b)

