import datetime as dt
import pandas as pd
import random
import smtplib

FROM_MAIL = "longwaytogo45@gmail.com"
PWD = ""


today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today_tuple = (today_month, today_day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# checking today is birthday of any one mentioned in the csv file & opting one of the letter_template & sending mail
if today_tuple in birthdays_dict:
    person_data = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", person_data["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=PWD)
        connection.sendmail(from_addr=FROM_MAIL, to_addrs=person_data["email"],
                            msg=f"Subject:Happy Birthday !\n\n{letter_content}")






