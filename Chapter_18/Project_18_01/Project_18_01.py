"""
Random Chore Assignment Emailer
Write a program that takes a list of people’s email addresses and a list
of chores that need to be done and randomly assigns chores to people.
Email each person their assigned chores. If you’re feeling ambitious, keep
a record of each person’s previously assigned chores so that you can make
sure the program avoids assigning anyone the same chore they did last
time. For another possible feature, schedule the program to run once a
week automatically.
Here’s a hint: if you pass a list to the random.choice() function, it will
return a randomly selected item from the list. Part of your code could
look like this:
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
randomChore = random.choice(chores)
chores.remove(randomChore) # this chore is now taken, so remove it

@author Sharaf Qeshta
"""
import random
import smtplib

EMAILS = ['x1@example.com', 'x2@example.com', 'x3@example.com', 'x4@example.com']
CHORES = ['dishes', 'bathroom', 'vacuum', 'walk dog']

sender_email = "fakeemail@gmail.com"
sender_password = "1234567890"
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(sender_email, sender_password)

for recipient_email in EMAILS:
    random_chore = random.choice(CHORES)
    CHORES.remove(random_chore)  # this chore is now taken, so remove it
    smtp_object.sendmail(sender_email, recipient_email, f"Subject: {random_chore}")

smtp_object.quit()
