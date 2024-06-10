import datetime as dt
import random
import pandas
import smtplib

my_email = "put here your email"
password = "put here your generated password"

# tutorial for password = 2. Go to https://myaccount.google.com/
#
# Select Security on the left and scroll down to How you sign in to Google.
#
# Enable 2-Step Verification
#
# 3. Click on 2-Step Verification again, and scroll to the bottom.
#
# There you can add an App password.
#
# Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.
#
# COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
#
# Use this App password in your Python code instead of your normal password.

panda = pandas.read_csv("birthdays.csv")
dict = panda.to_dict()
novo_dict = {}

now = dt.datetime.now()
for index in range(len(dict)):
    novo_dict[dict["name"][index]] = [[dict["email"][index]],(dict["month"][index],dict["day"][index],)]

for content in novo_dict:
    if now.month == novo_dict[content][1][0] and now.day == novo_dict[content][1][1]:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            subject, message = random.choice(list(dict.items()))
            connection.sendmail(from_addr=my_email, to_addrs=novo_dict[content][0],msg=f"Subject:Feliz aniversario {content} \n\n Feliz Aniversario! Hoje e um dia especial, pois celebramos a vida de uma pessoa incrivel: voce! Que este novo ano seja cheio de momentos inesqueciveis, sorrisos e sonhos realizados. Que cada dia te traga mais alegria, amor e sucesso. Voce merece o melhor que a vida pode oferecer. Aproveite cada segundo do seu dia e saiba que voce e muito amado(a). Parabens! Com carinho Fefo, Abracos\n\n(com certeza essa mensagem nao foi automatizada com Python)")