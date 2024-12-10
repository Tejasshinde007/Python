#String:-any sequence of character which is enclosed in single,double,triple coat is called string in the python

# a='Tejas' 
# a="Tejas"
# a='''Tejas'''     #we can define string by this types as well
# a="""Tejas"""
# print(a)


#Accessing the string element
#1)Indexing:-is the address is given to the each element of the string

# a="Hello"
# print(a[1])

#2)Slicing:-to fetch the part of the string

#a[start:end:steps]

# a="Hello World"
# print(a[0:3])
# print(a[0:6:2])#DEFAULT Step is 1  #steps means the difference we want in the string

# print(a[8:11])  #OR  print(a[8:len(a)])  print(a[8:])
# print(a[::2])


#negative indexing :- it always start with -length and ends with -1
# a="Hello"
# print(a[-5:])
# print(a[::-1])




###################### ACESSING the string element using for loop:

# s="Python"
# for i in s:
#     print(i)



#WAP to accept string from the user and display its chracter by index

# s=input("Enter the sring:-")
# for i in range(len(s)):
#     print(s[i],"=",i)

#Accessing string element using while loop
# s=input("Enter the sring:-")
# i=0
# while i<=len(s):
#     print(s[i])
#     i+=1


#######################  WAP to swap to variable  ###########################
#Without using the 3rd variable  1st logic     ##############  ASKED IN INTERVIEW  #########################
#it is only used in python
# a=10                                     
# b=20
# a,b=b,a
# print(a)
# print(b)

#Without using the 3rd variable  2st logic
# a=5
# b=15
# a=a+b  #a=20
# b=a-b  #b=5
# a=a-b  #a=15
# print(a,b)


#Without using the 3rd variable  2st logic
# a=5
# b=15
# a=a*b  #a=75
# b=a//b  #b=5
# a=a//b  #a=15
# print(a,b)

#using the 3rd variable
# a=5
# b=15
# temp=a
# a=b
# b=temp
# print(a,b)


#####################################  Mathematical Operation on string ##################################

# #1)+ operation for concatenation
# a="Tejas"
# b=" Shinde"
# print(a+b)

#2)* operator for repetition
# a="Tejas"
# print(a*5)   #print string 5 times



#WAP to access each character of string forward and backward direction


#Forward
# s="Learning Python is very easy!!!"
# i=0
# while i<len(s):
#     print(s[i],end=" ")
#     i+=1
# print(s[:len(s)])
# print(s[::-1])


#Backward
# s="Learning Python is very easy!!!"
# i=-1
# while i>-len(s):
#     print(s[i],end=" ")
#     i-=1



#Comparison of string

# print('A'>'a')


#inbuild function on string
#1)find():-returns index of first occurance of the given substring.if it is not available then we will get -1

# s="Learning Python is very easy"
# print(s.find("e"))

#2)index():-it is exactly same as find() method except that if the specified substring is not available then we will get valueerror

#IQ what id=s difference between index and find ############

#3) Count():-used to find the number of occurances of the substring of given string and if substring not there then it will give 0
# s="abbassjjgoiajgbja"
# print(s.count("a"))


#WAP to find the number of the occurances of substring present in string ? without using count function

# s="anndnajjajajajjdvins"
# a='a'
# c=0
# for i in s:
#     if i == a:
#         c+=1
# print(c)


#4)Replace function:-inside s, every occurance of old sting with new string
# a="Tejas Shinde"
# print(a.replace("Shinde","Nalge"))

#5)len():-return a length of a present element in a string

# a="Tejas Shinde"
# print(len(a))

#6)Split():- is used to split the given string according to specified seperator the default seperator is space the return type of split method is list

# a="Pyhton is very easy programming"
# l=a.split()                            #default
# print(l)
# ['Pyhton', 'is', 'very', 'easy', 'programming']  #output


# a="Pyhton is very easy programming"
# l=a.split("y")                             #by a character 
# print(l)
# ['P', 'hton is ver', ' eas', ' programming']   #output



#7)join():-we can join a group of string(list or tuple) wrt the given seperator.default seperator for join is (,)
# s=seperator.join(group of string)   #syntax
# a=["sunny","munny","dhani"]
# s=" ".join(a)
# print(s)
# sunny munny dhani  #output


# a=["sunny","munny","dhani"]
# s="_".join(a)
# print(s)
# sunny_munny_dhani   #output


#############      changing case of a string     ##########
#1)upper()
# a="TejasShinde"
# print(a.upper())  #output   TEJASSHINDE

#2)lower()
# a="TejasShinde"
# print(a.lower())    #output   tejasshinde

#3)swapcase()
# a="TejasShinde"
# print(a.swapcase())   #output  tEJASsHINDE

#4)title()
# a="TejasShinde is a very good"
# print(a.title())        #output   Tejasshinde Is A Very Good

#5)capitalize()
# a="TejasShinde is a very good"
# print(a.capitalize())     #output  Tejasshinde is a very good

###########  Checking stARTING AND ENDING PRAT OF THE STRING  ###########

#1)starstwith():-
# a="TejasShinde"
# print(a.startswith("T"))
#output   True


#2)endswith():-
# a="TejasShinde"
# print(a.endswith("de"))
#output   True

##########  Check type of character of the string  #################
# Python contains the following methods for this purpose.

# 1) İsalnum(): Returns True if all characters are alphanumeric( a to z, A to Z,0 to9)

# 2) Isalpha(); Returns True if all characters are only alphabet symbols(a to z,A to Z)

# 3) Isdigit(); Returns True if all characters are digits only(0 to 9)

# 4) İslower(); Returns True if all characters are lower case alphabet symbols

# 5) Isupper(); Returns True if all characters are upper case aplhabet symbols

# 6) İstitle(): Returns True if string is in title case

# 7) Isspace(); Returns True if string contains only spaces

# ER:

# print('Durga786'.Isalnum()) #True

# print('durga786'.isalpha())  #False

# print('durga'.Isalpha()) #True

# print('durga'.Isdigit()) #False

# print('786786'.Isdigit()) #True

# print('abc'.islower()) #True

# print('ABC'.isupper()) #True

# print(' '.isspace())  #True


#WAP to print addition of numbers present in a given string
# a="abc123cd"
# sum=0
# for i in a:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)

# a="a4b3c2"
# s=""
# for i in a:
#     if i.isalpha():
#         s+=i
#         p=i
#     elif i.isdigit():
#         s=s+(p*(int(i)-1))
# print(s)

# s="a4k3p2"
#output=aeknpr
# a='a4k3p2' 
# s=""
# for i in a:
#    if i.isalpha():
#        s+=i
#        p=i
#    elif i.isdigit():
#          s=s+chr(ord(p)+(int(i)))
# print(s) 

#WAP to remove duplicate character from the given input string

# a=input("Enter the string:-")
# c=""
# for i in a:
#     if i in c:
#         continue
#     else:
#         c+=i      
# print(c)

#output:-Enter the string:-aabbccjjaf
# abcjf

# a=input("Enter the string:-")
# c=""
# for i in a:
#     if i not in c:
#         c+=i     
# print(c)


