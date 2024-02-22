import smtplib
  
# change these as per use
your_email = "praveen.gopi717@gmail.com"
your_password = "wsjb dise wtad bspn"
  
# establishing connection with gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)
  

  
# getting the names and the emails
message="hello world"
server.sendmail(your_email,["praveengopi998@gmail.com","condorgalaxy777@gmail.com"],message)
server.close()
  