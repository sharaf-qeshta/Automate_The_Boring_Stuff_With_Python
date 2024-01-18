"""
Image Site Downloader
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that
has a search feature.

@author Sharaf Qeshta
"""

from selenium import webdriver
import re, requests, os

from selenium.webdriver.common.by import By


def download_image(url):
    with open(os.path.basename(url), "wb") as f:
        f.write(requests.get(url).content)


driver = webdriver.Chrome()
original_url = "https://www.flickr.com/search/?text=sea&view_all=1&page={}"

pages = range(1, 5)

for page in pages:
    concat_url = original_url.format(page)
    print("Now it is page", page)
    driver.get(concat_url)
    for element in driver.find_elements(By.CSS_SELECTOR, ".photo-list-photo-view"):
        image_url = 'https:' + re.search(r'url\(\"(.*)\"\)', element.get_attribute("style")).group(1)
        download_image(image_url)
