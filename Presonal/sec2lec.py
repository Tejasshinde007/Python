# str1="Hii my name is tejas What'sup"
# print(str1)


# ################     escape sequence characters  ##############
# a="My name is:\n Tejas"
# print(a)
# b="this is\t tab space"
# print(b)

###########################  Basic operation  ####################

# #Concatenation
# a="tejas"
# b="Shinde"
# print(a+b)
# print(len(a))

# #Indexing
# a="Tejas Shinde"
# print(a[4])
# print(a[5]) #it prints space as well

###########################  Slicing  ##########################

# a="Tejasshinde"
# print(a[2:5])
# print(a[5:len(a)]) #till last index
# #OR
# print(a[5:])

# #negative index
# a="APPLE"
# print(a[-5:-2])

#########################   String Function  ######################


#1)str.endswith("name")  #it only give True and False

# a="Tejas"
# print(a.endswith("s"))
# print(a.endswith("a"))

#2)str.capitalize()  #Print 1st letter in Capital
# a="tejasshinde"
# print(a.capitalize())  #For more read My notes

#3)str.replace("old","new")  # replace old string to new
# a="Tejas Nalge"
# print(a.replace("Nalge","Shinde"))

#4)str.fild("String") #return the first index of first occurance
# a="Tejasshinde"
# print(a.find("s"))
# print(a.find("shinde"))

#5)str.count("string") #counts the occurance of the substring in the string
# a="my home is away from my home"
# print(a.count("my"))
# print(a.count("m"))

#########  for more function go to the page pynative.com  ################



######################  Conditional Statements   ###########################################

# marks=int(input("Enter your marks:-"))
# if(marks>=90):
#     grade="A"
# elif(marks<90 and marks>=80):
#     grade="B"
# elif(marks<80 and marks>=70):
#     grade="C"
# else:
#     grade="D"
    
# print("Grade of the Student is:-",grade)


#Given number is Even or ODD:


# no=int(input("Enter thr number:-"))
# if(no%2==0):
#     number="Even"
# else:
#     number="Odd"
# print("The given number is:-",number)


#Greate number among 3 number:


# a=int(input("Enter thr number:-"))
# b=int(input("Enter thr number:-"))
# c=int(input("Enter thr number:-"))

# if(a>=b and a>=c):
#     print(a)
# elif(b>=c):
#     print(b)
# else:
#     print(c)


year=int(input("Enter the year:-"))

if(year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("not a leap year")
