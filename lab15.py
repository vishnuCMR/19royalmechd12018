import smtplib
s=smtplib.SMTP ('smtp.gmail.com',587)
s.starttls()
s.login("vishnusharmananda@gmail.com", "cricketgod") 
  
# message to be sent 
message = "lets stop texting and hunt for chiks in bangalore"
  
# sending the mail 
s.sendmail("vishnusharmananda@gmail.com", "prajwalbiradar75.com", message)

print("message sent")

  
# terminating the session 
s.quit() 