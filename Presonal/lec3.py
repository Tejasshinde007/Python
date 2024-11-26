################# List and Tuple #########################

###################################### List ##############################

# a=[2,1,4,3]
# print(a[2])  #print the string using index number


######## List are mutable(means we can change value inside list) and we also add different datatype value as well ##########

# a=["tejas",1,"Ashu",3]
# a[2]="Ritesh"  ######## here we havew update the value
# print(a)
# print(len(a))  ######## here we have print the length of the string




##############  list Slicing  ##############

# [  -6,  -5,  -4,  -3,-2,-1]
# a=["Tejas",2,"Shinde",3,5,8]
# print(a[1:3])
# print(a[:5])
# print(a[2:])
# print(a[-3:-1])
# print(a[::-1])  #it is used to reverse the string



#############  List Methods ##################

#1)list.append():- is basically used to  add element at last

# a=[2,1,3,4,5]
# a.append(10)  
# print(a)

#i)list.insert(index,value):-used to add element at index we want to insert
# a=[2,1,3,4]
# a.insert(2,100)
# print(a)

#ii)list.extend([2,3,2]):-used to extend list
# a=[1,2,3,4]
# a.extend([5,6,7])
# print(a)

#2)list.sort():- it is bascially used to sort element in ascending order

# a=[2,1,3,4,5]
# a.sort()
# print(a.sort())  # if we printthe sort function it dosen't return any value means it return NONE 
# print(a)

#3)list.sort(reverse=True):- sort elements in descending order

# a=[2,1,3,4,5]
# a.sort(reverse=True)
# print(a)

#4)list.reverse():- used to reverse the list

# a=[2,1,3,4,5]
# a.reverse()
# print(a)

#5)list.insert(idx,element):- used to add element at the index we want

# a=[2,1,3,4,5]
# a.insert(2,"tejas")
# print(a)

#6)list.remove(value which we want to remove):-used to remove the value by the occurance means the element we provide comes first get removed

# a=[2,1,3,1,5]
# a.remove(1)
# print(a)

#7)list.pop(index which we want to remove):-used to remove elemnt by the index number

# a=[2,1,3,4,5]
# a.pop(2)
# print(a)

#8)list.clear():-used to delete the items int the list
# a=[1,2,3,4,5]
# a.clear()
# print(a)

# Concatenation of two lists

# my_list1 = [1, 2, 3]
# my_list2 = [4, 5, 6]

# # Using + operator
# my_list3 = my_list1 + my_list2
# print(my_list3)
# # Output [1, 2, 3, 4, 5, 6]

# # Using extend() method
# my_list1.extend(my_list2)
# print(my_list1)

#Using max() & min()

# mylist = [3, 4, 5, 6, 1]
# print(max(mylist)) #returns the maximum number in the list.
# print(min(mylist)) #returns the minimum number in the list.

#Using sum()

# a=[1,2,3,4,5]
# print(sum(a))

######################################   Tuple  #####################################

# #creation of tuple
# a=(1,2,3,4)
# print(a)
# print(type(a))

# inserting the single value in the tuple we writr (1,) bcz if we dont put (,) after the value python take the value as integer
# a=(1,)
# print(a)

#### Slicing in the tuple ######
# a=(1,2,3,4)
# print(a[1:3])

######## Tuple Methods ########

# #1)tup.index(element):-used to write the index of th first occurance of the element
# a=(1,2,1,3,1)
# print(a.index(2))

#Finding an item in a Tuple

# The index() method accepts the following three arguments
# 1.item – The item which needs to be searched
# 2.start – (Optional) The starting value of the index from which the search will start
# 3.end – (Optional) The end value of the index search

# a=(1,2,3,4,5,6)
# print(a.index(4,1,len(a)))

#Find within a range

# tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
# # Limit the search locations using start and end
# # search only from location 4 to 6
# # start = 4 and end = 6
# # get index of item 60
# position = tuple1.index(60, 4, 6)
# print(position)  

#Checking if an item exists

# a=[10,20,30,40]
# print(50 in a)
# print(20 in a)

# #2)tup.count(element):-used to count the element present in the tuple
# a=(1,2,21,1,3,1)
# print(a.count(1))



################### Examples ##########

#1 enter the 3 movie name and store in the list
# list=[]
# a=input("Enter the 1 st movie name:-")
# b=input("Enter the 1 st movie name:-")
# c=input("Enter the 1 st movie name:-")
# list.append(a)
# list.append(b)
# list.append(c)
# print(list)

#### OR anothe method ######

# list=[]
# list.append(input("Enter the 1 st movie name:-"))
# list.append(input("Enter the 1 st movie name:-"))
# list.append(input("Enter the 1 st movie name:-"))

# print(list)

























