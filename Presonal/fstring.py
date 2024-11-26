# String Formating
# letters="Hey my name is {} and i am from {}"
# country="India"
# name="Tejas"

# print(letters.format(name,country))
# Hey my name is Tejas and i am from India

# print(letters.format(country,name))
# Hey my name is India and i am from Tejas

# and this is the problem here while formating if we make the changes in the format
# it affect to the statement 
# To encounter that  "f string" introduce

# F string :- ussed to put the variable in the string
# introduce in python version 3.6
# name="Tejas"
# country="India"
# print(f"Hi my name is {name} and i am from {country}")
# Hi my name is {name} and i am from {country} to print this string as it is without taking values we do like this
# print(f"Hi my name is {{name}} and i am from {{country}}")   #just put 2 curly braces
# Hi my name is {name} and i am from {country}
