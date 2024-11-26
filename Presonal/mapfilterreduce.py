

# ###################    Map filter and reduce take the function as a argument   ######################

##################### Syntax map(function,iterable) iterable means list,tuple,etc.


#####################  we can use Without function by lambda function as i mention below 

# MAP():-The map function lets you apply a certain operation to every item in a collection (like a list). 
# It's like telling Python, “Do something to each item in the list.”

# #Used for:-The map() function is used when you want to apply the same operation to every item in a collection. 
# #It's useful for transformations, like changing all items in a list in some way (e.g., doubling numbers, converting strings to lowercase, etc.).


'''l=[1,2,3,4,5]
def squre_num(l):
    a=[]
    for i in l:
        c=i**2
        a.append(c)
    print(a)
squre_num(l)'''

# It is very lenthy process to reduce this we use map
# 1st we have to def function

''' def squr(n):
     return n**2
 print(squr(3))'''  

# l=[1,2,3,4,5,6]

# # it is the short process we neet just define functionand call 
'''newl=list(map(squr,l))   #we have take the function as a argument(squr)
print(newl)''' 

# using lambda function

'''numbers = [1, 2, 3, 4]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))'''

# WAP that uses the map() function to convert each string to an integer and then find the sum of all the numbers.

'''l=["1","2","3","4","5","6"]
integer=map(int,l)
total_sum=sum(integer)
print(total_sum)'''

# Use map() to add 5 to each number in a list of ages
'''l=[1,2,3,4,5]
newl=list(map(lambda x:x+5,l))
print(newl)'''




#######################    FILTER()   ###################################################

# Filter():-The filter function helps you choose certain items from a collection based on a condition. 
# It’s like saying, “Give me only the items that meet this rule.”


# Used for:-he filter() function is used when you want to keep only the items in a collection that satisfy a condition. 
# It's useful for selecting specific items from a list (e.g., filtering out odd numbers or picking words that start with a certain letter).

'''l=[1,3,4,5,6,7,2]
def filter_fun(a):
    return a>4
newl=list(filter(filter_fun,l))      #It is used for the conditional purpose
print(newl)'''

# using lambda function

# l=[1,2,3,4,5,6]
# newl=list(filter(lambda x:x>=4,l))
# print(newl)




##################################   REDUCE()   #######################
'''# Here we have to first import the function'''

# he reduce function is a bit different. Instead of changing each item, 
# it takes all the items in a collection and combines them into a single value. It "reduces" the list to one final result.

# USED FOR:- he reduce() function is used when you want to combine all the items in a collection into a single value. 
# It's helpful for operations like summing numbers, multiplying all items, or even more complex operations like finding the maximum or the product of all items.

'''from functools import reduce'''

# Example find the sum of list by lambda function
'''l=[1,2,3,4,5]
newl=reduce(lambda x,y:x+y,l) 
print(newl)'''

# taking the function as an argument
'''l=[1,2,3,4,5]
def sum(x,y):
    return x+y

newl=reduce(sum,l)
print(newl)'''

