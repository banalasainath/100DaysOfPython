import smtplib

from_mail = "longwaytogo45@gmail.com"
pwd = ""
# from_mail = "selfmadeachiever@yahoo.com"
# pwd = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    # with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=from_mail, password=pwd)
    connection.sendmail(from_addr=from_mail, to_addrs="selfmadeachiever@yahoo.com",
                        msg="Subject:First Subject\n\nGood Morning")
    # connection.sendmail(from_addr=from_mail, to_addrs="longwaytogo45@gmail.com",
    #                     msg="Subject:First_Subject\n\nGood Morning")
