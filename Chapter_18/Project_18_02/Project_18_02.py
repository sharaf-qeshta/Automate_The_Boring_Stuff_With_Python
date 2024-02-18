"""
Umbrella Reminder
Chapter 12 showed you how to use the requests module to scrape data from
https://weather.gov/. Write a program that runs just before you wake up in
the morning and checks whether it’s raining that day. If so, have the program
 text you a reminder to pack an umbrella before leaving the house.

@author Sharaf Qeshta
"""
import requests
import bs4
from twilio.rest import Client

account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+15559998888'
twilio_number = '+15552225678'


def rain_check():
    url = 'https://weather.com/weather/today/l/Houston+TX?canonicalCityId=e7763a6187b4cb5fd0f85ad30c23f37f320bfe7e910e6fdbe90b501f206d265c'
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    weather_status = soup.select('.CurrentConditions--phraseValue--mZC_p')
    weather = weather_status[0].getText()
    return 'rainy' == weather.lower()


def text_myself(message):
    twilio_client = Client(account_sid, auth_token)
    twilio_client.messages.create(body=message, from_=twilio_number, to=my_number)


def main():
    if rain_check():
        text_myself("remember to take an umbrella with you")


main()
