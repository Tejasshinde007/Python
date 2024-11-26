# Reading the File

# 1)f.read():-it will read the complete file

# f = open("D:\\PYTHON\\Presonal\\text.txt", "r")
# data=f.read()
# print(data)
# output:-  Hi my name
#           is tejas


# 2)f.readline():-read one line at time

# f = open("D:\\PYTHON\\Presonal\\text.txt", "r")
# data=f.readlines()
# print(data)
# f.close()



# Writing to the file

# 1)"w"

# f=open("D:\\PYTHON\\Presonal\\text.txt","w")
# print(f.write("desi gang"))
# f.close()

# 2)"a"
# f=open("D:\\PYTHON\\Presonal\\text.txt","a")
# data=f.write("\nThis is my code")    # \n for the new line
# print(data)
# f.close()

# 3)"r+"
# # without a+ data
# desi gang
# This is my code

# f=open("D:\\PYTHON\\Presonal\\text.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

# output with using r+
# abci gang
# This is my code

# if we print data it will start data with i

# print(f.read())
# i gang
# This is my code

# "w+"
# without w+
# desi gang
# This is my code

# f=open("D:\\PYTHON\\Presonal\\text.txt","w+")
# f.write("abc")
# print(f.read())
# f.close()

# after w+
# abc     #it truncate the whole data and the print

# "a+"
# without a+
# Desi gang
# This is my code

# f=open("D:\\PYTHON\\Presonal\\text.txt","a+")
# f.write("abc")
# print(f.read())
# f.close()

# after a+
# Desi gang
# This is my codeabc


# With Syntax

# with open("D:\\PYTHON\\Presonal\\text.txt","r") as f:    # same as this     # f = open("D:\\PYTHON\\Presonal\\text.txt", "r")
#     data=f.read()                                                           # data=f.read()
#     print(data)                                                             # print(data)

# same as for the write("w")



#######################   Problems   #######################
# WAP to replace java to pyhton

# with open("D:\\PYTHON\\Presonal\\Practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("java","Python")    
# print(new_data)

# # we have again write the which we have replaced
# with open("D:\\PYTHON\\Presonal\\Practice.txt","w") as f:
#     f.write(new_data)



# WAP to fing the word learning exits or not

# with open("D:\\PYTHON\\Presonal\\Practice.txt","r") as f:
#     data=f.read()
#     if(data.find("learning")!=-1):
#         print("found")
#     else:
#         print("notfound")


# WAF to find in which line of the file does the word "learning" occurs first.
# print -1 if word not fount

# def check_for_line():
#     word="learning"
#     line_no=1
#     data=True
#     with open("D:\\PYTHON\\Presonal\\Practice.txt","r") as f:
#         while word:
#             data=f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no +=1
#     return -1
# check_for_line()


# find the even numbers in the file seperated by comma

# def even_no():
#     with open("D:\\PYTHON\\Presonal\\Practice.txt","r") as f:
#         data=f.read()
#         print(data)
#         num=data.split(",")
#         print(num)
#         for i in num:
#             if int(i)%2==0:
#                 print(i,end=" ")

# even_no()

