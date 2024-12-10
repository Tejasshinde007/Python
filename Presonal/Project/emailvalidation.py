# email=input("Enter the email: ")
# k,j,d=0,0,0
# if len(email)>=6:
#     if email[0].isalpha():
#       if "@" in email and email.count("@")==1:
#           if email[-4]=="." or email[-3]==".":
#               for i in email:
#                   if i==i.isspace():
#                       k=1
#                   elif i.isalpha():
#                       if i==i.upper():
#                           j=1
#                   elif i.isdigit():
#                       continue
#                   elif i=="_" or i=="." or i=="@":
#                       continue 
#                   else:
#                       d==1
#               if k==1 or j==1 or d==1:
#                    print("check your email")
#               else:
#                   print("Correct email")
                      
#           else:
#               print("check . placing")
#       else:
#           print("should have @ 1 time")
#     else:
#         print("Email should starts with character")    
# else:
#     print("Email should be greate than or equla to 6")


import tkinter as tk
from tkinter import messagebox

def validate_email():
    email = email_entry.get()
    k, j, d = 0, 0, 0
    if len(email) >= 6:
        if email[0].isalpha():
            if "@" in email and email.count("@") == 1:
                if email[-4] == "." or email[-3] == ".":
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i.isupper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i in "_@.":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        messagebox.showerror("Invalid Email", "Check your email.")
                    else:
                        messagebox.showinfo("Valid Email", "Correct email.")
                else:
                    messagebox.showerror("Invalid Email", "Check the placement of '.'")
            else:
                messagebox.showerror("Invalid Email", "Email should contain '@' exactly once.")
        else:
            messagebox.showerror("Invalid Email", "Email should start with a character.")
    else:
        messagebox.showerror("Invalid Email", "Email should be at least 6 characters long.")

# Create the main window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")

# Create and place widgets
prompt_label = tk.Label(root, text="Enter your email:", font=("Arial", 12))
prompt_label.pack(pady=10)

email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.pack(pady=10)

validate_button = tk.Button(root, text="Validate", command=validate_email, font=("Arial", 12))
validate_button.pack(pady=10)

# Run the application
root.mainloop()
