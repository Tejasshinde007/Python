######### Dictionary And Sets ###################

######## Dictionary ########

# a={
#     "name":"Tejas",
#     "age":22,
#     "marks":[22,333,44],
#     "subject":("Phy","Chem","Bio")
# }


# a["age"]=33
# a["marks"].append("mark")  #For the updation int he list int the dictionary
# a["marks"].pop(3)          #for the removing the name int the list
# print(a)

####### nested dictionaries ####
# a={
#     "name":"Tejas",
#     "Subject":{
#         "phy":84,
#         "chem":94,
#         "math":98
#     }
# }

# print(a)
# print(a["Subject"])  #for printion only nested dictionary
# print(a["Subject"]["math"]) #for accessing the value int the nested list



#########  Methods in the dictionary ###########


#1)mydict.keys() #return all keys
# a={
#     "name":"Tejas",
#     "Subject":{
#         "phy":84,
#         "chem":94,
#         "math":98
#     }
# }

# print(a.keys())  #here the nested keys wont be dislayed
# print(list(a.keys()))   #we can convert into list
# print(len(a.keys()))  #we can print the length of the dictionary

#2)mydict.values() #return all the values
# a={
#     "name":"Tejas",
#     "Subject":{
#         "phy":84,
#         "chem":94,
#         "math":98
#     }
# }

# print(a.values())
# print(list(a.values()))  #we can convert  into list

#3)mydict.items() #return all {key,value} pair as tuple
# a={
#     "name":"Tejas",
#     "Subject":{
#         "phy":84,
#         "chem":94,
#         "math":98
#     }
# }

# print(a.items())
# pair=list(a.items())  #convert to list
# print(pair[0])       #access the list by indexing

#4)mydict.get("key") #return the key according to the value
# a={
#     "name":"Tejas",
#     "Subject":{
#         "phy":84,
#         "chem":94,
#         "math":98
#     }
# }

# print(a["name"])
# print(a.get("name"))  #here both will give me the same output but the difference is in wechange the "key name" ex:-

# print(a["name1"])  # this will give an error if error occurs next line wont perform

#ths why we use this method
# print(a.get("name1"))  #this wont give the error but give none(means no such key is present)

#5)mydict.update(new_dict or new {key,value} pair) #we can pass new_dict or new {key,value} pair
# a={
#     "name":"Tejas",
#     "Subject":{
#         "phy":84,
#         "chem":94,
#         "math":98
#     }
# }

# a.update({"core":"design"})
# print(a)

# new_dict={"city":"Delhi","age":22}
# a.update(new_dict)
# print(a)



############################### SETS ####################

# a={1,2,2,"Hello",4}
# print(a)               #here the duplicate values wont be printed
# print(type(a))


#if we want to create empty set we write

# a=set()
# print(a)

# bcz if we create a={} it will be showed as empty dictionary



#################  methods in set  ################


#1)set.add(element) #add the new element in set

# a={1,2,3,4}
# # a.add(6,7)  #it will give an error bcz set take only 1 argument as input
# a.add(5)
# print(a)


#2)set.remove(element)  #remove element in sets

# a={1,2,3,4,5}
# a.remove(4)
# print(a)


#3)set.clear()  # create empty set

# a={1,2,3,"hello"}
# a.clear()
# print(a)


#4)set.pop()  #pop/remove the remdon value or number

# a={1,2,3,"hello","hii","wooo"}
# print(a.pop())
# print(a)


#5)set1.union(set2)  #combine both set values and return new

# a={1,2,3}
# b={2,3,4}
# print(a.union(b))  #here the dublicate value are niglected 


#6)set1.intersection(set2) #combines the common values and return the new

# a={1,2,3}
# b={2,3,4}
# print(a.intersection(b))



###############  Examples  ############

#1. add the following words in the dictionary
# a={
#     "table":["a piece of furniture","list of facts"],
#     "cat":"a small animal"
# }

# print(a)

#2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. 
# How many classrooms are needed by all students

# a={"python","java","c++","python","javascript","c"}
# print(len(a))

#3 WAP to add 3 subject marks in an empty dictionary

# a={}
# a.update({"python":200})
# a.update({"C++":300})
# a.update({"OOP":400})
# print(a)





