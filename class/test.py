# accept 1 string from user
# find the vovels from that string

'''s=input("Enter the sring:-")
a=("a,e,i,o,u")
c=0
for i in s:
    if i in a:
        c+=1
print("count of vovels is:",c)'''

# find length with and without len
'''a="tejas"
print(len(a))
c=0
for i in a:
    c+=1
print(c)'''

# count each character occurance m dict(eg.{"c"=2})
'''s="aabbcdefabced"
d={}
for i in s:
      d[i]=s.count(i)
print(d)'''



# reverse word in string
'''a="tejas shinde"
print(a[::-1])'''

# Write a program that takes any two lists L and M of the same size and adds their elements together 
# to form a new list N whose elements are sums of the corresponding elements in L and M. For instance,
# if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4,6,13].
L = [3, 1, 4]
M = [1, 5, 9]

s=[]
for i in range(len(L)):
    s.append(L[i]+M[i])

print(s)






