import smtplib
import datetime as dt
import random


def send_mail(quote_to_send):
    from_mail = "longwaytogo45@gmail.com"
    pwd = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_mail, password=pwd)
        connection.sendmail(from_addr=from_mail, to_addrs="selfmadeachiever@yahoo.com",
                            msg=f"Subject:First Subject\n\n{quote_to_send}")


# from datetime class, calling now() method which will get current time from the system And the now is of type datetime
now = dt.datetime.now()
weekday = now.weekday()
# checking if the day is monday
if weekday == 0:
    with open('quotes.txt') as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    send_mail(quote)
