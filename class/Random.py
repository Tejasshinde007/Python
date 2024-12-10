# ramdom function is used to generate ramdom number
from random import *
print("random value:",random())

for i in range(10):
    print(random())
    
print("<-------------------------------------------------------------->")
# 2)randint() function:
# to generate random integer between two given number(inclusive)
print("Ramdom number between 1 to 100:",randint(1,100))
for i in range(10):
    print(randint(1,100))

print("<----------------------------------------------------------------->")
# 3) uniform():
# it returns random float values between 2 given numbers(not inclusive)

for i in range(10):
    print(uniform(1,10))

print("<---------------------------------------------------------------->")
# 4)randrange([start],stop,[step])

for i in range(10):
    print(randrange(10))

print("<------------------------------------------------------------------->")

# 5)choice():
# it wont return random number
# it will return a random object from he given list or tuple

list=["tejas","ashu","Boss","Shooter"]

print(choice(list))


