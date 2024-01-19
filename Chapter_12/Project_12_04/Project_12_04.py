"""
Link Verification
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages
that have a 404 “Not Found” status code and print them out as broken links.


@author Sharaf Qeshta
"""

import requests
import bs4

url = 'https://github.com/sharaf-qeshta/Automate_The_Boring_Stuff_With_Python'
response = requests.get(url)
response.raise_for_status()

page_content = bs4.BeautifulSoup(response.text, 'html.parser')

urls = page_content.select('a')
for link in urls:
    link = link.get('href')
    try:
        response = requests.get(link)
        if response.status_code == 404:
            print('404 for: ' + link)
        else:
            print('Working link: ' + link)
            continue
    except requests.exceptions.MissingSchema:
        continue
