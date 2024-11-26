###########################    IT is very important topic for django     ######################## 
# if we want to represent the key value pair the we use Dictionary
# Dictionary is the group of key value pair which is represented by curly braces ({ })
# Syntax:{key:value,
#         key:value,
#         etc..}

# d={1:1,2:4,3:9,4:16,5:25}
# print(d,type(d),len(d))

# dict={"name":"tejas",
#       "course":"python",
#       "classes":"It vedant",
#       "Batch":"P432",
#       "rollno":45}
# print(dict)


# ######### Here Key Should be unique(duplicate key is not allowed) but the value can duplicate  ##########
# ########  Indexing and slicing is not allowed (it gives key error)  ################

# ###  Accessing the dictionary   #######

# # We can access the dictionary key 
# print("<------------------------------------------------------------------------------------------------>")

# print(dict["name"])
# print(dict["Batch"])
# print(dict["course"])


# # Update the dictionary
# print("<---------------------------------------------------------------------------------------------->")

# dict["name"]="Don"   # it is used to update the present key value pair
# print(dict)

# # Add new key value pair
# print("<---------------------------------------------------------------------------------------------->")

# dict["age"]=22   # if the key value is not present in the dictionary it will add the key value pair
# print(dict)


# # Delete the element from dictionary

# # it delete entry ofa key value pair
# # if the key value pair is not present it give keyerror
# print("<------------------------------------------------------------------------------------------------>")

# del dict["classes"]
# print(dict)

# # to delete the complete dictionary
# # del dict

# # clear():-it empty the dictionary
# print("<---------------------------------------------------------------------------------------------->")

# dict.clear()
# print(dict)


# print("<---------------------------------------------------------------------------------------------->") 

# # Function in dictionary

# d=dict()    #create dictionary
# print(type(d))

# print("<---------------------------------------------------------------------------------------------->")

# eval()is used to take the input from user as per the inputed date it defines its type
# d1=eval(input("Enter Dictionary "))
# print(d1,type(d1))

# get():-
# print(dict.get("name"))

# pop():-it remove entry associated with the specific key and return the corresponding value
# if the specified key is not available then it will give keyerror
# dict.pop("rollno")
# print(dict)     # output:-{'name': 'tejas', 'course': 'python', 'classes': 'It vedant', 'Batch': 'P432'}  here the rollno is poped
# print(dict.pop("name"))
# print(dict)      #output:-tejas
#                        {'course': 'python', 'classes': 'It vedant', 'Batch': 'P432', 'rollno': 45}

# pop item():-it is used to delete and return last inserted item from the dictionary
# if the dictionary is empty it give keyerror 
# print(dict.popitem())


# key():-is used to return all keys from dictionary
# print(dict.keys())

# values():-is used to return all the values from dictionary
# print(dict.values())

# items():-it returns list of tuple represent key value pair
# print(dict.items())
# output:-dict_items([('name', 'tejas'), ('course', 'python'), ('classes', 'It vedant'), ('Batch', 'P432'), ('rollno', 45)])


#update


# cardict2 = {'price' : 1254221,}
# cardict.update(cardict2)
# print(cardict)

# Dictionary Comprehension : 
# it is very easy way to creating list from any iterable object
# dict  compr : 

# {exp:value for i in iterable_object}

# y = {i:i**2 for i in range(1,11)}
# print(y)
 
 
# WAP to print sum of numbers

# a={1:20,2:86,3:4,4:33}
# s=0
# for i in a.values():
#       s+=i
# print(s)    

# WAP to find number of occurances of each letter present in string and store in dictionary
# s="aabbcdefabced"
# d={}
# for i in s:
#       d[i]=s.count(i)
# print(d)  

# Given a string, count the frequency of each word in the string using a dictionary.
# text = "hello world hello everyone"
# word=text.split()
# f={}
# for i in word:
#       f[i]=f.get(i,0)+1
# print(f)

