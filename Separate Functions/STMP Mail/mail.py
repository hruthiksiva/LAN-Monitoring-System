import smtplib

sender = "hruthikphotography@gmail.com"
receiver = "hruthiksivakumar@gmail.com"
password = input(str("password : "))
message = "Hey Whats up"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
print("Login Success")
server.sendmail(sender,receiver,message)
print("Email has been sent to ",receiver)