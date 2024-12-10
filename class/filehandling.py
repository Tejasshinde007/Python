# file Handling

'''Mode 
Write
read 
append
w -> write
w+ -> Write and read
wb -> Write binary
wb+ -> Write binary and read
r  -> Read
r+ -> Read and Write
rb -> Read binary
rb+ -> Read Binary and Write
a -> Append(Write the element at the last of the file)
a+ -> Append and read
ab -> Append Binary
ab+ -> Append Binary and Read '''


# f=open("notes.txt","w+")
# f.write("my name is briuce Wayne")

# print("Text file created")
# f.close()

'''l=["My name is bruce Wayne","\nAnd i am the richest","\nAnd God of Shadows"]
f=open("notes.txt","w+")
f.writelines(l)    # writelines takes the inputs from list and store in the text or etc file
print("Text file created")
f.close()'''

# tell():- it is used to show the current position of cursor
# seek():- seek function is used to move the cursor

# f=open("notes.txt","w+")
# f.write("Hello")
# f.seek(10)
# print("position=",f.tell())
# f.write("my name is tejas")
# print("text file created")
# f.close()


with open("notes.txt","r") as f:
    # f.write("Hii my name is tejas shinde")
    print("my name is")
    print(f.read())









