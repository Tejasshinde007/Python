import smtplib as s 

ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("tejasshinde20033@gmail.com","DJTEJAS@007")
subject="Interview sheduled on 5th DEC."
body="Interview sheduled"
message="Subject:{}\n\n{}".format(subject,body)
listadd=["tejasshinde5156@gmail.com","tejasshinde5651@gmail.com"]
ob.sendmail("tejasshinde20033@gmail.com",listadd,message)
print("mail send")
ob.quit()
 