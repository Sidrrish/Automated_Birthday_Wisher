import smtplib as smt
import datetime as dt
import random as rd
import pandas


now = dt.datetime.now()
today_tuple = (now.day, now.month)

birthdays = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row.day, data_row.month):data_row for (index, data_row) in birthdays.iterrows()}

if today_tuple in birthdays_dict :

    birthday_person = birthdays_dict[today_tuple]

    with open(f'./letter_templates/letter_{rd.randint(1,3)}.txt') as lt:
        letter = lt.read()
        new_letter = letter.replace('[NAME]', birthday_person['name'])
        print(new_letter)


    my_email = 'your email'
    password = 'application password(not your email password)'

    with smt.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f'Subject:Happy Birthday Ma BOiii \n\n{new_letter}')

