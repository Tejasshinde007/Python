# 1) Filter(Fun,Sequence):-filter is used to filter the value from sequence bsed on condition 
# l=[1,2,3,4,5,6,7,8,9,10]

# def is_even(n):
#     if n%2==0:
#         return True

# l1=list(filter(is_even,l))
# print(l1)

# Using lambda function

# l=[1,2,3,4,5,6,7,8,9,10]

# l1=list(filter(lambda x:x%2==0,l))
# print(l1)

# 2)Map(fun,sequence):-for every element apply some functionality and generate new element
# using function

# a=[1,2,3,4]
# def cube(n):
#     return n**3

# l2=list(map(cube,a))
# print(l2)


# Using lambda function

# l=[1,2,3,4,5]
# l1=list(map(lambda x:x**3,l))
# print(l1)

# Reduce(fun,sequence):-return single element from sequence
# from functools import reduce

# l=[1,2,3,4,5]

# l1=reduce(lambda x,y:x+y,l)
# print(l1)

'''Scope 
# 1)global variable:-it can access globaly outside the function also
# 2)local variable:-it can access within function or etc.
'''

