# for searching specific format
# for matching specific format


# Character classes:

'''We can use character classes to search a group of characters

1. [abc]===>Either a or b or c

2. [^abc] ===>Except a and b and c

3. [a-z]==>Any Lower case alphabet symbol

4. [A-Z]===>Any upper case alphabet symbol

5. [a-zA-Z]==>Any alphabet symbol

6. [0-9] Any digit from 0 to 9

7. [a-zA-Z0-9]==>Any alphanumeric character

8. [^a-zA-Z0-9]==>Except alphanumeric characters (Specia Characters)'''


# Pre defined Character classes:

'''\s→ Space character

\S→ Any character except space character

\d→ Any digit from 0 to 9

\D→ Any character except digit

\w→ Any word character [a-zA-Z0-9]

\W→ Any character except word character (Special Characters)

(.)→ Any character including special characters'''

# Qunatifiers:

'''We can use quantifiers to specify the number of occurrences to match.

a→ Exactly one 'a'

a+→ Atleast one 'a'

a*→ Any number of a's including zero number

a? Atmost one 'a' ie either zero number or one number

a{m}→ Exactly m means(m number of a's)

a{m,n}→ Minimum m number of a's and Maximum n number of a's'''


import re

'''l.finditer()=

start()=return start index

end()=return end Index 

group()=pattern/string
'''

# ex:-

# Syntax:-variable name=re.finditer("Pattern","String")

matcher=re.finditer("is","python is programming language")
for i in matcher:
    print(i.start())
    print(i.end())
    print(i.group())
    
print("<---------------------------------------------------------------------------->")    
   
# Match():check at the starting of the string

mx=re.match("py","python is programming language")
print(i.start(),i.end(),i.group())

print("<---------------------------------------------------------------------------->")


# fullmatch():check all string

x="language"
alpha=re.fullmatch("language",x)
if alpha != None:
    print(alpha.group())

print("<---------------------------------------------------------------------------->")

# WAP to check the given mobile number is valid or not

number="9373129233"

num=re.fullmatch("[6-9][0-9]{9}",number)
if num!=None:
    print("given mobile number is valid")
else:
    print("given mobile number is not valid")


# WAP to check maharashtra number plate is valid or not

numberplate="MH17FR4224"
plate=re.fullmatch("[M][H][0-5][0-9]\w{2}\d{4}",numberplate)
if plate!=None:
    print("Number Plate is valid")
else:
    print("Number plate is not valid")



