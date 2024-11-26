# '''
# *
# **
# ***
# ****
# *****
# '''
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
        

'''
*****
****
***
**
*
'''
# n=5
# for i in range(n+1):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
    


'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
# for i in range(6):
#     for j in range(6):
#         print("*", end=" ")
#     print()


'''
2
4 6
8 12 14
16 18 20 22
'''

a=2
for i in range(2,6):
    for j in range(1,i):
        print(a,end=" ")
        a+=2
    print()
    
    
    
'''
1
22
333
4444
55555
'''    
# a=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()