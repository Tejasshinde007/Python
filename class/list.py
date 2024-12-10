###########    LIST    ############
# List:-Lists are used to store multiple items in a single variable.
# Lists are created using square brackets


# Accessing the list 

# 1)indexing:-
# a=[1,2,3,4,"tejas"]
# print(a[2])

# 2)slicing:-
# a=[1,2,3,4,5,"tejas"]
# print(a[2:4])

#using foor loop:-
# a=[1,2,3,4,5,"tejas"]
# for i in a:
#     print(i)

#usiong while loop:-
# a=[1,2,3,4,5,"tejas"]
# i=0
# while i<len(a):
#     print(i)
#     i+=1


#######################   Functions of the list  ###################
# a=[1,2,3,6,"tejas"]

# 1)len():-
# print(len(a))

# 2)count():-
# print(a.count(2))

# 3)append():-used to add the elements at the last of the string
# a.append("Shinde")
# print(a)

# 4)insert():-used to add the elements in the list at any position by using the indexing
# a.insert(3,5)
# print(a) 

# 5)extend():-wwe can add multiple elements and as well as the another list (but it will add at the end o the list)
# a.extend([4,5,7,8,9])
# print(a)

# 6)remove():-we can remove the specific item from the list by remove
# a.remove("tejas")
# print(a)

# 7)pop():-we can also remove the item using pop by their indexing
# a.pop(2)  # 2 is the index number
# print(a)

# 8)clear():-used to clear all the elements from the list
# a.clear()
# print(a)

# 9)sort():-The sort function sorts the elements in the list in ascending order.
# b=[2,3,1,5,3,6]
# b.sort()
# print(b)

# 10)reserved():-The reverse function is used to reverse the elements in the list.
# a.reverse()
# print(a)









# l=[1,2,3,4,"hello"]
# print(l[4][0:3])

# lis=[10,20,30,40,50,60]
# for i in lis:
#     print(i)

# lis=[10,20,30,40,50,60]
# n=len(lis)
# c=0
# while n>0:
#     print(lis[c])
#     c+=1
#     n-=1


#List Comprehension:-
# it is very easy and compact way of creating list object from iterable object
# a=[1,2,3,4,5]
# squ_list=[i**2 for i in a]     #make big code into single line
# print(squ_list)


# a=[1,2,3,4,5]
# squ_list=[i**2 for i in range (1,11)if i%2==0]     #make big code into single line
# print(squ_list)

# a=[9,3,4,5,11,334,2,1]
# a.sort()    #use to arrange in sequence
# print(a)

#          1st method but in interview it has no value   for find the largest number
# a=[9,3,4,5,11,334,2,1]
# a.sort()
# print(a[-1])

#print max number
# a=[9,3,4,5,11,334,2,1]
# b=a[0]
# for i in a:
#     if i > b:
#         b=i
# print(b)

#print 2 max number
# a=[9,3,4,255,11,334,260,2,1]
# max=a[0]
# max2=a[0]
# max3=a[0]
# for i in a:
#     if i > max:
#         max3=max2     #only use for third max
#         max2=max      #only use for second max
#         max=i
#     elif i>max2 and i!=max:     #second max
#         max2=i
#     elif i>max3 and i!=max2:    #third max
#         max3=i
# print(max3)



#WAP to remove duplicate from the list
# l=[1,2,34,5,61,2,4,62,5,2,34]
# a=[]
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a)

