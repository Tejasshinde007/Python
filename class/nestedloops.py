###########  NESTED LOOPS  #####################

# for i in range(5):      #here the loop will execut once and inner loop will execute till range the it will execute again  
#     for j in range(5):  #here the innner loop will execute first till its range
#         print(i,j)
        #output for this is  
# 0 1
# 0 2
# 0 3
# 0 4
# 1 0
# 1 1
# 1 2
# 1 3
# 1 4
# 2 0
# 2 1
# 2 2
# 2 3
# 2 4
# 3 0
# 3 1
# 3 2
# 3 3
# 3 4
# 4 0
# 4 1
# 4 2
# 4 3
# 4 4
#here the first loop is execute first one tine and the inner loop is execute till its range 

# for i in range (1,6):
#     for j in range(i):
#         print("*",end=" ")  #End is used for print the output in the same line without printing new linw
#     print()                 #print() is used for empty line

# # to see the difference
# for i in range (1,6):
#     for j in range(i):
#         print("*")  
#     print()    


#OUTPUT
# *

# *
# *

# *
# *
# *

# *
# *
# *
# *

# *
# *
# *
# *
# *
    


# for i in range (1,6):
#     for j in range(i):
#         print("*",end=" ")  
#output
# * * * * * * * * * * * * * * * 



# a=1
# for i in range (5):
#     for j in range(i):
#         print(a,end=" ")
#         a+=1  
#     print()
    
#OUTPUT     
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10



# for i in range (5):
#     for j in range(5):
#         print("* ",end=" ") 
#     print()




# # ASCII
# # A=65   97-a 
# # Z=90   122-2



# a=0
# for i in range(6):
#         for j in range(i):
#                 print(a,end=" ")
#                 a+=2
#         print()

# #output
# 0 
# 2 4 
# 6 8 10 
# 12 14 16 18 
# 20 22 24 26 28 

# a=2
# for i in range(1,6):
#         for j in range(i):
#                 print(a,end=" ")
#         a*=2
#         print()

#OUTPUT
# 2 
# 4 4 
# 8 8 8 
# 16 16 16 16 
# 32 32 32 32 32 


# n=5
# for i in range(n):
#         for j in range(i):
#                 print(" ",end=" ")
#         for k in range(n-i):
#                 print("*",end=" ")
#         print()
   
# #OUTPUT     
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 


# a=65
# for i in range(65,70):
#         for j in range(65,i):
#                 print(chr(a),end=" ")
#                 a+=1
#         print()

# #output
# A 
# B C 
# D E F 
# G H I J 


# a=97
# for i in range(97,102):
#         for j in range(97,i):
#                 print(chr(a),end=" ")
#                 a+=1
#         print()
# #output
# a 
# b c 
# d e f 
# g h i j 



# a=97
# for i in range(97,102):
#         for j in range(97,i+1):
#                 print(chr(a),end=" ")
#         a+=1
#         print()
        
# #output
# a 
# b b 
# c c c 
# d d d d 
# e e e e e 